# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1525278082.533978
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
        logo_uri = context.get('logo_uri', UNDEFINED)
        submit_text = context.get('submit_text', UNDEFINED)
        tos_uri = context.get('tos_uri', UNDEFINED)
        password = context.get('password', UNDEFINED)
        recover_uri = context.get('recover_uri', UNDEFINED)
        passwd_title = context.get('passwd_title', UNDEFINED)
        login = context.get('login', UNDEFINED)
        url = context.get('url', UNDEFINED)
        policy_uri = context.get('policy_uri', UNDEFINED)
        login_title = context.get('login_title', UNDEFINED)
        query = context.get('query', UNDEFINED)
        title = context.get('title', UNDEFINED)
        register_uri = context.get('register_uri', UNDEFINED)
        acr = context.get('acr', UNDEFINED)
        action = context.get('action', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<div class="col-md-4 col-md-offset-4 header">\n    <h1><a href="/">')
        __M_writer(str(title))
        __M_writer('</a></h1>\n</div>\n<div class="col-md-4 col-md-offset-4 login_form top_form" class="block">\n    <form action="')
        __M_writer(str(action))
        __M_writer('" method="post" class="login form">\n        <input type="hidden" name="query" value="')
        __M_writer(str(query))
        __M_writer('"/>\n        <input type="hidden" name="acr_values" value="')
        __M_writer(str(acr))
        __M_writer('"/>\n')
        __M_writer('        <table>\n            <tr>\n                <td>')
        __M_writer(str(login_title))
        __M_writer('</td>\n                <td><input class="form-control" type="text" name="login" value="')
        __M_writer(str(login))
        __M_writer('"/></td>\n            </tr>\n            <tr>\n                <td>')
        __M_writer(str(passwd_title))
        __M_writer('</td>\n                <td><input class="form-control" type="password" name="password"\n                value="')
        __M_writer(str(password))
        __M_writer('"/></td>\n            </tr>\n        </table>\n        <input class="form-control" type="hidden" name="url" id="url" value="')
        __M_writer(str(url))
        __M_writer('"/>\n        <div><input class="btn btn-primary btn-lg btn-block top_form" type="submit" name="form.commit"\n                        value="')
        __M_writer(str(submit_text))
        __M_writer('"/></div>\n\n    </form>\n')
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
        __M_writer('\n\n<script>\n    var URLactual = window.location;\n    //document.getElementById("url").value = URLactual;\n    //console.log("URLLLLLLLLLLLLLLLLLLLL: "+ document.getElementById(\'url\').value);\n</script>')
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
{"source_encoding": "utf-8", "uri": "login.mako", "filename": "htdocs/login.mako", "line_map": {"27": 0, "47": 1, "48": 3, "49": 3, "50": 6, "51": 6, "52": 7, "53": 7, "54": 8, "55": 8, "56": 10, "57": 12, "58": 12, "59": 13, "60": 13, "61": 16, "62": 16, "63": 18, "64": 18, "65": 21, "66": 21, "67": 23, "68": 23, "69": 26, "70": 27, "71": 27, "72": 27, "73": 29, "74": 30, "75": 30, "76": 30, "77": 32, "78": 33, "79": 33, "80": 33, "81": 42, "82": 43, "83": 43, "84": 43, "85": 45, "86": 46, "87": 46, "88": 46, "89": 48, "90": 56, "96": 50, "100": 50, "106": 100}}
__M_END_METADATA
"""
