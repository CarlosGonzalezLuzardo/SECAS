# !/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys
import os
import traceback
import base64
import wave
import random
import io
import array

from tempfile import TemporaryFile
import cgi

from future.backports.urllib.parse import parse_qs

from oic.utils import shelve_wrapper
from oic.utils.authn.javascript_login import JavascriptFormMako

from oic.utils.authn.client import verify_client
from oic.utils.authn.multi_auth import setup_multi_auth
from oic.utils.authn.multi_auth import AuthnIndexedEndpointWrapper
from oic.utils.authn.saml import SAMLAuthnMethod
from oic.utils.authn.user import UsernamePasswordMako
from oic.utils.authz import AuthzHandling
from oic.utils.keyio import keyjar_init
from oic.utils.userinfo import UserInfo
from oic.utils.userinfo.aa_info import AaUserInfo
from oic.utils.webfinger import WebFinger
from oic.utils.webfinger import OIC_ISSUER
from oic.utils.authn.authn_context import AuthnBroker
from oic.utils.authn.authn_context import make_auth_verify
from oic.utils.time_util import utc_time_sans_frac


__author__ = 'rohe0002'

import re

from oic.oic.provider import Provider
from oic.oic.provider import EndSessionEndpoint
from oic.utils.http_util import *

from mako.lookup import TemplateLookup

from urllib.parse import parse_qs as urllib_parse_qs
import pyqrcode
from TOTPAuthn import TOTPAuthn
from modifydb import Modifier_module
from recovery import recovery_module
from biometricAuthn import BiometricAuthn
# from userManager import PASSWD, TOTP_SECRETS, UserManager
from userManager import UserManager
from UserPassAuthn import UserPassBcryptMako

from voiceReg import BiometricEnrollment

# This is *NOT* good practice !!
try:
    from requests.packages import urllib3
except ImportError:
    pass
else:
    urllib3.disable_warnings()

from http.cookies import SimpleCookie

LOGGER = logging.getLogger("")
LOGFILE_NAME = 'oc3.log'
hdlr = logging.FileHandler(LOGFILE_NAME)
base_formatter = logging.Formatter(
    "%(asctime)s %(name)s:%(levelname)s %(message)s")

CPC = ('%(asctime)s %(name)s:%(levelname)s '
       '[%(client)s,%(path)s,%(cid)s] %(message)s')
cpc_formatter = logging.Formatter(CPC)

hdlr.setFormatter(base_formatter)
LOGGER.addHandler(hdlr)
LOGGER.setLevel(logging.DEBUG)

logger = logging.getLogger('oicServer')

URLMAP = {}
NAME = "pyoic"
OAS = None

JWKS_FILE_NAME = "static/jwks.json"

ROOT = './'
LOOKUP = TemplateLookup(directories=[ROOT + 'templates', ROOT + 'htdocs'],
                        module_directory=ROOT + 'modules',
                        input_encoding='utf-8', output_encoding='utf-8')


# ----------------------------------------------------------------------------


def static_file(path):
    try:
        os.stat(path)
        return True
    except OSError:
        return False


# noinspection PyUnresolvedReferences
def static(self, environ, start_response, path):
    logger.info("[static]sending: %s" % (path,))

    try:
        data = open(path, 'rb').read()
        if path.endswith(".ico"):
            start_response('200 OK', [('Content-Type', "image/x-icon")])
        elif path.endswith(".html"):
            start_response('200 OK', [('Content-Type', 'text/html')])
        elif path.endswith(".json"):
            start_response('200 OK', [('Content-Type', 'application/json')])
        elif path.endswith(".txt"):
            start_response('200 OK', [('Content-Type', 'text/plain')])
        elif path.endswith(".css"):
            start_response('200 OK', [('Content-Type', 'text/css')])
        else:
            start_response('200 OK', [('Content-Type', "text/xml")])
        return [data]
    except IOError:
        resp = NotFound()
        return resp(environ, start_response)


def check_session_iframe(self, environ, start_response, logger):
    return static(self, environ, start_response, "htdocs/op_session_iframe.html")


# ----------------------------------------------------------------------------


def key_rollover(self, environ, start_response, _):
    # expects a post containing the necessary information
    _txt = get_post(environ)
    _jwks = json.loads(_txt)
    logger.info("Key rollover to")
    OAS.do_key_rollover(_jwks, "key_%d_%%d" % int(time.time()))
    # Dump to file
    f = open(JWKS_FILE_NAME, "w")
    f.write(json.dumps(OAS.keyjar.export_jwks()))
    f.close()
    resp = Response("OK1")
    return resp(environ, start_response)


def clear_keys(self, environ, start_response, _):
    OAS.remove_inactive_keys()
    resp = Response("OK2")
    return resp(environ, start_response)


# --------------------------------------------------------------------------

