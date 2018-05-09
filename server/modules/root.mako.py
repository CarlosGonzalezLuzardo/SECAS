# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1525849009.4292605
_enable_loop = True
_template_filename = 'templates/root.mako'
_template_uri = 'root.mako'
_source_encoding = 'utf-8'
_exports = ['css', 'post', 'css_link', 'pre']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        next = context.get('next', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def post():
            return render_post(context._locals(__M_locals))
        set = context.get('set', UNDEFINED)
        def pre():
            return render_pre(context._locals(__M_locals))
        __M_writer = context.writer()
        self.seen_css = set() 
        
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('<html>\n<head><title>OpenID Connect provider example</title>\n')
        __M_writer(str(self.css()))
        __M_writer('\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n')
        __M_writer('</head>\n<body>\n')
        __M_writer(str(pre()))
        __M_writer('\n')
        __M_writer(str(next.body()))
        __M_writer('\n')
        __M_writer(str(post()))
        __M_writer('\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_css(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        context._push_buffer()
        def css_link(path,media=''):
            return render_css_link(context,path,media)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(css_link('/static/bootstrap/css/bootstrap.min.css', 'screen')))
        __M_writer('\n    ')
        __M_writer(str(css_link('/static/bootstrap/css/style.css', 'screen')))
        __M_writer('\n')
    finally:
        __M_buf, __M_writer = context._pop_buffer_and_writer()
        context.caller_stack._pop_frame()
    __M_writer(filters.trim(__M_buf.getvalue()))
    return ''


def render_post(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        context._push_buffer()
        __M_writer = context.writer()
        __M_writer('\n<div>\n    <div class="footer">\n    </div>\n</div>\n')
    finally:
        __M_buf, __M_writer = context._pop_buffer_and_writer()
        context.caller_stack._pop_frame()
    __M_writer(filters.trim(__M_buf.getvalue()))
    return ''


def render_css_link(context,path,media=''):
    __M_caller = context.caller_stack._push_frame()
    try:
        context._push_buffer()
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if path not in self.seen_css:
            __M_writer('    <link rel="stylesheet" type="text/css" href="')
            __M_writer(filters.html_escape(str(path)))
            __M_writer('" media="')
            __M_writer(str(media))
            __M_writer('">\n')
        __M_writer('    ')
        self.seen_css.add(path) 
        
        __M_writer('\n')
    finally:
        __M_buf, __M_writer = context._pop_buffer_and_writer()
        context.caller_stack._pop_frame()
    __M_writer(filters.trim(__M_buf.getvalue()))
    return ''


def render_pre(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        context._push_buffer()
        __M_writer = context.writer()
        __M_writer('\n')
    finally:
        __M_buf, __M_writer = context._pop_buffer_and_writer()
        context.caller_stack._pop_frame()
    __M_writer(filters.trim(__M_buf.getvalue()))
    return ''


"""
__M_BEGIN_METADATA
{"filename": "templates/root.mako", "source_encoding": "utf-8", "line_map": {"96": 6, "69": 14, "74": 14, "98": 6, "16": 0, "92": 4, "82": 2, "95": 6, "88": 2, "89": 3, "90": 4, "91": 4, "28": 1, "93": 4, "30": 1, "31": 7, "32": 11, "33": 13, "34": 19, "35": 22, "36": 24, "37": 24, "38": 28, "39": 30, "40": 30, "41": 33, "42": 33, "43": 34, "44": 34, "111": 12, "50": 8, "106": 12, "94": 4, "119": 111, "57": 8, "58": 9, "59": 9, "60": 10, "61": 10}, "uri": "root.mako"}
__M_END_METADATA
"""
