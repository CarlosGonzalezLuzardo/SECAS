# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1505476004.9228826
_enable_loop = True
_template_filename = 'htdocs/biom_form.mako'
_template_uri = 'biom_form.mako'
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
        button_label = context.get('button_label', UNDEFINED)
        title = context.get('title', UNDEFINED)
        submit_text = context.get('submit_text', UNDEFINED)
        username = context.get('username', UNDEFINED)
        file_label = context.get('file_label', UNDEFINED)
        action = context.get('action', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="header">\n    <h1>')
        __M_writer(str(title))
        __M_writer('</h1>\n</div>\n<div class="login_form" class="block">\n\n    <p>')
        __M_writer(str(file_label))
        __M_writer('</p>\n    <p>\n    <input type="file" accept="audio/*" capture="microphone" id="recorder"><br>\n    <audio id="player" controls></audio>\n    </p>\n    <form name="biom" id="biom" action="')
        __M_writer(str(action))
        __M_writer('" class="login form" method="post"\n    >\n        <table>\n            <input type="hidden" name="username" value="')
        __M_writer(str(username))
        __M_writer('"/>\n            <input name="thefile" id="thefile" type="text" value=\'\' hidden>\n            <tr>\n                <td>')
        __M_writer(str(button_label))
        __M_writer('</td>\n                <td><input type="submit" value=')
        __M_writer(str(submit_text))
        __M_writer(' /></td>\n            </tr>\n        </table>\n    </form>\n</div>\n\n<script type="text/javascript">\n    function validateForm() {\n        var recorder = document.getElementById(\'recorder\');\n\n        var reader  = new FileReader();\n\n        reader.onload = (function()\n        { return function(e)\n            {\n                var myform = document.getElementById(\'thefile\');\n                myform.value = window.btoa(e.target.result);\n                console.log(\'Voiceprint ready to submit\');\n            };\n        })();\n\n        reader.readAsDataURL(recorder.files[0]);\n\n        filename = recorder.value;\n        if (filename == "") {\n            alert("Name must be filled out");\n            return false;\n        }\n    }\n</script>\n\n<script>\n\n  var recorder = document.getElementById(\'recorder\');\n  var player = document.getElementById(\'player\');\n\n  recorder.addEventListener(\'change\', function(e) {\n    var file = e.target.files[0];\n    // Preparing the audio file.\n      validateForm();\n\n    player.src =  URL.createObjectURL(file);\n    console.log(player.src);\n  });\n\n</script>\n\n\n')
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
{"line_map": {"67": 61, "38": 1, "39": 4, "40": 4, "41": 8, "42": 8, "43": 13, "44": 13, "45": 16, "46": 16, "47": 19, "48": 19, "49": 20, "50": 20, "51": 75, "57": 68, "27": 0, "61": 68}, "filename": "htdocs/biom_form.mako", "uri": "biom_form.mako", "source_encoding": "utf-8"}
__M_END_METADATA
"""