def test(environ, start_response):
    resp = Response("OK3")
    template_args = {
        'title': 'Password Update',
        'username_title': 'Username',
        'password_title': 'Old Password',
        'newpassword_title': 'New Password',
        'submit_text': 'Submit'
    }
    if (environ['REQUEST_METHOD'] == 'GET'):
        mako_template = LOOKUP.get_template('modify_pwd.mako')
        resp.message = mako_template.render(**template_args).decode('utf-8')
    elif (environ['REQUEST_METHOD'] == 'POST'):
        registration_info = urllib_parse_qs(environ['wsgi.input'].read().decode('utf-8'), True)

        username = registration_info['username'][0]
        password = registration_info['password'][0]
        newpassword = registration_info['newpassword'][0]

        if newpassword != '':
            resp = Modifier_module.modify_password(username, password, newpassword)
        else:
            resp = Modifier_module.modify_totp(username, password)

    return resp(environ, start_response)


def modifier(environ, start_response):
    resp = Response("OK3")
    ##username = self.username
    if 'HTTP_COOKIE' in environ:
        cookie = SimpleCookie(environ['HTTP_COOKIE'])
        if 'username' in cookie:
            # handle the cookie value
            username = cookie['username'].value

    template_args = {
        'title': 'Password Update',
        'username_title': 'Username',
        'username': username,
        'password_title': 'Old Password',
        'newpassword_title': 'New Password',
        'confnewpassword_title': 'Confirm New Password',
        'wrong_code': "",
        'wrong_value': 0,
        'url': environ['HTTP_REFERER'],
        'submit_text': 'Submit'
    }
    if (environ['REQUEST_METHOD'] == 'GET'):
        mako_template = LOOKUP.get_template('modify_pwd.mako')
        resp.message = mako_template.render(**template_args).decode('utf-8')
    elif (environ['REQUEST_METHOD'] == 'POST'):
        registration_info = urllib_parse_qs(environ['wsgi.input'].read().decode('utf-8'), True)

        username = username = cookie['username'].value
        password = registration_info['password'][0]
        newpassword = registration_info['newpassword'][0]
        template_args['url'] = registration_info['url'][0]

        if newpassword != '':
            resp = Modifier_module.modify_password(username, password, newpassword)
        else:
            resp = Modifier_module.modify_totp(username, password)

        if (resp[0] == True):
            template_args['wrong_value'] = 1
        else:
            template_args['wrong_value'] = 2
        resp = Response("OK")
        mako_template = LOOKUP.get_template('modify_pwd.mako')
        resp.message = mako_template.render(**template_args).decode('utf-8')

    return resp(environ, start_response)


def pwd_recovery(environ, start_response):
    resp = Response("Fail in pass_recovery")

    template_args = {
        'title': 'Password Recovery',
        'username_title': 'Username',
        'username_used': 'username_used',
        'submit_text': 'Submit',
        'url': environ['HTTP_REFERER']

    }

    if (environ['REQUEST_METHOD'] == 'GET'):
        template_args['url']= environ['HTTP_REFERER']
        template_args['username_used'] = 0
        mako_template = LOOKUP.get_template('recover_pwd.mako')
        resp.message = mako_template.render(**template_args).decode('utf-8')
    elif (environ['REQUEST_METHOD'] == 'POST'):
        registration_info = urllib_parse_qs(environ['wsgi.input'].read().decode('utf-8'), True)
        url = registration_info['url'][0]
        ################
        # Cookie break #
        if 'HTTP_COOKIE' in environ:
            cookie = SimpleCookie(environ['HTTP_COOKIE'])
            if 'username' in cookie:
                # handle the cookie value
                username = cookie['username'].value
        #################
        print("REGISTRATION_INFO: ", registration_info)
        if 'username' in registration_info:
            username = registration_info['username'][0]
            url = registration_info['url'][0]
            recover_unit = recovery_module(username)
            resp = recover_unit.show_question(url)

            if not UserManager.verify_username(username):
                template_args['url'] = url
                template_args['username_used'] = 2
                mako_template = LOOKUP.get_template('recover_pwd.mako')
                resp.message = mako_template.render(**template_args).decode('utf-8')



            ################
            # Cookie break #
            cookie = SimpleCookie()
            cookie['username'] = username
            cookieheaders = ('Set-Cookie', cookie['username'].OutputString())
            headers = [cookieheaders, ('content-type', 'text/html')]
            # add headers without triggering start_response
            resp.headers = headers
            #################

        elif 'question_ans' in registration_info:
            answers = registration_info['question_ans'][0]
            url = registration_info['url'][0]
            recover_unit = recovery_module(username)
            resp = recover_unit.check_answer(answers, url)

        elif 'newpassword' in registration_info:
            password = registration_info['password'][0]
            newpassword = registration_info['newpassword'][0]
            url = registration_info['url'][0]
            if newpassword == "" or password == "":
                return resp('password not found')
            elif newpassword != password:
                return resp('300 Retype password mismatch')
            else:
                recover_unit = recovery_module(username)
                resp = recover_unit.update_password(newpassword, url)

    return resp(environ, start_response)


