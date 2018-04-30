# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523001738.1200407
_enable_loop = True
_template_filename = 'htdocs/operror.mako'
_template_uri = 'operror.mako'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        error = context.get('error', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n\n<html>\n<head>\n    <title>pyoidc RP</title>\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <!-- Bootstrap -->\n    <link href="static/bootstrap/css/bootstrap.min.css" rel="stylesheet" media="screen">\n    <link href="static/style.css" rel="stylesheet" media="all">\n\n    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->\n    <!--[if lt IE 9]>\n    <script src="../../assets/js/html5shiv.js"></script>\n    <script src="../../assets/js/respond.min.js"></script>\n    <![endif]-->\n</head>\n<body>\n\n<!-- Static navbar -->\n<div class="navbar navbar-default navbar-fixed-top">\n    <div class="navbar-header">\n        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n        </button>\n        <a class="navbar-brand" href="#">pyoidc RP</a>\n    </div>\n    <div class="navbar-collapse collapse">\n        <ul class="nav navbar-nav">\n        </ul>\n        <ul class="nav navbar-nav navbar-right">\n            <li><a href="logout">Logout</a></li>\n        </ul>\n    </div>\n    <!--/.nav-collapse -->\n</div>\n\n<div class="container">\n    <!-- Main component for a primary marketing message or call to action -->\n    <div class="jumbotron">\n        <h1>OP result</h1>\n\n        <p>You have failed to connect to the designated OP with the message:</p>\n\n        <p>')
        __M_writer(str(error))
        __M_writer('</p>\n    </div>\n\n</div>\n<!-- /container -->\n<!-- jQuery (necessary for Bootstrap\'s JavaScript plugins) -->\n<script src="/static/jquery.min.1.9.1.js"></script>\n<!-- Include all compiled plugins (below), or include individual files as needed -->\n<script src="/static/bootstrap/js/bootstrap.min.js"></script>\n\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "filename": "htdocs/operror.mako", "uri": "operror.mako", "line_map": {"16": 0, "24": 46, "30": 24, "22": 1, "23": 46}}
__M_END_METADATA
"""
