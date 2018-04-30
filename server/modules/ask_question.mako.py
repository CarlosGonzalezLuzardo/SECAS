# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1510912545.3776953
_enable_loop = True
_template_filename = 'htdocs/ask_question.mako'
_template_uri = 'ask_question.mako'
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
        submit_text = context.get('submit_text', UNDEFINED)
        question_str = context.get('question_str', UNDEFINED)
        question = context.get('question', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="col-md-4 col-md-offset-4 header">\n    <h1>')
        __M_writer(str(title))
        __M_writer('</h1>\n</div>\n<div class="col-md-4 col-md-offset-4 registration_form top_form" class="block">\n    <form method="post" class="login form">\n        <table class="col-md-12">\n            <tr>\n                <td>')
        __M_writer(str(question))
        __M_writer(str(question_str))
        __M_writer('</td>\n            </tr>\n            <tr>\n                <td><input class="form-control" type="text" name="question_ans"/></td>\n            </tr>\n            <tr>\n                </td>\n                <td><input class="btn btn-primary btn-lg btn-block" type="submit" name="form.commit"\n                        value="')
        __M_writer(str(submit_text))
        __M_writer('"/></td>\n            </tr>\n        </table>\n    </form>\n</div>\n\n')
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
{"uri": "ask_question.mako", "line_map": {"36": 1, "37": 4, "38": 4, "39": 10, "40": 10, "41": 10, "42": 18, "43": 18, "44": 30, "50": 24, "54": 24, "27": 0, "60": 54}, "filename": "htdocs/ask_question.mako", "source_encoding": "utf-8"}
__M_END_METADATA
"""
