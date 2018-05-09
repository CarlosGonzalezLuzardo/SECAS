# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1525850602.7719872
_enable_loop = True
_template_filename = 'htdocs/recover_pwd.mako'
_template_uri = 'recover_pwd.mako'
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
        title = context.get('title', UNDEFINED)
        username_title = context.get('username_title', UNDEFINED)
        submit_text = context.get('submit_text', UNDEFINED)
        username_used = context.get('username_used', UNDEFINED)
        url = context.get('url', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<body onload="myFunction()">\n\n<div class="col-md-4 col-md-offset-4 header">\n    <h1>')
        __M_writer(str(title))
        __M_writer('</h1>\n</div>\n<div class="col-md-4 col-md-offset-4 registration_form login_form" class="block">\n    <form method="post" class="login form" id="recoveryUserForm">\n        <table>\n            <tr>\n                <td>')
        __M_writer(str(username_title))
        __M_writer('</td>\n                <td><input class="form-control" id="username" type="text" name="username"/></td>\n                <input class="form-control" id="username_used" type="number" name="username_used" value="')
        __M_writer(str(username_used))
        __M_writer('" visible/>\n            </tr>\n        </table>\n        <div><input class="form-control" type="hidden" name="url" value="')
        __M_writer(str(url))
        __M_writer('"/></div>\n')
        __M_writer('        <input class="btn btn-primary btn-lg btn-block top_form" type="button" onclick="checkFields()" value="New ')
        __M_writer(str(submit_text))
        __M_writer('">\n')
        __M_writer('                        \n    </form>\n    <a href="')
        __M_writer(str(url))
        __M_writer('"><strong>Back to login page</strong></a><br>\n</div>\n\n')
        __M_writer('\n\n<script>\n// -----------My script-----------\nfunction checkFields() {\n    var username = document.getElementById("username").value;\n    \n    if( username == "" ){\n         alert("Username must be filled out");\n         exit(0);\n    }\n\n    document.getElementById("recoveryUserForm").submit();\n}\n\n\nfunction myFunction(){\n    var failures = document.getElementById(\'username_used\');\n\n    console.log(\'myFunction\');\n    console.log(failures.value);\n    if(failures.value == 2){\n        alert("Username not found");\n    }\n  }\n//---------------\n\n</script>')
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
{"line_map": {"68": 62, "37": 1, "38": 6, "39": 6, "40": 12, "41": 12, "42": 14, "43": 14, "44": 17, "45": 17, "46": 19, "47": 19, "48": 19, "49": 21, "50": 23, "51": 23, "52": 32, "58": 26, "27": 0, "62": 26}, "source_encoding": "utf-8", "uri": "recover_pwd.mako", "filename": "htdocs/recover_pwd.mako"}
__M_END_METADATA
"""