def register_user(environ, start_response):
    resp = Response("OK4")

    if (environ['REQUEST_METHOD'] == 'GET'):
        template_args = {
            'title': 'Registration',
            'username_title': 'Username',
            'password_title': 'Password',
            'password_title2': 'Repeat Password',
            'question_title': 'Recovery Question',
            'answer_title': 'Answer',
            'answer_title2': 'Repeat Answer',
            'audio_title': 'Submit audio',
            'audio_button': 'Submit audio',
            'submit_text': 'Submit',
            'username_used': 'username_used',
            'username_title_value': "",
            'question_title_value': "",
            'url': environ['HTTP_REFERER'],
            'voice_submited': 0
        }

        resp = Response("OK51")
        template_args['username_used'] = 0
        mako_template = LOOKUP.get_template('registration.mako')
        resp.message = mako_template.render(**template_args).decode("utf-8")
    elif (environ['REQUEST_METHOD'] == 'POST'):
        registration_info = urllib_parse_qs(environ['wsgi.input'].read().decode('utf-8'))
        username = registration_info['username'][0]
        password = registration_info['password'][0]
        password2 = registration_info['password2'][0]
        question = registration_info['question'][0]
        answer = registration_info['answer'][0]
        answer2 = registration_info['answer2'][0]
        username_used = registration_info['username_used'][0]
        url = registration_info['url'][0]
        voice_submited = registration_info['voice_submited'][0]

        template_args = {
            'title': 'Registration',
            'username_title': "Username",
            'password_title': 'Password',
            'password_title2': 'Repeat Password',
            'question_title': 'Recovery Question',
            'answer_title': 'Answer',
            'answer_title2': 'Repeat Answer',
            'audio_title': 'Submit audio',
            'audio_button': 'Submit audio',
            'submit_text': 'Submit',
            'username_used': 0,
            'username_title_value': "",
            'question_title_value': "",
            'url': url,
            'voice_submited': 0
        }
        if UserManager.verify_username(username):
            username_used1 = True
            # template_args = {
            #     'title': 'Registration',
            #     'username_title': 'Username',
            #     'password_title': 'Password',
            #     'password_title2': 'Repeat Password',
            #     'question_title': 'Recovery Question',
            #     'answer_title': 'Answer',
            #     'answer_title2': 'Repeat Answer',
            #     'audio_title': 'Submit audio',
            #     'audio_button': 'Submit audio',
            #     'submit_text': 'Submit',
            #     'username_used':'username_used'
            # }

            resp = Response("OK51")
            template_args['username_used'] = 1
            mako_template = LOOKUP.get_template('registration.mako')
            resp.message = mako_template.render(**template_args).decode("utf-8")
        else:
            username_used1 = False

            # template_args = {
            #     'title': 'Registration',
            #     'username_title': "Username",
            #     'password_title': 'Password',
            #     'password_title2': 'Repeat Password',
            #     'question_title': 'Recovery Question',
            #     'answer_title': 'Answer',
            #     'answer_title2': 'Repeat Answer',
            #     'audio_title': 'Submit audio',
            #     'audio_button': 'Submit audio',
            #     'submit_text': 'Submit',
            #     'username_used': 2,
            #     'username_title_value': username,
            #     'question_title_value': question
            # }
            if password != password2:
                resp = BadRequest("Password mismatch")
                # template_args = {
                #     'title': 'Registration',
                #     'username_title': "Username",
                #     'password_title': 'Password',
                #     'password_title2': 'Repeat Password',
                #     'question_title': 'Recovery Question',
                #     'answer_title': 'Answer',
                #     'answer_title2': 'Repeat Answer',
                #     'audio_title': 'Submit audio',
                #     'audio_button': 'Submit audio',
                #     'submit_text': 'Submit',
                #     'username_used': 2,
                #     'username_title_value': username,
                #     'question_title_value': question
                # }
                template_args['username_used'] = 2
                template_args['username_title_value'] = username
                template_args['question_title_value'] = question
                mako_template = LOOKUP.get_template('registration.mako')
                resp.message = mako_template.render(**template_args).decode("utf-8")
            elif answer != answer2:
                resp = BadRequest("Answer mismatch")
                template_args['username_used'] = 3
                template_args['username_title_value'] = username
                template_args['question_title_value'] = question
                mako_template = LOOKUP.get_template('registration.mako')
                resp.message = mako_template.render(**template_args).decode("utf-8")
            else:
                userData = [username, 'English', 'Mixed', 'my voice is my password']
                biom = BiometricEnrollment(userData)

                ################
                # Cookie break #
                cookie = SimpleCookie()
                cookie['username'] = username
                cookie['channel'] = 'English'
                cookie['type'] = 'Mixed'
                cookie['utterText'] = 'my voice is my password'
                cookieheaders = ('Set-Cookie', cookie['username'].OutputString())
                headers = [cookieheaders, ('content-type', 'text/html')]
                # add headers without triggering start_response
                resp.headers = headers
                #################

                result = biom.getvoiceStatus('SECAS_' + str(cookie['username'].value), cookie['channel'].value,
                                             cookie['type'].value)
                if (result[0] == True):
                    template_args['username_used'] = 4
                    template_args['username_title_value'] = username
                    template_args['question_title_value'] = question
                    mako_template = LOOKUP.get_template('registration.mako')
                    resp.message = mako_template.render(**template_args).decode("utf-8")
                else:
                    try:
                        totp_secret = UserManager.create_user(username, password, question, answer)
                    except RuntimeError:
                        resp = BadRequest("Username already in use")
                        totp_secret = 0
                    try:
                        otpauth_link = 'otpauth://totp/%s?secret=%s' % (username, totp_secret)
                        qr_code = pyqrcode.create(otpauth_link)
                        template_args = {
                            'username': username,
                            'totp_secret': totp_secret,
                            'qr_blob': qr_code.png_as_base64_str(scale=5),
                            'home_uri': url
                        }
                    except RuntimeError:
                        resp = BadRequest("There was a problem generating your TOTP")
                    mako_template = LOOKUP.get_template('user_registered.mako')
                    resp.message = mako_template.render(**template_args).decode("utf-8")







    return resp(environ, start_response)


