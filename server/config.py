# -*- coding: utf-8 -*-

keys = [
    {"type": "RSA", "key": "cp_keys/key.pem", "use": ["enc", "sig"]},
    {"type": "EC", "crv": "P-256", "use": ["sig"]},
    {"type": "EC", "crv": "P-256", "use": ["enc"]}
]

ISSUER='https://localhost'
SERVICE_URL = "{issuer}/verify"

USER_PASSWORD_END_POINTS = ["user_password", "multi_user_password_saml_verify",
                            "multi_user_password_js_verify"]
SAML_END_POINTS = ['saml', "multi_saml_pass"]
JAVASCRIPT_END_POINTS = ['javascript_login', "multi_javascript_login"]
TOTP_END_POINTS = ["totp_login"]
BIOM_END_POINTS = ["biom_login"]

AUTHENTICATION = {
    "SAML" : {"ACR": "SAML", "WEIGHT": 1, "END_POINTS": SAML_END_POINTS},
    "UserPassword" : {"ACR": "PASSWORD", "WEIGHT": 2,
                      "END_POINTS": USER_PASSWORD_END_POINTS},
    "TOTP" : {"ACR": "TOTP", "WEIGHT": 2,
                      "END_POINTS": TOTP_END_POINTS},
    "VoiceVerification" : {"ACR": "BIOMETRIC", "WEIGHT": 2,
                      "END_POINTS": BIOM_END_POINTS},
    "SamlPass": {"ACR": "SAML_PASS", "WEIGHT": 3},
    "JavascriptLogin": {"ACR": "JAVASCRIPT_LOGIN", "WEIGHT": 4,
                        "END_POINTS": JAVASCRIPT_END_POINTS},
    "JavascriptPass": {"ACR": "JAVASCRIPT_PASS", "WEIGHT": 5},
    "MultiAuthn": {"ACR": "MULTI_AUTHN", "WEIGHT": 5},

}

COOKIENAME= 'pyoic'
COOKIETTL = 4*60 # 4 hours
SYM_KEY = "SoLittleTime,Got"

SERVER_CERT = "certs/server.crt"
SERVER_KEY = "certs/server.key"
#CERT_CHAIN="certs/chain.pem"
CERT_CHAIN = None

# =======  SAML ==============
#User information is collected with SAML
#USERINFO = "SAML"
#User information is collected with a SAML attribute authority
#USERINFO = "AA"
#Name of the Service Provider configuration file.
SP_CONFIG="sp_conf"
#Dictionary with userinformation for the SAML users. Must be empty.
SAML = {}

# =======  SIMPLE DATABASE ==============

USERINFO = "SIMPLE"
