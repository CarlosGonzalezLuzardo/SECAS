# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1525278386.0677342
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
        answer_title2 = context.get('answer_title2', UNDEFINED)
        audio_button = context.get('audio_button', UNDEFINED)
        submit_text = context.get('submit_text', UNDEFINED)
        username_title_value = context.get('username_title_value', UNDEFINED)
        password_title2 = context.get('password_title2', UNDEFINED)
        password_title = context.get('password_title', UNDEFINED)
        question_title = context.get('question_title', UNDEFINED)
        username_used = context.get('username_used', UNDEFINED)
        question_title_value = context.get('question_title_value', UNDEFINED)
        answer_title = context.get('answer_title', UNDEFINED)
        url = context.get('url', UNDEFINED)
        audio_title = context.get('audio_title', UNDEFINED)
        title = context.get('title', UNDEFINED)
        username_title = context.get('username_title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<body onload="myFunction()">\n\n<div class="col-md-4 col-md-offset-4 header">\n    <h1>')
        __M_writer(str(title))
        __M_writer('</h1>\n</div>\n<div class="col-md-6 col-md-offset-3 registration_form top_form" class="block">\n    <form method="post" class="login form">\n        <table class="registration-table">\n            <tr>\n                <td  class="col-md-4">')
        __M_writer(str(username_title))
        __M_writer('</td>\n                <td class="col-md-8"><input class="form-control" type="text" name="username" id="username" value="')
        __M_writer(str(username_title_value))
        __M_writer('"/></td>\n            </tr>\n            <tr>\n                <td class="col-md-4">')
        __M_writer(str(password_title))
        __M_writer('</td>\n                <td class="col-md-8"><input class="form-control" type="password" name="password"/></td>\n            </tr>\n            <tr>\n                <td class="col-md-4">')
        __M_writer(str(password_title2))
        __M_writer('</td>\n                <td class="col-md-8"><input class="form-control" type="password" name="password2"/></td>\n            </tr>\n            <tr>\n                <td class="col-md-4">')
        __M_writer(str(question_title))
        __M_writer('</td>\n                <td class="col-md-8"><input class="form-control" type="text" name="question" value="')
        __M_writer(str(question_title_value))
        __M_writer('"/></td>\n            </tr>\n            <tr>\n                <td class="col-md-4">')
        __M_writer(str(answer_title))
        __M_writer('</td>\n                <td class="col-md-8"><input class="form-control" type="password" name="answer"/></td>\n            </tr>\n            <tr>\n                <td class="col-md-4">')
        __M_writer(str(answer_title2))
        __M_writer('</td>\n                <td class="col-md-8"><input class="form-control" type="password" name="answer2"/></td>\n            </tr>\n            <tr>\n                <td class="col-md-4">')
        __M_writer(str(audio_title))
        __M_writer('</td>\n                <td class="col-md-8"><input class="btn btn-secondary btn-block" type="button" name="audioButton" id="audioButton"\n                        value=')
        __M_writer(str(audio_button))
        __M_writer('/></td>\n            </tr>\n        </table>\n        <input name="username_used" id="username_used" type="number" value="')
        __M_writer(str(username_used))
        __M_writer('" hidden>\n        <div><input class="form-control" type="hidden" name="url" value="')
        __M_writer(str(url))
        __M_writer('"/></div>\n        <div class="submit"><input class="btn btn-primary btn-lg btn-block" type="submit" name="form.commit"\n                        value="')
        __M_writer(str(submit_text))
        __M_writer('"/></div>\n\n    </form>\n    <a href="')
        __M_writer(str(url))
        __M_writer('"><strong>BACK</strong></a><br>\n</div>\n\n')
        __M_writer('\n<script>\n\n  var audioButton = document.getElementById(\'audioButton\');\n\n  var successes = 0;\n\n  audioButton.addEventListener(\'click\', function() {\n        var username = document.getElementById(\'username\').value;\n\n        if (username == "") {\n            alert("Username must be filled out");\n            console.log("Username must be filled out");\n            return false;\n        }else{\n\n            if (successes>=3){\n                return true;\n            }\n\n            var url = "biom_enroll?id=" + username;\n\n            var childWin = window.open(url, "Voiceprint enrollment", "width=500,height=350");\n            return false;\n        }\n  });\n\n  function myFunction(){\n    var error = document.getElementById(\'username_used\');\n\n    if(error.value == 1){\n        alert("Usuario ya existente");\n    }\n    else if (error.value == 2){\n        alert("Password mismatch");\n    }\n    else if (error.value == 3){\n        alert("Answer mismatch");\n    }\n  }\n\n  function shenanigans(val1){\n')
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
{"source_encoding": "utf-8", "uri": "registration.mako", "filename": "htdocs/registration.mako", "line_map": {"64": 32, "65": 36, "66": 36, "67": 38, "68": 38, "69": 41, "70": 41, "71": 42, "72": 42, "73": 44, "74": 44, "75": 47, "76": 47, "77": 56, "78": 99, "84": 50, "88": 50, "27": 0, "94": 88, "46": 1, "47": 6, "48": 6, "49": 12, "50": 12, "51": 13, "52": 13, "53": 16, "54": 16, "55": 20, "56": 20, "57": 24, "58": 24, "59": 25, "60": 25, "61": 28, "62": 28, "63": 32}}
__M_END_METADATA
"""