def getvoiceStatus(environ, start_response):
    resp = Response("Voice files added succesfully")

    template_args = {
        "title": "Biometric registration",
        "file_label": "Voiceprint recording:",
        "button_label": "Submit voiceprint (Check before submit it):",
        "username": environ['QUERY_STRING'].split('=')[1],
        "submit_text": "Submit",
        "action": environ['REQUEST_URI'],
        "nsuccess": 0,
        "nfailures": 0,
        "nalert": 0
    }
    userData = [template_args['username'], 'English', 'Mixed', 'my voice is my password']
    biom = BiometricEnrollment(userData)


    ################
    # Cookie break #
    cookie = SimpleCookie()
    cookie['username'] = template_args['username']
    cookie['channel'] = 'English'
    cookie['type'] = 'Mixed'
    cookie['utterText'] = 'my voice is my password'
    cookieheaders = ('Set-Cookie', cookie['username'].OutputString())
    headers = [cookieheaders, ('content-type', 'text/html')]
    # add headers without triggering start_response
    resp.headers = headers
    #################

    result = biom.getvoiceStatus('SECAS_' + str(cookie['username'].value), cookie['channel'].value,
                                        cookie['type'].value)

    return resp(environ, start_response)


def voiceRegistration(environ, start_response):
    global username_used1
    resp = Response("Voice files added succesfully")
    result = False, False
    template_args = {
        "title": "Biometric registration",
        "file_label": "Voiceprint recording:",
        "button_label": "Submit voiceprint (Check before submit it):",
        "username": environ['QUERY_STRING'].split('=')[1],
        "submit_text": "Submit",
        "action": environ['REQUEST_URI'],
        "nsuccess": 0,
        "nfailures": 0,
        "nalert": 0
    }
    userData = [template_args['username'], 'English', 'Mixed', 'my voice is my password']
    # GET should start the enrollment method
    if (environ['REQUEST_METHOD'] == 'GET'):
        biom = BiometricEnrollment(userData)

        ################
        # Cookie break #
        cookie = SimpleCookie()
        cookie['username'] = template_args['username']
        cookie['channel'] = 'English'
        cookie['type'] = 'Mixed'
        cookie['utterText'] = 'my voice is my password'
        cookieheaders = ('Set-Cookie', cookie['username'].OutputString())
        headers = [cookieheaders, ('content-type', 'text/html')]
        # add headers without triggering start_response
        resp.headers = headers
        #################

        if UserManager.verify_username(template_args['username']):
            template_args['nfailures'] = 4
            mako_template = LOOKUP.get_template('biom_enroll.mako')
            resp.message = mako_template.render(**template_args).decode("utf-8")
            resp.headers = headers
            username_used1 = True

            #################
            result = biom.enrollVoicePrintBegin('SECAS_' + str(cookie['username'].value), cookie['channel'].value,
                                                cookie['type'].value)
            ###################
        else:
            username_used1 = False
            result = biom.enrollVoicePrintBegin('SECAS_' + str(cookie['username'].value), cookie['channel'].value,
                                                cookie['type'].value)


            # POST should keep going the enrollment method until
    # either the voiceprint is rejected or validated
    if (environ['REQUEST_METHOD'] == 'POST'):

        registration_info = urllib_parse_qs(environ['wsgi.input'].read().decode('utf-8'))
        nsuccess = int(registration_info['nsuccess'][0])
        nfailures = int(registration_info['nfailures'][0])
        orig_pkg = registration_info['thefile2'][0]

        biom = BiometricEnrollment(userData, nsuccess, nfailures)

        ################
        # Cookie break #
        if 'HTTP_COOKIE' in environ:
            cookie = SimpleCookie(environ['HTTP_COOKIE'])
            if 'username' in cookie:
                # handle the cookie value
                username = cookie['username'].value
                utterText = 'my voice is my password'

                cookie['status'] = 'unfinished'
                cookieheaders = ('Set-Cookie', cookie['status'].OutputString())
                headers = [cookieheaders, ('content-type', 'text/html')]
        #################

        # wav=pickupVoicePrint()
        # orig_pkg = _dict["thefile"][0]
        orig_audio = base64.b64decode(orig_pkg)
        print(orig_audio)
        head, data = orig_audio.decode('ascii').split(',')
        print(data)
        data = base64.b64decode(data)
        print(data)
        # Verify Biometric Authentication
        try:
            # Do verification
            with open('audiofile.wav', 'wb') as f:
                soundfile = f.write(data)
            with open('audiofile.wav', 'rb') as soundfile:
                print(soundfile.read())
                # num_frames = soundfile.getnframes()
                # str_data = soundfile.readframes(num_frames)
                # soundfile.close()
                result = biom.enrollVoicePrintData('SECAS_' + str(cookie['username'].value), utterText,soundfile.read())
        except:
            raise

        if (result[0] == True):
            template_args["nsuccess"] = nsuccess + 1
            template_args["nfailures"] = nfailures
            template_args["nalert"] = 0

        else:
            template_args["nfailures"] = nfailures + 1
            template_args["nsuccess"] = nsuccess
            template_args["nalert"] = 1

    if (not username_used1):
        if ((result[0] == False) and (result[1] == False)):
            mako_template = LOOKUP.get_template('biom_enroll.mako')
            resp.message = mako_template.render(**template_args).decode("utf-8")
            resp.headers = headers
        elif ((result[0] == True) and (result[1] == False)):
            mako_template = LOOKUP.get_template('biom_enroll.mako')
            resp.message = mako_template.render(**template_args).decode("utf-8")
            resp.headers = headers
        elif ((result[0] == False) and (result[1] == True)):
            mako_template = LOOKUP.get_template('biom_enroll.mako')
            resp.message = mako_template.render(**template_args).decode("utf-8")
            resp.headers = headers
            template_args['nfailures'] = 3
            template_args["nalert"] = 0
        elif ((result[0] == True) and (result[1] == True)):
            template_args['nsuccess'] = 3
            mako_template = LOOKUP.get_template('biom_enroll.mako')
            resp.message = mako_template.render(**template_args).decode("utf-8")
            resp.headers = headers
            if 'HTTP_COOKIE' in environ:
                cookie = SimpleCookie(environ['HTTP_COOKIE'])
                if 'username' in cookie:
                    # handle the cookie value
                    username = cookie['username'].value
                    utterText = 'my voice is my password'
                    cookie['status'] = 'ok'
                    cookieheaders = ('Set-Cookie', cookie['status'].OutputString())
                    headers = [cookieheaders, ('content-type', 'text/html')]
        else:
            ################
            # Cookie break #
            if 'HTTP_COOKIE' in environ:
                cookie = SimpleCookie(environ['HTTP_COOKIE'])
                if 'username' in cookie:
                    # handle the cookie value
                    username = cookie['username'].value
                    utterText = 'my voice is my password'
                    cookie['status'] = 'ok'
                    cookieheaders = ('Set-Cookie', cookie['status'].OutputString())
                    headers = [cookieheaders, ('content-type', 'text/html')]
        #################

    return resp(environ, start_response)


