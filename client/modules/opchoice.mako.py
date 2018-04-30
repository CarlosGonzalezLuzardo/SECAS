# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1511423207.9386148
_enable_loop = True
_template_filename = 'htdocs/opchoice.mako'
_template_uri = 'opchoice.mako'
_source_encoding = 'utf-8'
_exports = []



def op_choice(op_list):
    #Creates a dropdown list of OpenID Connect providers
    element = "<select name=\"op\">"
    for name in op_list:
        element += "<option value=\"%s\">%s</option>" % (name, name)
    element += "</select>"
    return element


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        op_list = context.get('op_list', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<!DOCTYPE html>\n\n<html>\n<head>\n    <title>pyoidc RP</title>\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <!-- Bootstrap -->\n    <link href="static/bootstrap/css/bootstrap.min.css" rel="stylesheet" media="screen">\n    <link href="static/style.css" rel="stylesheet" media="all">\n\n    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->\n    <!--[if lt IE 9]>\n    <script src="../../assets/js/html5shiv.js"></script>\n    <script src="../../assets/js/respond.min.js"></script>\n    <![endif]-->\n</head>\n<body>\n\n<!-- Static navbar -->\n<div class="navbar navbar-default navbar-fixed-top">\n    <div class="navbar-header">\n        <a class="navbar-brand" href="#">pyoidc RP</a>\n    </div>\n</div>\n\n<div class="container">\n    <!-- Main component for a primary marketing message or call to action -->\n    <div class="jumbotron">\n        <form class="form-signin" action="rp" method="get">\n            <h1>OP by UID</h1>\n\n            <h3>Chose the OpenID Connect Provider: </h3>\n\n            <p>From this list</p>\n            ')
        __M_writer(str(op_choice(op_list)))
        __M_writer('\n            <p> OR by providing your unique identifier at the OP. </p>\n            <input type="text" id="uid" name="uid" class="form-control" placeholder="UID" autofocus>\n            <p> OR by providing an issuer id</p>\n            <input type="text" id="issuer" name="issuer" class="form-control" placeholder="ISSUER">\n            <button class="btn btn-lg btn-primary btn-block" type="submit">Start</button>\n        </form>\n    </div>\n\n</div>\n<!-- /container -->\n<!-- jQuery (necessary for Bootstrap\'s JavaScript plugins) -->\n<script src="/static/jquery.min.1.9.1.js"></script>\n<!-- Include all compiled plugins (below), or include individual files as needed -->\n<script src="/static/bootstrap/js/bootstrap.min.js"></script>\n\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "uri": "opchoice.mako", "filename": "htdocs/opchoice.mako", "line_map": {"16": 1, "32": 9, "34": 45, "33": 45, "40": 34, "26": 0}}
__M_END_METADATA
"""
