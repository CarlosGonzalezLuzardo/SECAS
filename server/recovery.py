
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

class recovery_module:

    def __init__(self, username):
        """
        :param username: Username
        :param template_lookup: template lookup
        :return:
        """
        self.username = username
        self.template_lookup = LOOKUP
        self.mako_template = 'recover_pwd.mako'
        self.mako_template2 = 'ask_question.mako'
        self.mako_template3 = 'new_pwd.mako'
        # self.template_lookup = template_lookup
        # self.verification_endpoints = verification_endpoints or ["verify"]
        # self.return_to = return_to

    def __call__(self, cookie=None, end_point_index=0, **kwargs):
        """
        Put up the username form
        """
        resp = Response()

        template_args = self.templ_arg_func(end_point_index, **kwargs)

        # mako_template_engine = self.template_lookup.get_template('totp_form.mako')
        mako_template_engine = self.template_lookup.get_template(self.mako_template)
        resp.message = mako_template_engine.render(**template_args).decode("utf-8")

        return resp
    # //---------------------------------------------------------

    def show_question(self):
        """
        Returns the secret question for the given user
        :param username: Username given by the user
        :return:
        """
        resp = Response("OK")
        try:
            question_str = UserManager._read_lostqstn(self.username)
            # question_str = 'Have you lost your marbles'

            template_args = {
                'title':'Password Recovery',
                'question':'Question: ',
                'question_str':question_str,
                'submit_text':'Submit',
            }


            mako_template = LOOKUP.get_template(self.mako_template2)
            resp.message = mako_template.render(**template_args)
        except RuntimeError:
            resp = BadRequest("Username not found")
        return resp

        # return UserManager._read_lostqstn(username)
        # return 'have you lost your marbles?'

    def check_answer(self,answer):
        """
        Checks if the answer is correct
        :param username: Username given by the user
        :param answer: Answer to the question
        :return:
        """
        resp = Response("OK")
        try:
            # question_str = UserManager.verify_lostpwd(self.username,answer)

            if UserManager.verify_lostpwd(self.username,answer):

                template_args = {
                    'title':'Password Recovery',
                    'password_title':'New password: ',
                    'newpassword_title':'New password: ',
                    'submit_text':'Submit',
                }

                mako_template = LOOKUP.get_template(self.mako_template3)
                resp.message = mako_template.render(**template_args)
        except RuntimeError:
            resp = BadRequest("Username not found")
        return resp

    def update_password(self,newpassword):
        """
        Updates the password
        :param username: Username given by the user
        :param newpassword: New Password selected by the user
        """
        resp = Response("OK")
        try:
            usernm = UserManager._update_password(self.username, newpassword)

            # mako_template = LOOKUP.get_template(self.mako_template3)

        except RuntimeError:
            resp = BadRequest("Username %s not found" % self.username)

        """
        Update the TOTP secret
        """
        try:
            totp_secret = UserManager._reset_totp(self.username)

            otpauth_link = 'otpauth://totp/%s?secret=%s' % (self.username, totp_secret)
            qr_code = pyqrcode.create(otpauth_link)

            template_args = {
                'username': self.username,
                'totp_secret': totp_secret,
                'qr_blob': qr_code.png_as_base64_str(scale=5)
            }

            mako_template = LOOKUP.get_template('modify_totp.mako')
            resp.message = mako_template.render(**template_args)
        except RuntimeError:
            resp = BadRequest("Username not found")
        return resp