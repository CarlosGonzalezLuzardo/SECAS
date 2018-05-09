# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1525793067.7521348
_enable_loop = True
_template_filename = 'htdocs/login.mako'
_template_uri = 'login.mako'
_source_encoding = 'utf-8'
_exports = ['add_js']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'root.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        action = context.get('action', UNDEFINED)
        tos_uri = context.get('tos_uri', UNDEFINED)
        login_title = context.get('login_title', UNDEFINED)
        title = context.get('title', UNDEFINED)
        register_uri = context.get('register_uri', UNDEFINED)
        submit_text = context.get('submit_text', UNDEFINED)
        login = context.get('login', UNDEFINED)
        query = context.get('query', UNDEFINED)
        recover_uri = context.get('recover_uri', UNDEFINED)
        policy_uri = context.get('policy_uri', UNDEFINED)
        url = context.get('url', UNDEFINED)
        passwd_title = context.get('passwd_title', UNDEFINED)
        logo_uri = context.get('logo_uri', UNDEFINED)
        acr = context.get('acr', UNDEFINED)
        password = context.get('password', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<div class="col-md-4 col-md-offset-4 header">\n')
        __M_writer('    <h1><font color="#428bca">')
        __M_writer(str(title))
        __M_writer('</font></h1>\n</div>\n<div class="col-md-4 col-md-offset-4 login_form top_form" class="block">\n    <form action="')
        __M_writer(str(action))
        __M_writer('" method="post" class="login form" id="loginForm">\n        <input type="hidden" name="query" value="')
        __M_writer(str(query))
        __M_writer('"/>\n        <input type="hidden" name="acr_values" value="')
        __M_writer(str(acr))
        __M_writer('"/>\n')
        __M_writer('        <table>\n            <tr>\n                <td>')
        __M_writer(str(login_title))
        __M_writer('</td>\n                <td><input class="form-control" id="username" type="text" name="login" value="')
        __M_writer(str(login))
        __M_writer('"/></td>\n            </tr>\n            <tr>\n                <td>')
        __M_writer(str(passwd_title))
        __M_writer('</td>\n                <td><input class="form-control" id="password" type="password" name="password" value="')
        __M_writer(str(password))
        __M_writer('"/></td>\n            </tr>\n        </table>\n        <input class="form-control" type="hidden" name="url" id="url" value="')
        __M_writer(str(url))
        __M_writer('"/>\n')
        __M_writer('            <input class="btn btn-primary btn-lg btn-block top_form" type="button" onclick="checkFields()" value="New ')
        __M_writer(str(submit_text))
        __M_writer('">\n')
        __M_writer('    </form>\n')
        if logo_uri:
            __M_writer('        <img src="')
            __M_writer(str(logo_uri))
            __M_writer('" alt="Client logo">\n')
        if policy_uri:
            __M_writer('        <a href="')
            __M_writer(str(policy_uri))
            __M_writer('"><strong>Client&#39;s Policy</strong></a>\n')
        if tos_uri:
            __M_writer('        <a href="')
            __M_writer(str(tos_uri))
            __M_writer('"><strong>Client&#39;s Terms of Service</strong></a><br>\n')
        if recover_uri:
            __M_writer('        <a href="')
            __M_writer(str(recover_uri))
            __M_writer('"><strong>Forgot your password?</strong></a><br>\n')
        if register_uri:
            __M_writer('        <a href="')
            __M_writer(str(register_uri))
            __M_writer('"><strong>New user?</strong></a><br>\n')
        __M_writer('</div>\n\n')
        __M_writer('\n\n<script>\n    var URLactual = window.location;\n    //document.getElementById("url").value = URLactual;\n    //console.log("URLLLLLLLLLLLLLLLLLLLL: "+ document.getElementById(\'url\').value);\n\n// -----------My script-----------\nfunction checkFields() {\n    var username = document.getElementById("username").value;\n    var password = document.getElementById("password").value;\n    //var error = document.getElementById(\'username_used\');\n    \n    if(username == "" && password == ""){\n        alert("Username & Password must be filled out");\n        exit(0);\n    }\n    if( username == "" ){\n         alert("Username must be filled out");\n         exit(0);\n    }\n    if( password == "" ){\n        alert("Password must be filled out");\n         exit(0);\n    }\n\n\n    document.getElementById("loginForm").submit();\n}\n//---------------\n\n</script>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_add_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n    <script type="text/javascript">\n        $(document).ready(function() {\n            bookie.login.init();\n        });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"27": 0, "47": 1, "48": 4, "49": 4, "50": 4, "51": 7, "52": 7, "53": 8, "54": 8, "55": 9, "56": 9, "57": 11, "58": 13, "59": 13, "60": 14, "61": 14, "62": 17, "63": 17, "64": 18, "65": 18, "66": 21, "67": 21, "68": 23, "69": 23, "70": 23, "71": 26, "72": 27, "73": 28, "74": 28, "75": 28, "76": 30, "77": 31, "78": 31, "79": 31, "80": 33, "81": 34, "82": 34, "83": 34, "84": 43, "85": 44, "86": 44, "87": 44, "88": 46, "89": 47, "90": 47, "91": 47, "92": 49, "93": 57, "99": 51, "103": 51, "109": 103}, "uri": "login.mako", "filename": "htdocs/login.mako", "source_encoding": "utf-8"}
__M_END_METADATA
"""
