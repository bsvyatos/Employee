# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1387033835.365
_enable_loop = True
_template_filename = 'C:\\Users\\Svyatoslav\\Documents\\Pylon_script\\mydev\\Scripts\\Employee\\employee\\templates/main.mako'
_template_uri = '/main.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html>\r\n<html lang="en">\r\n  <head>\r\n    <meta charset="utf-8">\r\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\r\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\r\n    <meta name="description" content="">\r\n    <meta name="author" content="">\r\n    \r\n    <title>Starter Template for Bootstrap</title>\r\n\r\n    <!-- Bootstrap core CSS -->\r\n    <link href="/css/bootstrap.css" rel="stylesheet" />\r\n      \r\n    <!-- Custom styles for this template -->\r\n    <link href="/css/starter-template.css" rel="stylesheet"> \r\n    <link href="/css/new.css" rel="stylesheet">\r\n    <!-- Just for debugging purposes. Don\'t actually copy this line! -->\r\n    <!--[if lt IE 9]><script src="../../docs-assets/js/ie8-responsive-file-warning.js"></script><![endif]-->\r\n\r\n    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->\r\n    <!--[if lt IE 9]>\r\n      <script src="http://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>\r\n      <script src="http://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>\r\n    <![endif]-->\r\n  </head>\r\n\r\n  <body>\r\n\r\n    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">\r\n      <div class="container">\r\n        <div class="navbar-header">\r\n          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">\r\n            <span class="sr-only">Toggle navigation</span>\r\n            <span class="icon-bar"></span>\r\n            <span class="icon-bar"></span>\r\n            <span class="icon-bar"></span>\r\n          </button>\r\n          <a class="navbar-brand" href="testboot">EM Pro</a>\r\n        </div>\r\n        <div class="collapse navbar-collapse">\r\n          <ul class="nav navbar-nav">\r\n            <li><a href="testboot">Home</a></li>\r\n            <li><a href="boot">List All</a></li>\r\n            <li class="active"><a href="newemployee">Add Employee</a></li>\r\n          </ul>\r\n        </div><!--/.nav-collapse -->\r\n      </div>\r\n    </div>\r\n\r\n    <div class="container">\r\n\r\n      <div class="starter-template">\r\n        <div class="container">\r\n    \r\n          <form class="form-signin" method="post" action="validate">\r\n            <h2 class="form-signin-heading">Add Employee</h2>\r\n            <input type="text" class="form-control" placeholder="Name and Surname" name="sname" value="')
        # SOURCE LINE 58
        __M_writer(escape(c.sname))
        __M_writer(u'" required>\r\n')
        # SOURCE LINE 59
        if c.sname_msg:
            # SOURCE LINE 60
            __M_writer(u'                    <p class="text-danger">')
            __M_writer(escape(c.sname_msg))
            __M_writer(u'</p>\r\n')
        # SOURCE LINE 62
        __M_writer(u'            <input type="text" class="form-control" placeholder="Username" name="uname" value="')
        __M_writer(escape(c.uname))
        __M_writer(u'" required>\r\n')
        # SOURCE LINE 63
        if c.uname_msg:
            # SOURCE LINE 64
            __M_writer(u'                    <p class="text-danger">')
            __M_writer(escape(c.uname_msg))
            __M_writer(u'</p>\r\n')
        # SOURCE LINE 66
        __M_writer(u'            <input type="text" class="form-control" placeholder="Email address" name="umail" value="')
        __M_writer(escape(c.umail))
        __M_writer(u'" required>\r\n')
        # SOURCE LINE 67
        if c.umail_msg:
            # SOURCE LINE 68
            __M_writer(u'                    <p class="text-danger">')
            __M_writer(escape(c.umail_msg))
            __M_writer(u'</p>\r\n')
        # SOURCE LINE 70
        __M_writer(u'            <input type="password" class="form-control" placeholder="Password" name="upass" required>\r\n')
        # SOURCE LINE 71
        if c.upass_msg: 
            # SOURCE LINE 72
            __M_writer(u'                   <p class="text-danger">')
            __M_writer(escape(c.upass_msg))
            __M_writer(u'</p>\r\n')
        # SOURCE LINE 74
        __M_writer(u'            <input type="date" class="form-control">\r\n            <input type="number" class="form-control" placeholder="Wage" required>\r\n            <select class="form-control" name="select">\r\n                  <option class="form-control" value="sd">Select Department</option>\r\n                  <option value="qa">QA</option>\r\n                  <option value="it">IT</option>\r\n                  <option value="pr">PR</option>\r\n            </select>\r\n')
        # SOURCE LINE 82
        if c.select_msg:
            # SOURCE LINE 83
            __M_writer(u'                    <p class="text-danger">')
            __M_writer(escape(c.select_msg))
            __M_writer(u'</p>\r\n')
        # SOURCE LINE 85
        __M_writer(u'            <button class="btn btn-lg btn-primary btn-block" type="submit">Add</button>\r\n          </form>\r\n    \r\n        </div> <!-- /container -->      </div>\r\n\r\n    </div><!-- /.container -->\r\n\r\n\r\n    <!-- Bootstrap core JavaScript\r\n    ================================================== -->\r\n    <!-- Placed at the end of the document so the pages load faster -->\r\n    <script src="http://code.jquery.com/jquery-1.10.2.min.js"></script>\r\n    <script src="/js/bootstrap.min.js"></script>\r\n </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


