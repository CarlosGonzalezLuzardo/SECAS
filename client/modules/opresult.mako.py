# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1486728126.6655185
_enable_loop = True
_template_filename = 'htdocs/opresult.mako'
_template_uri = 'opresult.mako'
_source_encoding = 'utf-8'
_exports = []



from html import entities as htmlentitydefs
import re

# this pattern matches substrings of reserved and non-ASCII characters
pattern = re.compile(r"[&<>\"\x80-\xff]+")

# create character map
entity_map = {}

for i in range(256):
    entity_map[chr(i)] = "&#%d;" % i

for entity, char in htmlentitydefs.entitydefs.items():
    if char in entity_map:
        entity_map[char] = "&%s;" % entity

def escape_entity(m, get=entity_map.get):
    return "".join(map(get, m.group()))

def escape(string):
    return pattern.sub(escape_entity, string)

def create_result(userinfo, user_id, id_token):
    """
        Creates a display of user information.
        """
    element = "<h3>You have successfully authenticated!</h3>"
    if id_token:
      element += '<h3>With the following authentication information</h3>'
      for key, value in id_token.items():
          element += "<div class='row'>"
          element += "<div class='col-md-3'>" +  escape(str(key)) + "</div>"
          element += "<div class='col-md-7'>" + escape(str(value)) + "</div>"
          element += "</div>"
    if user_id:
      element += '<h3>And are now known to the RP as:</h3>'
      element += '<i>'+userid+'</i>'
    if userinfo:
      element += '<h3>With the following user information</h3>'
      for key, value in userinfo.items():
          element += "<div class='row'>"
          element += "<div class='col-md-3'>" +  escape(str(key)) + "</div>"
          element += "<div class='col-md-7'>" + escape(str(value)) + "</div>"
          element += "</div>"
    return element


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        userinfo = context.get('userinfo', UNDEFINED)
        user_id = context.get('user_id', UNDEFINED)
        id_token = context.get('id_token', UNDEFINED)
        check_session_iframe_url = context.get('check_session_iframe_url', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n\n')
        __M_writer('\n\n<html>\n<head>\n    <title>pyoidc RP</title>\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <!-- Bootstrap -->\n    <link href="static/bootstrap/css/bootstrap.min.css" rel="stylesheet" media="screen">\n    <link href="static/style.css" rel="stylesheet" media="all">\n\n    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->\n    <!--[if lt IE 9]>\n    <script src="../../assets/js/html5shiv.js"></script>\n    <script src="../../assets/js/respond.min.js"></script>\n    <![endif]-->\n</head>\n<body>\n\n<!-- Static navbar -->\n<div class="navbar navbar-default navbar-fixed-top">\n    <div class="navbar-header">\n        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n        </button>\n        <a class="navbar-brand" href="#">pyoidc RP</a>\n    </div>\n    <div class="navbar-collapse collapse">\n        <ul class="nav navbar-nav">\n        </ul>\n        <ul class="nav navbar-nav navbar-right">\n            <li><a href="modify_user">Update Passwords</a></li>\n            <li><a href="logout">Logout</a></li>\n        </ul>\n    </div>\n    <!--/.nav-collapse -->\n</div>\n\n<div class="container">\n    <!-- Main component for a primary marketing message or call to action -->\n    <div class="jumbotron">\n        <h1>OP result</h1>\n        ')
        __M_writer(str(create_result(userinfo, user_id, id_token)))
        __M_writer('\n    </div>\n\n</div>\n<!-- /container -->\n\n\n')
        if check_session_iframe_url is not UNDEFINED:
            __M_writer('    <iframe id="rp_iframe" src="/session_iframe" hidden></iframe>\n    <iframe id="op_iframe" src="')
            __M_writer(str(check_session_iframe_url))
            __M_writer('" hidden></iframe>\n')
        __M_writer('\n\n<!-- jQuery (necessary for Bootstrap\'s JavaScript plugins) -->\n<script src="/static/jquery.min.1.9.1.js"></script>\n<!-- Include all compiled plugins (below), or include individual files as needed -->\n<script src="/static/bootstrap/js/bootstrap.min.js"></script>\n\n\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "opresult.mako", "line_map": {"64": 0, "80": 101, "73": 1, "74": 49, "75": 92, "76": 92, "77": 99, "78": 100, "79": 101, "16": 3, "81": 103, "87": 81}, "source_encoding": "utf-8", "filename": "htdocs/opresult.mako"}
__M_END_METADATA
"""
