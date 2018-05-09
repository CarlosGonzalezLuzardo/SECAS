# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1525793182.8579879
_enable_loop = True
_template_filename = 'htdocs/totp_form.mako'
_template_uri = 'totp_form.mako'
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
        username = context.get('username', UNDEFINED)
        query = context.get('query', UNDEFINED)
        form_action = context.get('form_action', UNDEFINED)
        acr = context.get('acr', UNDEFINED)
        url = context.get('url', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="col-md-4 col-md-offset-4 header">\n')
        __M_writer('</div>\n\n<div class="col-md-4 col-md-offset-4 login_form top_form" class="block">\n    <form action="')
        __M_writer(str(form_action))
        __M_writer('">\n        <input type="hidden" name="query" value="')
        __M_writer(str(query))
        __M_writer('"/>\n        <input type="hidden" name="acr_values" value="')
        __M_writer(str(acr))
        __M_writer('"/>\n        <input type="hidden" name="username" value="')
        __M_writer(str(username))
        __M_writer('"/>\n        <label for="totp">TOTP (Time-based One Time Password)</label>\n        <p>Introduce your code from Google Autenticator</p>\n        <input class="form-control" name="totp" type="text"></br>\n        <input class="form-control" type="hidden" name="url" id="url" value="')
        __M_writer(str(url))
        __M_writer('"/>\n        <input class="btn btn-primary btn-lg btn-block" type="submit"><br/>\n    </form>\n    <a href="')
        __M_writer(str(url))
        __M_writer('"><strong>Back to login page</strong></a><br>\n</div>\n\n')
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
{"line_map": {"66": 60, "37": 1, "38": 5, "39": 8, "40": 8, "41": 9, "42": 9, "43": 10, "44": 10, "45": 11, "46": 11, "47": 15, "48": 15, "49": 18, "50": 18, "56": 21, "27": 0, "60": 21}, "uri": "totp_form.mako", "filename": "htdocs/totp_form.mako", "source_encoding": "utf-8"}
__M_END_METADATA
"""
