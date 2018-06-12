import base64
import logging
import time
import six
import pyotp

from oic.utils.authn.user import UserAuthnMethod

from future.backports.urllib.parse import parse_qs
from future.backports.urllib.parse import urlsplit
from future.backports.urllib.parse import urlunsplit
from future.backports.urllib.parse import urlencode
from future.backports.urllib.parse import unquote

from oic.exception import PyoidcError

from oic.utils import aes
from oic.utils.http_util import Response
from oic.utils.http_util import CookieDealer
from oic.utils.http_util import InvalidCookieSign
from oic.utils.http_util import SeeOther
from oic.utils.http_util import Unauthorized

LOC = {
    "en": {
        "title": "User log in",
        "login_title": "Username",
        "passwd_title": "Password",
        "submit_text": "Submit",
        "client_policy_title": "Client Policy",
        "wrong_value": 0},
    "se": {
        "title": "Logga in",
        "login_title": u"Användarnamn",
        "passwd_title": u"Lösenord",
        "submit_text": u"Sänd",
        "client_policy_title": "Klientens sekretesspolicy"
    }
}


class TOTPAuthn(UserAuthnMethod):
    param_map = {"as_user": "login", "acr_values": "acr",
                 "policy_uri": "policy_uri", "logo_uri": "logo_uri",
                 "tos_uri": "tos_uri", "query": "query"}

    #
    # def __init__(self, srv, get_totp_secret_key, template_lookup, return_to="", verification_endpoints=None):
    #     UserAuthnMethod.__init__(self, srv)
    #     self.get_totp_secret_key = get_totp_secret_key
    #     self.template_lookup = template_lookup
    #     self.return_to = return_to
    #     self.verification_endpoints = verification_endpoints or ["verify"]
    #     self.templ_arg_func = self.template_args

    def __init__(self, srv, mako_template, template_lookup, get_totp_secret_key, return_to="",
                 templ_arg_func=None, verification_endpoints=None, nerror=0):
        """
        :param srv: The server instance
        :param mako_template: Which Mako template to use
        :param pwd: Username/password dictionary like database
        :param return_to: Where to send the user after authentication
        :return:
        """
        UserAuthnMethod.__init__(self, srv)
        self.nerrors = nerror
        self.mako_template = mako_template
        self.template_lookup = template_lookup
        self.get_totp_secret_key = get_totp_secret_key
        self.return_to = return_to
        # if verification_endpoints != None:
        #    self.return_to = verification_endpoints[0]
        self.verification_endpoints = verification_endpoints or ["verify"]
        if templ_arg_func:
            self.templ_arg_func = templ_arg_func
        else:
            self.templ_arg_func = self.template_args

    def template_args(self, end_point_index=0, **kwargs):
        """
        Method to override if necessary, dependent on the page layout
        and context
        :param kwargs:
        :return: dictionary of parameters used to build the Authn page
        """

        print("KWARGSTOT: ", kwargs)

        try:
            action = kwargs["action"]
        except KeyError:
            action = self.verification_endpoints[end_point_index]

        print("MANOLOOOOOOO: ", parse_qs(kwargs["request"])['url'][0])
        argv = {"password": "", "action": action, "url": parse_qs(kwargs["request"])['url'][0]}

        for fro, to in self.param_map.items():
            try:
                argv[to] = kwargs[fro]
            except KeyError:
                argv[to] = ""

        if "extra" in kwargs:
            for param in kwargs["extra"]:
                try:
                    argv[param] = kwargs[param]
                except KeyError:
                    argv[param] = ""

        try:
            _locs = kwargs["ui_locales"]
        except KeyError:
            argv.update(LOC["en"])
        else:
            for loc in _locs:
                try:
                    argv.update(LOC[loc])
                except KeyError:
                    pass
                else:
                    break
        try:
            argv.update({
                'title': 'TOTP verification',
                'form_action': self.verification_endpoints[end_point_index],
                'username': parse_qs(kwargs["request"])["login"][0]
            })
            # print("KWARGS2: ",kwargs)
        except KeyError:
            print("KWARGS: ", kwargs)
        return argv

    def __call__(self, cookie=None, end_point_index=0, **kwargs):
        """
        Put up the login form
        """
        resp = Response()
        self.nerror = 0
        template_args = self.templ_arg_func(end_point_index, **kwargs)

        # mako_template_engine = self.template_lookup.get_template('totp_form.mako')
        mako_template_engine = self.template_lookup.get_template(self.mako_template)
        resp.message = mako_template_engine.render(**template_args).decode("utf-8")

        return resp

    def verify(self, request, **kwargs):
        """
        Verifies that the given totp was correct
        :param request: Either the query part of a URL a urlencoded
        body of a HTTP message or a parse such.
        :param kwargs: Catch whatever else is sent.
        :return: redirect back to where ever the base applications
        wants the user after authentication.
        """
        if isinstance(request, six.string_types):
            _dict = parse_qs(request)
        elif isinstance(request, dict):
            _dict = request
        else:
            raise ValueError("Wrong type of input")

        # verify totp
        try:
            # Do verification
            totp_generator = pyotp.TOTP(self.get_totp_secret_key(_dict["username"][0]))
            assert (True == totp_generator.verify(_dict["totp"][0]))
        except (AssertionError, KeyError):
            resp = Unauthorized("Wrong TOTP")
            ##resp = Unauthorized("Unknown user or wrong password")

            kwargs["request"] = request
            kwargs["form_action"] = kwargs["url"]
            argv = self.templ_arg_func(0, **kwargs)
            argv['wrong_value'] = 1
            argv['form_action'] = kwargs["baseurl"] + "/totp_login"
            argv['username'] = _dict['username'][0]
            argv['acr'] = argv['form_action']
            argv['title'] = 'TOTP verification'

            self.nerror = self.nerror + 1
            if (self.nerror>=3):
                self.nerror = 0
                argv['wrong_value'] = 4

            mte = self.template_lookup.get_template('totp_form.mako')
            resp.message = mte.render(**argv).decode("utf-8")
            return resp, False

        else:
            # If I remove this header, authentication enters in a infinite loop.
            headers = [self.create_cookie(_dict["username"][0], "upm")]
            try:
                _qp = _dict["query"][0]
            except KeyError:
                _qp = self.get_multi_auth_cookie(kwargs['cookie'])
            try:
                return_to = self.generate_return_url(kwargs["return_to"], _qp)
            except KeyError:
                try:
                    return_to = self.generate_return_url(self.return_to, _qp,
                                                         kwargs["path"])
                except KeyError:
                    return_to = self.generate_return_url(self.return_to, _qp)

            return SeeOther(return_to, headers=headers), True

    def done(self, areq):
        try:
            _ = areq[self.query_param]
            return False
        except KeyError:
            return True