# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1525793153.368415
_enable_loop = True
_template_filename = 'htdocs/new_pwd.mako'
_template_uri = 'new_pwd.mako'
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
        password_title = context.get('password_title', UNDEFINED)
        title = context.get('title', UNDEFINED)
        newpassword_title = context.get('newpassword_title', UNDEFINED)
        submit_text = context.get('submit_text', UNDEFINED)
        url = context.get('url', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="col-md-4 col-md-offset-4 header">\n    <h1>')
        __M_writer(str(title))
        __M_writer('</h1>\n')
        __M_writer('</div>\n<div class="col-md-4 col-md-offset-4 registration_form top_form" class="block">\n    <form method="post" class="login form" id="recoveryNewpwdForm">\n        <table>\n            <tr>\n                <td>')
        __M_writer(str(password_title))
        __M_writer('</td>\n                <td><input class="form-control" id="new_pwd" type="password" name="password"/></td>\n            </tr>\n            <tr>\n                <td>')
        __M_writer(str(newpassword_title))
        __M_writer('</td>\n                <td><input class="form-control" id="confirm_pwd" type="password" name="newpassword"/></td>\n            </tr>\n        </table>\n            <div><input class="form-control" type="hidden" name="url" value="')
        __M_writer(str(url))
        __M_writer('"/></div>\n')
        __M_writer('        <input class="btn btn-primary btn-lg btn-block top_form" type="button" onclick="checkFields()" value="New ')
        __M_writer(str(submit_text))
        __M_writer('">\n')
        __M_writer('\n    </form>\n    <a href="')
        __M_writer(str(url))
        __M_writer('"><strong>Back to login page</strong></a><br>\n</div>\n\n')
        __M_writer('\n\n<script>\n// -----------My script-----------\nfunction checkFields() {\n    var new_pwd = document.getElementById("new_pwd").value;\n    var confirm_pwd = document.getElementById("confirm_pwd").value;\n\n    if( new_pwd == "" && confirm_pwd == ""){\n         alert("Your password fields must be filled out");\n         exit(0);\n    }\n    if( new_pwd == "" ){\n         alert("You have to choose a new password");\n         exit(0);\n    }\n    if( confirm_pwd == "" ){\n         alert("You have to confirm your new password");\n         exit(0);\n    }\n    if( new_pwd != confirm_pwd){\n        alert("Fields must have the same value!");\n        exit(0);\n    }\n\n    document.getElementById("recoveryNewpwdForm").submit();\n}\n//---------------\n\n</script>')
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
{"line_map": {"59": 28, "37": 1, "38": 4, "39": 4, "40": 6, "41": 11, "42": 11, "43": 15, "44": 15, "45": 19, "46": 19, "47": 21, "48": 21, "49": 21, "50": 23, "51": 25, "52": 25, "53": 34, "27": 0, "69": 63, "63": 28}, "uri": "new_pwd.mako", "filename": "htdocs/new_pwd.mako", "source_encoding": "utf-8"}
__M_END_METADATA
"""
