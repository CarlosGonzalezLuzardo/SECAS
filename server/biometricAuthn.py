import base64
import logging
import time
import six
import pyotp
import requests
import json
import ast

import zeep
from zeep import Client

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


import wave

# import VoiceVerification
VVOPS='https://vv.sestek.com/VVOperations.asmx'


LOC = {
    "en": {
        "title": "Biometric authentication",
        "file_label": "Voiceprint recording:",
        "button_label": "Submit voiceprint (Check before submit it):",
        "submit_text": "Submit",
        "client_policy_title": "Client Policy",
        "thefile2": "",
        "wrong_value": 0},
    "se": {
        "title": u"Biometrisk autentisering",
        "file_label": u"Välj en fil att ladda upp:",
        "button_label": u"Ladda upp fil",
        "submit_text": u"Sänd",
        "client_policy_title": "Klientens sekretesspolicy"
    }
}

class BiometricAuthn(UserAuthnMethod):

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

    def __init__(self, srv, mako_template, template_lookup, get_userData, return_to="",
                 templ_arg_func=None, verification_endpoints=None):
        """
        :param srv: The server instance
        :param mako_template: Which Mako template to use
        :param pwd: Username/password dictionary like database
        :param return_to: Where to send the user after authentication
        :return:
        """
        UserAuthnMethod.__init__(self, srv)
        self.mako_template = mako_template
        self.template_lookup = template_lookup
        self.get_userData = get_userData

        self.nerror=0
        #if verification_endpoints == None:
        self.return_to = return_to
        #else:
        #   self.return_to = verification_endpoints[0]
        self.verification_endpoints = verification_endpoints or ["verify"]

        self.clientwsdl = Client(VVOPS+'?WSDL')

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
        print("KWARGSBIOMETRIC:",kwargs)
        try:
            action = kwargs["action"]
        except KeyError:
            action = self.verification_endpoints[end_point_index]
        argv = {"password": "", "action": action, 'username': parse_qs(kwargs["request"])['username'][0], "url": parse_qs(kwargs["request"])['url'][0]}
                #'username': parse_qs(kwargs["request"])["The connection fail"][0]}
        print("KWARGSBIOMETRICREQUEST:",kwargs["request"])
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
        print("ARGVVVVVVVVVVVVVVVVV: ",argv)
        return argv


    def __call__(self, cookie=None, end_point_index=0, **kwargs):
        """
        Put up the biom form
        """
        resp = Response()

        template_args = self.templ_arg_func(end_point_index, **kwargs)

        mako_template_engine = self.template_lookup.get_template(self.mako_template)
        resp.message = mako_template_engine.render(**template_args).decode("utf-8")

        return resp


    def _verify(self,name,soundfile,custData=[]):

        try:
            #with open(soundfile) as wavefile:
                #wave_params=wavefile.getparams()

            newwavefile='newwave.wav'
            # with wave.open(newwavefile,'wb') as newwave:
            #     newwave.setparams(wave_params[0],wave_params[1],8000,wave_params[3],wave_params[4],wave_params[5])

            userData=self.get_userData(name)
            userCode=userData[0]
            contentCode=userData[1]
            channelCode=userData[2]
            utteranceText=userData[3]

            isRecog = False
            if utteranceText is not '':
                isRecog=True

            ## wav byte[] Voice data (8kHz 16bit PCM wav format)
            ## wave(nchannels, sampwidth, framerate, nframes, comptype, compname)
            ## ResultCode,ResultText,ResultScore,ResultGender,TransactionId =
            # VoiceVerification.AuthenticateVoicePrint(userCode,contentCode,channelCode,utteranceText,
            # soundfile,isRecog,custData)
                results = \
                    self.clientwsdl.service.AuthenticateVoicePrint(userCode, contentCode,\
                    channelCode, utteranceText, soundfile.read(), isRecog)

                #results = self.clientwsdl.service.GetVoicePrintStatus(userCode, contentCode,\
                #            channelCode)
            #results = [-100,'error test']

            if results.ResultCode < -99:
                raise AssertionError(results.ResultText)
            if results.ResultCode < 0:
                raise AssertionError(results.ResultText)

        except wave.Error:
            raise wave.Error

    def verify(self, request, **kwargs):
        """
        Verifies that the given value was correct
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

        orig_pkg = _dict["thefile2"][0]
        orig_audio=base64.b64decode(orig_pkg)
        head, data = orig_audio.decode('ascii').split(',')
        data = base64.b64decode(data)

        # Verify Biometric Authentication
        try:
            # Do verification
            with open('audiofile.wav', 'wb') as f:
                soundfile = f.write(data)
            with open('audiofile.wav', 'rb') as soundfile:
                print("DICTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT: ", _dict["username"][0])
                self._verify(_dict["username"][0],soundfile)
        except (AssertionError, KeyError):
            if (self.nerror>=3):
                self.nerror = 0
                resp = Unauthorized("Voice not recognized")

                kwargs["request"] = request
                kwargs["form_action"] = kwargs["url"]
                argv = self.templ_arg_func(0, **kwargs)
                argv['wrong_value'] = 3
                argv['form_action'] = kwargs["baseurl"] + "/user_password"
                argv['login_title'] = "Username"
                argv['passwd_title'] = "Password"
                argv['acr'] = argv['form_action']
                argv['title'] = 'User log in'
                mte = self.template_lookup.get_template('login.mako')
                resp.message = mte.render(**argv).decode("utf-8")

                return resp, False
            else:
                self.nerror = self.nerror+1
                resp = Unauthorized("Voice not recognized")

                kwargs["request"] = request
                kwargs["form_action"] = kwargs["url"]
                argv = self.templ_arg_func(0, **kwargs)
                argv['wrong_value'] = 1
                argv['form_action'] = kwargs["baseurl"] + "/biom_login"
                argv['username'] = _dict['username'][0]
                argv['acr'] = argv['form_action']
                argv['title'] = 'TOTP verification'
                argv['recover_uri'] = "recover_user"
                argv['register_uri'] = "register_user"
                mte = self.template_lookup.get_template('biom_form.mako')
                resp.message = mte.render(**argv).decode("utf-8")

                return resp, False
                raise
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