def func_logout(environ, start_response):
    session = environ['beaker.session']
    # session.invalidate()
    session.clear()
    resp = Response("Logout OK")
    return resp(environ, start_response)


# ----------------------------------------------------------------------------
from oic.oic.provider import AuthorizationEndpoint
from oic.oic.provider import TokenEndpoint
from oic.oic.provider import UserinfoEndpoint
from oic.oic.provider import RegistrationEndpoint

# ----------------------------------------------------------------------------

ROOT = './'

LOOKUP = TemplateLookup(directories=[ROOT + 'templates', ROOT + 'htdocs'],
                        module_directory=ROOT + 'modules',
                        input_encoding='utf-8', output_encoding='utf-8')


# ----------------------------------------------------------------------------


class Application(object):
    def __init__(self, oas, urls):
        self.oas = oas

        self.endpoints = [
            AuthorizationEndpoint(self.authorization),
            TokenEndpoint(self.token),
            UserinfoEndpoint(self.userinfo),
            RegistrationEndpoint(self.registration),
            EndSessionEndpoint(self.endsession),
        ]

        self.oas.endpoints = self.endpoints
        self.urls = urls
        self.urls.extend([
            (r'^.well-known/openid-configuration', self.op_info),
            (r'^.well-known/simple-web-discovery', self.swd_info),
            (r'^.well-known/host-meta.json', self.meta_info),
            (r'^.well-known/webfinger', self.webfinger),
            #    (r'^.well-known/webfinger', webfinger),
            (r'.+\.css$', self.css),
            (r'safe', self.safe),
            (r'^keyrollover', key_rollover),
            (r'^clearkeys', clear_keys),
            (r'^check_session', check_session_iframe),
            #    (r'tracelog', trace_log),
            (r'^logout', func_logout),
            (r'^biom_enroll', voiceRegistration),
            (r'^register_user', register_user),
            (r'^recover_user', pwd_recovery),
            (r'^modify_user', modifier),
            (r'^test', test)
        ])

        self.add_endpoints(self.endpoints)

    def add_endpoints(self, extra):
        for endp in extra:
            self.urls.append(("^%s" % endp.etype, endp.func))

    # noinspection PyUnusedLocal
    def safe(self, environ, start_response):
        _srv = self.oas.server
        _log_info = self.oas.logger.info

        _log_info("- safe -")
        # _log_info("env: %s" % environ)
        # _log_info("handle: %s" % (handle,))

        try:
            authz = environ["HTTP_AUTHORIZATION"]
            (typ, code) = authz.split(" ")
            assert typ == "Bearer"
        except KeyError:
            resp = BadRequest("Missing authorization information")
            return resp(environ, start_response)

        try:
            _sinfo = _srv.sdb[code]
        except KeyError:
            resp = Unauthorized("Not authorized")
            return resp(environ, start_response)

        info = "'%s' secrets" % _sinfo["sub"]
        resp = Response(info)
        return resp(environ, start_response)

    # noinspection PyUnusedLocal
    def css(self, environ, start_response):
        try:
            info = open(environ["PATH_INFO"]).read()
            resp = Response(info)
        except (OSError, IOError):
            resp = NotFound(environ["PATH_INFO"])

        return resp(environ, start_response)

    # ----------------------------------------------------------------------------

    # noinspection PyUnusedLocal
    def token(self, environ, start_response):
        return wsgi_wrapper(environ, start_response, self.oas.token_endpoint,
                            logger=logger)

    # noinspection PyUnusedLocal
    def authorization(self, environ, start_response):
        return wsgi_wrapper(environ, start_response,
                            self.oas.authorization_endpoint, logger=logger)

    # noinspection PyUnusedLocal
    def userinfo(self, environ, start_response):
        return wsgi_wrapper(environ, start_response, self.oas.userinfo_endpoint,
                            logger=logger)

    # noinspection PyUnusedLocal
    def op_info(self, environ, start_response):
        return wsgi_wrapper(environ, start_response,
                            self.oas.providerinfo_endpoint, logger=logger)

    # noinspection PyUnusedLocal
    def registration(self, environ, start_response):
        if environ["REQUEST_METHOD"] == "POST":
            return wsgi_wrapper(environ, start_response,
                                self.oas.registration_endpoint,
                                logger=logger)
        elif environ["REQUEST_METHOD"] == "GET":
            return wsgi_wrapper(environ, start_response,
                                self.oas.read_registration, logger=logger)
        else:
            resp = ServiceError("Method not supported")
            return resp(environ, start_response)

    # noinspection PyUnusedLocal
    def check_id(self, environ, start_response):
        return wsgi_wrapper(environ, start_response, self.oas.check_id_endpoint,
                            logger=logger)

    # noinspection PyUnusedLocal
    def swd_info(self, environ, start_response):
        return wsgi_wrapper(environ, start_response, self.oas.discovery_endpoint,
                            logger=logger)

    # noinspection PyUnusedLocal
    def trace_log(self, environ, start_response):
        return wsgi_wrapper(environ, start_response, self.oas.tracelog_endpoint,
                            logger=logger)

    # noinspection PyUnusedLocal
    def endsession(self, environ, start_response):
        return wsgi_wrapper(environ, start_response,
                            self.oas.endsession_endpoint, logger=logger)

    # noinspection PyUnusedLocal
    def meta_info(self, environ, start_response):
        """
        Returns something like this::

             {"links":[
                 {
                    "rel":"http://openid.net/specs/connect/1.0/issuer",
                    "href":"https://openidconnect.info/"
                 }
             ]}

        """
        pass

    def webfinger(self, environ, start_response):
        query = parse_qs(environ["QUERY_STRING"])
        try:
            assert query["rel"] == [OIC_ISSUER]
            resource = query["resource"][0]
        except KeyError:
            resp = BadRequest("Missing parameter in request")
        else:
            wf = WebFinger()
            resp = Response(wf.response(subject=resource,
                                        base=self.oas.baseurl))
        return resp(environ, start_response)

    def application(self, environ, start_response):
        """
        The main WSGI application. Dispatch the current request to
        the functions from above and store the regular expression
        captures in the WSGI environment as  `oic.url_args` so that
        the functions from above can access the url placeholders.

        If nothing matches call the `not_found` function.

        :param environ: The HTTP application environment
        :param start_response: The application to run when the handling of the
            request is done
        :return: The response as a list of lines
        """
        # user = environ.get("REMOTE_USER", "")
        path = environ.get('PATH_INFO', '').lstrip('/')

        if path == "robots.txt":
            return static(self, environ, start_response, "static/robots.txt")

        environ["oic.oas"] = self.oas

        logger.info('PATH: "{}"'.format(path))

        if path.startswith("static/"):
            return static(self, environ, start_response, path)

        for regex, callback in self.urls:
            match = re.search(regex, path)
            if match is not None:
                try:
                    environ['oic.url_args'] = match.groups()[0]
                except IndexError:
                    environ['oic.url_args'] = path
                logger.info("callback: %s" % callback)
                try:
                    return callback(environ, start_response)
                except Exception as err:
                    print("%s" % err)
                    message = traceback.format_exception(*sys.exc_info())
                    print(message)
                    logger.exception("%s" % err)
                    resp = ServiceError("%s" % err)

                    return resp(environ, start_response)

        LOGGER.debug("unknown side: %s" % path)
        resp = NotFound("Couldn't find the side you asked for!")
        return resp(environ, start_response)


