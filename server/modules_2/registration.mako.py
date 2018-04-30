# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1506528989.2326076
_enable_loop = True
_template_filename = 'htdocs/registration.mako'
_template_uri = 'registration.mako'
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
        question_title = context.get('question_title', UNDEFINED)
        submit_text = context.get('submit_text', UNDEFINED)
        audio_title = context.get('audio_title', UNDEFINED)
        password_title = context.get('password_title', UNDEFINED)
        audio_button = context.get('audio_button', UNDEFINED)
        answer_title = context.get('answer_title', UNDEFINED)
        username_title = context.get('username_title', UNDEFINED)
        title = context.get('title', UNDEFINED)
        password_title2 = context.get('password_title2', UNDEFINED)
        answer_title2 = context.get('answer_title2', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="header">\n    <h1>')
        __M_writer(str(title))
        __M_writer('</h1>\n</div>\n<div class="registration_form" class="block">\n    <form method="post" class="login form">\n        <table>\n            <tr>\n                <td>')
        __M_writer(str(username_title))
        __M_writer('</td>\n                <td><input type="text" name="username" id="username" /></td>\n            </tr>\n            <tr>\n                <td>')
        __M_writer(str(password_title))
        __M_writer('</td>\n                <td><input type="password" name="password"/></td>\n            </tr>\n            <tr>\n                <td>')
        __M_writer(str(password_title2))
        __M_writer('</td>\n                <td><input type="password" name="password2"/></td>\n            </tr>\n            <tr>\n                <td>')
        __M_writer(str(question_title))
        __M_writer('</td>\n                <td><input type="text" name="question"/></td>\n            </tr>\n            <tr>\n                <td>')
        __M_writer(str(answer_title))
        __M_writer('</td>\n                <td><input type="password" name="answer"/></td>\n            </tr>\n            <tr>\n                <td>')
        __M_writer(str(answer_title2))
        __M_writer('</td>\n                <td><input type="password" name="answer2"/></td>\n            </tr>\n            <tr>\n                <td>')
        __M_writer(str(audio_title))
        __M_writer('</td>\n                <td><input type="button" name="audioButton" id="audioButton"\n                        value=')
        __M_writer(str(audio_button))
        __M_writer('/></td>\n            </tr>\n            <tr>\n                <td><input type="submit" name="form.commit"\n                        value="')
        __M_writer(str(submit_text))
        __M_writer('"/></td>\n            </tr>\n        </table>\n    </form>\n</div>\n\n')
        __M_writer('\n<script>\n\n  var audioButton = document.getElementById(\'audioButton\');\n\n  var successes = 0;\n\n  audioButton.addEventListener(\'click\', function() {\n        var username = document.getElementById(\'username\').value;\n\n        if (username == "") {\n            alert("Username must be filled out");\n            console.log("Username must be filled out");\n            return false;\n        }else{\n\n            if (successes>=3){\n                return true;\n            }\n\n            var url = "biom_enroll?id=" + username;\n\n            var childWin = window.open(url, "Voiceprint enrollment", "width=400,height=250");\n            return false;\n        }\n  });\n\n  function shenanigans(val1){\n')
        __M_writer('      if (val1) {\n          successes+=1;\n          console.log(successes);\n      }\n  }\n</script>')
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
{"source_encoding": "utf-8", "uri": "registration.mako", "line_map": {"64": 81, "70": 46, "74": 46, "80": 74, "27": 0, "42": 1, "43": 4, "44": 4, "45": 10, "46": 10, "47": 14, "48": 14, "49": 18, "50": 18, "51": 22, "52": 22, "53": 26, "54": 26, "55": 30, "56": 30, "57": 34, "58": 34, "59": 36, "60": 36, "61": 40, "62": 40, "63": 52}, "filename": "htdocs/registration.mako"}
__M_END_METADATA
"""
