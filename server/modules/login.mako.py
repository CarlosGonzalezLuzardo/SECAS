# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1504771232.3708785
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
        login_title = context.get('login_title', UNDEFINED)
        logo_uri = context.get('logo_uri', UNDEFINED)
        recover_uri = context.get('recover_uri', UNDEFINED)
        policy_uri = context.get('policy_uri', UNDEFINED)
        acr = context.get('acr', UNDEFINED)
        action = context.get('action', UNDEFINED)
        tos_uri = context.get('tos_uri', UNDEFINED)
        submit_text = context.get('submit_text', UNDEFINED)
        query = context.get('query', UNDEFINED)
        passwd_title = context.get('passwd_title', UNDEFINED)
        password = context.get('password', UNDEFINED)
        login = context.get('login', UNDEFINED)
        register_uri = context.get('register_uri', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<div class="col-md-4 col-md-offset-4 header">\n    <h1><a href="/">')
        __M_writer(str(title))
        __M_writer('</a></h1>\n</div>\n<div class="col-md-4 col-md-offset-4 login_form top_form" class="block">\n    <form action="')
        __M_writer(str(action))
        __M_writer('" method="post" class="login form">\n        <input type="hidden" name="query" value="')
        __M_writer(str(query))
        __M_writer('"/>\n        <input type="hidden" name="acr_values" value="')
        __M_writer(str(acr))
        __M_writer('"/>\n        <table class="col-md-12">\n            <tr>\n                <td class="col-md-4">')
        __M_writer(str(login_title))
        __M_writer('</td>\n                <td class="col-md-8"><input type="text" class="form-control" name="login" value="')
        __M_writer(str(login))
        __M_writer('"/></td>\n            </tr>\n            <tr>\n                <td class="col-md-4">')
        __M_writer(str(passwd_title))
        __M_writer('</td>\n                <td class="col-md-8"><input type="password" class="form-control" name="password"\n                value="')
        __M_writer(str(password))
        __M_writer('"/></td>\n            </tr>\n            </table>\n          <div class="col-md-12"><input type="submit" class="btn btn-primary btn-lg btn-block top_form" name="form.commit"\n                        value="')
        __M_writer(str(submit_text))
        __M_writer('"/></div>\n           </form>\n')
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
        __M_writer('\n')
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
{"line_map": {"27": 0, "46": 1, "47": 3, "48": 3, "49": 6, "50": 6, "51": 7, "52": 7, "53": 8, "54": 8, "55": 11, "56": 11, "57": 12, "58": 12, "59": 15, "60": 15, "61": 17, "62": 17, "63": 22, "64": 22, "65": 26, "66": 27, "67": 27, "68": 27, "69": 29, "70": 30, "71": 30, "72": 30, "73": 32, "74": 33, "75": 33, "76": 33, "77": 35, "78": 36, "79": 36, "80": 36, "81": 38, "82": 39, "83": 39, "84": 39, "85": 41, "86": 49, "92": 43, "96": 43, "102": 96}, "source_encoding": "utf-8", "filename": "htdocs/login.mako", "uri": "login.mako"}
__M_END_METADATA
"""