# ----------------------------------------------------------------------------
def generate_user_password_authn():
    # end_points = config.USER_PASSWORD_END_POINTS
    end_points = config.AUTHENTICATION["UserPassword"]["END_POINTS"]
    full_end_point_paths = ["%s%s" % (_issuer, ep) for ep in end_points]
    user_password_authn = UserPassBcryptMako(
        None, "login.mako", LOOKUP, lambda user_id: UserManager._read_password(user_id),
        "%sauthorization" % _issuer, None, full_end_point_paths)
    # {'recover_uri':'recover_user'}
    PASSWORD_END_POINT_INDEX = 0
    password_end_point = config.AUTHENTICATION["UserPassword"]["END_POINTS"][PASSWORD_END_POINT_INDEX]

    return user_password_authn, password_end_point,


def generate_totp_authn():
    end_points = config.AUTHENTICATION["TOTP"]["END_POINTS"]

    # end_points = config.TOTP_END_POINTS
    # full_end_point_paths = []
    # for ep in end_points:
    #     full_end_point_paths.append("%s%s" % (_issuer, ep))

    full_end_point_paths = [
        "%s%s" % (_issuer, ep) for ep in end_points]
    totp_login_authn = TOTPAuthn(None, 'totp_form.mako', LOOKUP, lambda user_id: UserManager._read_totp(user_id),
                                 "%s/authorization" % _issuer, None, full_end_point_paths)

    TOTP_POINT_INDEX = 0

    # totp_endpoint = config.TOTP_END_POINTS[TOTP_POINT_INDEX]
    totp_endpoint = config.AUTHENTICATION["TOTP"]["END_POINTS"][TOTP_POINT_INDEX]

    return totp_login_authn, totp_endpoint


