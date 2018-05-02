# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1525102180.5744016
_enable_loop = True
_template_filename = 'htdocs/biom_enroll.mako'
_template_uri = 'biom_enroll.mako'
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
        action = context.get('action', UNDEFINED)
        nsuccess = context.get('nsuccess', UNDEFINED)
        button_label = context.get('button_label', UNDEFINED)
        username = context.get('username', UNDEFINED)
        submit_text = context.get('submit_text', UNDEFINED)
        nfailures = context.get('nfailures', UNDEFINED)
        file_label = context.get('file_label', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<body onload="myFunction()">\n<div class="header">\n    <h1>')
        __M_writer(str(title))
        __M_writer('</h1>\n\n</div>\n<div class="voiceForm" class="block">\n\n    <p>')
        __M_writer(str(file_label))
        __M_writer('</p>\n    <p>\n        <input type="file" accept="audio/*" capture="microphone" id="recorder"><br>\n        <audio id="player" controls></audio>\n    </p>\n    <form name="biom" id="biom" action="')
        __M_writer(str(action))
        __M_writer('" class="login form" method="post"\n    >\n        <table>\n            <input type="visible" name="username" value="')
        __M_writer(str(username))
        __M_writer('"/>\n            <input name="thefile" id="thefile" type="text" value=\'\' visible>\n            <input name="nsuccess" id="nsuccess" type="number" value="')
        __M_writer(str(nsuccess))
        __M_writer('" visible>\n            <input name="nfailures" id="nfailures" type="number" value="')
        __M_writer(str(nfailures))
        __M_writer('" visible>\n            <tr>\n                <td>')
        __M_writer(str(button_label))
        __M_writer('</td>\n                <td><input type="submit" value=')
        __M_writer(str(submit_text))
        __M_writer(' /></td>\n            </tr>\n        </table>\n    </form>\n</div>\n\n<script type="text/javascript">\n    function validateForm() {\n        var recorder = document.getElementById(\'recorder\');\n\n        var reader  = new FileReader();\n\n        reader.onload = (function()\n        { return function(e)\n            {\n                var myform = document.getElementById(\'thefile\');\n                myform.value = window.btoa(e.target.result);\n                console.log(\'Voiceprint ready to submit\');\n            };\n        })();\n\n        reader.readAsDataURL(recorder.files[0]);\n\n        filename = recorder.value;\n        if (filename == "") {\n            alert("Name must be filled out");\n            return false;\n        }\n    }\n</script>\n\n<script>\n\n  var recorder = document.getElementById(\'recorder\');\n  var player = document.getElementById(\'player\');\n\n  recorder.addEventListener(\'change\', function(e) {\n    var file = e.target.files[0];\n    // Preparing the audio file.\n      validateForm();\n\n    player.src =  URL.createObjectURL(file);\n    console.log(player.src);\n  });\n\n  function OKClicked(){\n      window.opener.shenanigans(true);\n  }\n\n  function myFunction(){\n    var failures = document.getElementById(\'nfailures\');\n    var success = document.getElementById(\'nsuccess\');\n\n    if(failures.value == 4){\n        alert("Usuario ya existente");\n        window.close();\n    }\n    if(success.value == 3){\n        alert("Archivos subidos correctamente");\n        window.close();\n    }\n  }\n</script>\n\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_add_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n    <script type="text/javascript">\n        $(document).ready(function() {\n            bookie.login.init();\n        });\n    </script>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "biom_enroll.mako", "line_map": {"67": 89, "73": 67, "27": 0, "40": 1, "41": 5, "42": 5, "43": 10, "44": 10, "45": 15, "46": 15, "47": 18, "48": 18, "49": 20, "50": 20, "51": 21, "52": 21, "53": 23, "54": 23, "55": 24, "56": 24, "57": 96, "63": 89}, "filename": "htdocs/biom_enroll.mako", "source_encoding": "utf-8"}
__M_END_METADATA
"""
