from oic.utils.authn.user import UsernamePasswordMako
import bcrypt
import logging

import base64
import time
import six

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
from oic.utils.sanitize import sanitize

logger = logging.getLogger(__name__)
LOC = {
    "en": {
        "title": "User log in",
        "login_title": "Username",
        "passwd_title": "Password",
        "submit_text": "Submit",
        "client_policy_title": "Client Policy",
        "recover_uri":'recover_user',
        "register_uri":'register_user', ##register_uri
        "wrong_value": 0},
    "se": {
        "title": "Logga in",
        "login_title": u"Användarnamn",
        "passwd_title": u"Lösenord",
        "submit_text": u"Sänd",
        "client_policy_title": "Klientens sekretesspolicy",
        "recover_uri":'recover_user',
        "register_uri":'register_user'
    }
}
class UserPassBcryptMako(UsernamePasswordMako):
    """Do user authentication using the normal username password form in a
    WSGI environment using Mako as template system."""


    def _verify(self, pwd, user):
        hashed = bcrypt.hashpw(pwd.encode(), self.passwd(user))
        assert hashed == self.passwd(user), "Passwords don't match."

    param_map = {"as_user": "login", "acr_values": "acr",
                 "policy_uri": "policy_uri", "logo_uri": "logo_uri",
                 "tos_uri": "tos_uri", "query": "query"}

    def template_args(self, end_point_index=0, **kwargs):
        """
        Method to override if necessary, dependent on the page layout
        and context

        :param kwargs:
        :return: dictionary of parameters used to build the Authn page
        """

        try:
            action = kwargs["action"]
        except KeyError:
            action = self.verification_endpoints[end_point_index]

        argv = {"password": "", "action": action, "url": "https://172.16.3.159:8092/authorization?"+kwargs["query"]}

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

        return argv