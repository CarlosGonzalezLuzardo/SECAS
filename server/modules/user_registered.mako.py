# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1525278295.948763
_enable_loop = True
_template_filename = 'htdocs/user_registered.mako'
_template_uri = 'user_registered.mako'
_source_encoding = 'utf-8'
_exports = []


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
        home_uri = context.get('home_uri', UNDEFINED)
        totp_secret = context.get('totp_secret', UNDEFINED)
        qr_blob = context.get('qr_blob', UNDEFINED)
        username = context.get('username', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<h1 class="col-md-4 col-md-offset-4 header">User registered</h1>\n<div class="col-md-8 col-md-offset-2 login_form">\n    <h2>Name</h2>\n    <div class="user-name">')
        __M_writer(str(username))
        __M_writer('</div>\n    <h2>Two-factor authentication</h2>\n    <p>Insert this code (')
        __M_writer(str(totp_secret))
        __M_writer(') or scan the following QR code in your two-factor authentication app (ie. Google Authenticator).</p>\n    <p><img src="data:image/png;base64,')
        __M_writer(str(qr_blob))
        __M_writer('"/></p>\n')
        if home_uri:
            __M_writer('        <a href="')
            __M_writer(str(home_uri))
            __M_writer('"><strong>BACK</strong></a><br>\n')
        __M_writer('</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "uri": "user_registered.mako", "filename": "htdocs/user_registered.mako", "line_map": {"36": 1, "37": 6, "38": 6, "39": 8, "40": 8, "41": 9, "42": 9, "43": 10, "44": 11, "45": 11, "46": 11, "47": 13, "53": 47, "27": 0}}
__M_END_METADATA
"""