def generate_biometric_authn():
    end_points = config.AUTHENTICATION["VoiceVerification"]["END_POINTS"]
    # end_points = config.BIOM_END_POINTS
    # TODO userData must contain the data required for the authentication
    # TODO userData content is: [userCode,contentCode,channelCode,utteranceText]. All strings
    # TODO If utteranceText is '', authentication just won't try to match the expected phrase with it
    # userData = ['SECAS_','English','Mixed','my voice is my password']
    full_end_point_paths = [
        "%s%s" % (_issuer, ep) for ep in end_points]
    biom_login_authn = BiometricAuthn(None, 'biom_form.mako', LOOKUP,
                                      lambda user_id: ['SECAS_' + user_id, 'English', 'Mixed',
                                                       'my voice is my password'],
                                      "%s/authorization" % _issuer, None, full_end_point_paths)

    BIOM_POINT_INDEX = 0

    # biom_endpoint = config.BIOM_END_POINTS[BIOM_POINT_INDEX]
    biom_endpoint = config.AUTHENTICATION["VoiceVerification"]["END_POINTS"][BIOM_POINT_INDEX]
    return biom_login_authn, biom_endpoint

def secret(seed, sid):
    msg = "{}{:.6f}{}".format(time.time(), random.random(), sid).encode("utf-8")
    csum = hmac.new(seed, msg, hashlib.sha224)
    return csum.hexdigest()


def manual_client(self):

    # create new id och secret
    client_id = rndstr(12)
    while client_id in self.cdb:
        client_id = rndstr(12)

    client_secret = secret(self.seed, client_id)

    _rat = rndstr(32)
    reg_enp = "https://localhost:8092/registration"

    self.cdb[client_id] = {
        "client_id": client_id,
        "client_secret": client_secret,
        "registration_access_token": _rat,
        "registration_client_uri": "%s?client_id=%s" % (reg_enp, client_id),
        "client_secret_expires_at": self.client_secret_expiration_time(),
        "client_id_issued_at": utc_time_sans_frac(),
        "client_salt": rndstr(8)
    }

    self.cdb[_rat] = client_id
    _cinfo = {}
    _cinfo["application_type"] = "web"
    _cinfo["contacts"] = "ops@example.com"
    _cinfo["redirect_uris"] = "http://localhost:4200/home"
    _cinfo["response_types"] = "code"
    _cinfo["post_logout_redirect_uris"] = "http://localhost:4200/home"


    # Add the client_secret as a symmetric key to the keyjar
    if client_secret:
        self.keyjar.add_symmetric(client_id, str(client_secret))

    self.cdb[client_id] = _cinfo

    try:
        self.cdb.sync()
    except AttributeError:  # Not all databases can be sync'ed
        pass

    logger.info("user register manually:")


# ----------------------------------------------------------------------------

