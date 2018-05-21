
from oic.utils.authn.user import UserAuthnMethod

from oic.utils.http_util import *
from mako.lookup import TemplateLookup

import pyqrcode
from userManager import UserManager

# ----------------------------------------------------------------------------

ROOT = './'

LOOKUP = TemplateLookup(directories=[ROOT + 'templates', ROOT + 'htdocs'],
                        module_directory=ROOT + 'modules',
                        input_encoding='utf-8', output_encoding='utf-8')

# ----------------------------------------------------------------------------

class Modifier_module:

    def __init__(self, srv, tmako, template_lookup, totp, pwd):
        """
        :param srv: The server instance
        :param tmako: Template mako
        :param template_lookup: template lookup
        :param totp: TOTP dictionary like database
        :param pwd: Username/password dictionary like database
        :return:
        """
        UserAuthnMethod.__init__(self, srv)
        self.totp = totp
        self.passwd = pwd
        self.mako_template = tmako
        self.template_lookup = template_lookup
        # self.verification_endpoints = verification_endpoints or ["verify"]
        # self.return_to = return_to

    # //---------------------------------------------------------

    def modify_password(username, password, newpassword):
        """
        Update the password
        """
        resp = Response("OK")
        if UserManager.verify_match(username, password):
            """
            Update the password
            """
            try:
                usernm = UserManager._update_password(username, newpassword)

                mako_template = LOOKUP.get_template('modify_pwd.mako')

            except RuntimeError:
                resp = BadRequest("Username not found")
                return False, resp
        else:
            resp = BadRequest("Username/password mismatch")
            return False, resp
        return True, resp

    def modify_totp(username, password):
        """
        Update the TOTP secret
        """
        resp = Response("OK")

        if UserManager.verify_match(username, password):
            try:
                totp_secret = UserManager._reset_totp(username)

                otpauth_link = 'otpauth://totp/%s?secret=%s' % (username, totp_secret)
                qr_code = pyqrcode.create(otpauth_link)

                template_args = {
                    'username': username,
                    'totp_secret': totp_secret,
                    'qr_blob': qr_code.png_as_base64_str(scale=5)
                }

                mako_template = LOOKUP.get_template('modify_totp.mako')
                resp.message = mako_template.render(**template_args)
            except RuntimeError:
                resp = BadRequest("Username not found")
        else:
            resp = BadRequest("Username/password mismatch")
        return resp