# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1486573190.0557814
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
        form_action = context.get('form_action', UNDEFINED)
        title = context.get('title', UNDEFINED)
        acr = context.get('acr', UNDEFINED)
        username = context.get('username', UNDEFINED)
        query = context.get('query', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="header">\n    <h1>')
        __M_writer(str(title))
        __M_writer('</h1>\n</div>\n\n<div class="login_form" class="block">\n    <form action="')
        __M_writer(str(form_action))
        __M_writer('">\n        <input type="hidden" name="query" value="')
        __M_writer(str(query))
        __M_writer('"/>\n        <input type="hidden" name="acr_values" value="')
        __M_writer(str(acr))
        __M_writer('"/>\n        <input type="hidden" name="username" value="')
        __M_writer(str(username))
        __M_writer('"/>\n        <label for="totp">TOTP (Time-based One Time Password</label>\n        <input name="totp" type="text"></br>\n        <input type="submit"><br/>\n    </form>\n</div>\n\n')
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
{"filename": "htdocs/totp_form.mako", "source_encoding": "utf-8", "uri": "totp_form.mako", "line_map": {"64": 58, "37": 1, "38": 4, "39": 4, "40": 8, "41": 8, "42": 9, "43": 9, "44": 10, "45": 10, "46": 11, "47": 11, "48": 24, "54": 18, "58": 18, "27": 0}}
__M_END_METADATA
"""