if __name__ == '__main__':
    import argparse
    import importlib

    from cherrypy import wsgiserver
    from cherrypy.wsgiserver.ssl_builtin import BuiltinSSLAdapter

    from oic.utils.sdb import SessionDB

    parser = argparse.ArgumentParser()
    parser.add_argument('-v', dest='verbose', action='store_true')
    parser.add_argument('-d', dest='debug', action='store_true')
    parser.add_argument('-p', dest='port', default=80, type=int)
    parser.add_argument('-t', dest='tls', action='store_true')
    parser.add_argument('-k', dest='insecure', action='store_true')
    parser.add_argument(
        '-c', dest='capabilities',
        help="A file containing a JSON representation of the capabilities")
    parser.add_argument('-i', dest='issuer', help="issuer id of the OP",
                        nargs=1)
    parser.add_argument(dest="config")
    args = parser.parse_args()

    # Client data base
    cdb = shelve_wrapper.open("client_db")

    logger.info("Known client_ids: {}".format([k for k in cdb.keys()]))
    sys.path.insert(0, ".")
    config = importlib.import_module(args.config)

    if args.issuer:
        _issuer = args.issuer[0]
    else:
        if args.port not in [80, 443]:
            _issuer = config.ISSUER + ':{}'.format(args.port)
        else:
            _issuer = config.ISSUER

    if _issuer[-1] != '/':
        _issuer += '/'

    config.SERVICE_URL = config.SERVICE_URL.format(issuer=_issuer)

    ac = AuthnBroker()

    _urls = []
    password_authn, password_endpoint = generate_user_password_authn()

    totp_authn, totp_endpoint = generate_totp_authn()

    biom_authn, biom_endpoint = generate_biometric_authn()

    auth_modules = [(password_authn, r'^' + password_endpoint),
                    (totp_authn, r'^' + totp_endpoint),
                    (biom_authn, r'^' + biom_endpoint)
                    ]

    authn = setup_multi_auth(ac, _urls, auth_modules)

    if authn is not None:
        ac.add(config.AUTHENTICATION["MultiAuthn"]["ACR"], authn,
               config.AUTHENTICATION["MultiAuthn"]["WEIGHT"],
               "")
    # ----------------------------------------------------------------------------
    # dealing with authorization
    authz = AuthzHandling()

    kwargs = {
        "template_lookup": LOOKUP,
        "template": {"form_post": "form_response.mako"},
        # "template_args": {"form_post": {"action": "form_post"}}
    }

    # Should I care about verifying the certificates used by other entities
    if args.insecure:
        kwargs["verify_ssl"] = False
    else:
        kwargs["verify_ssl"] = True

    if args.capabilities:
        kwargs["capabilities"] = json.loads(open(args.capabilities).read())
    else:
        pass

    OAS = Provider(_issuer, SessionDB(_issuer), cdb, ac, None,
                   authz, verify_client, config.SYM_KEY, **kwargs)
    OAS.baseurl = _issuer

    for authn in ac:
        authn.srv = OAS

    # OAS.userinfo = UserManager(config.USERDB)
    OAS.userinfo = UserManager('users.json')

    try:
        OAS.cookie_ttl = config.COOKIETTL
    except AttributeError:
        pass

    try:
        OAS.cookie_name = config.COOKIENAME
    except AttributeError:
        pass

    # print URLS
    if args.debug:
        OAS.debug = True

    # All endpoints the OpenID Connect Provider should answer on
    # add_endpoints(ENDPOINTS)

    try:
        jwks = keyjar_init(OAS, config.keys, kid_template="op%d")
    except Exception as err:
        LOGGER.error("Key setup failed: %s" % err)
        OAS.key_setup("static", sig={"format": "jwk", "alg": "rsa"})
    else:
        jwks_file_name = JWKS_FILE_NAME
        f = open(jwks_file_name, "w")

        for key in jwks["keys"]:
            for k in key.keys():
                key[k] = as_unicode(key[k])

        f.write(json.dumps(jwks))
        f.close()
        OAS.jwks_uri = "%s%s" % (OAS.baseurl, jwks_file_name)

    for b in OAS.keyjar[""]:
        LOGGER.info("OC3 server keys: %s" % b)

    _app = Application(OAS, _urls)

    # Setup the web server
    SRV = wsgiserver.CherryPyWSGIServer(('0.0.0.0', args.port),
                                        _app.application)

    https = ""
    if args.tls:
        https = "using TLS"
        # SRV.ssl_adapter = ssl_pyopenssl.pyOpenSSLAdapter(
        #     config.SERVER_CERT, config.SERVER_KEY, config.CERT_CHAIN)
        SRV.ssl_adapter = BuiltinSSLAdapter(config.SERVER_CERT,
                                            config.SERVER_KEY)

    LOGGER.info(
        "OC server started (iss={}, port={})".format(_issuer, args.port))
    print("OC server started (iss={}, port={}) {}".format(_issuer, args.port,
                                                          https))

    #manual_client()
    try:
        SRV.start()
    except KeyboardInterrupt:
        SRV.stop()