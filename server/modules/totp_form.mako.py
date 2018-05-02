# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1525278327.839504
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
        url = context.get('url', UNDEFINED)
        form_action = context.get('form_action', UNDEFINED)
        query = context.get('query', UNDEFINED)
        title = context.get('title', UNDEFINED)
        acr = context.get('acr', UNDEFINED)
        username = context.get('username', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="col-md-4 col-md-offset-4 header">\n    <h1>')
        __M_writer(str(title))
        __M_writer('</h1>\n</div>\n\n<div class="col-md-4 col-md-offset-4 login_form top_form" class="block">\n    <form action="')
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
        __M_writer('"><strong>BACK</strong></a><br>\n</div>\n\n')
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
{"source_encoding": "utf-8", "uri": "totp_form.mako", "filename": "htdocs/totp_form.mako", "line_map": {"68": 62, "38": 1, "39": 4, "40": 4, "41": 8, "42": 8, "43": 9, "44": 9, "45": 10, "46": 10, "47": 11, "48": 11, "49": 15, "50": 15, "51": 18, "52": 18, "58": 21, "27": 0, "62": 21}}
__M_END_METADATA
"""
