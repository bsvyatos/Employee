# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1387018246.517
_enable_loop = True
_template_filename = 'C:\\Users\\Svyatoslav\\Documents\\Pylon_script\\mydev\\Scripts\\Employee\\employee\\templates/boot.mako'
_template_uri = '/boot.mako'
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
        __M_writer(u'<!DOCTYPE html>\r\n<html lang="en">\r\n  <head>\r\n    <meta charset="utf-8">\r\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\r\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\r\n    <meta name="description" content="">\r\n    <meta name="author" content="">\r\n    \r\n    <title>Starter Template for Bootstrap</title>\r\n\r\n    <!-- Bootstrap core CSS -->\r\n    <link href="/css/bootstrap.css" rel="stylesheet" />\r\n      \r\n    <!-- Custom styles for this template -->\r\n    <link href="/css/starter-template.css" rel="stylesheet">\r\n\r\n    <!-- Just for debugging purposes. Don\'t actually copy this line! -->\r\n    <!--[if lt IE 9]><script src="../../docs-assets/js/ie8-responsive-file-warning.js"></script><![endif]-->\r\n\r\n    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->\r\n    <!--[if lt IE 9]>\r\n      <script src="http://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>\r\n      <script src="http://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>\r\n    <![endif]-->\r\n  </head>\r\n\r\n  <body>\r\n\r\n    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">\r\n      <div class="container">\r\n        <div class="navbar-header">\r\n          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">\r\n            <span class="sr-only">Toggle navigation</span>\r\n            <span class="icon-bar"></span>\r\n            <span class="icon-bar"></span>\r\n            <span class="icon-bar"></span>\r\n          </button>\r\n          <a class="navbar-brand" href="testboot">EM Pro</a>\r\n        </div>\r\n        <div class="collapse navbar-collapse">\r\n          <ul class="nav navbar-nav">\r\n            <li><a href="testboot">Home</a></li>\r\n            <li class="active"><a href="#">List All</a></li>\r\n            <li><a href="newemployee">Add Employee</a></li>\r\n          </ul>\r\n        </div><!--/.nav-collapse -->\r\n      </div>\r\n    </div>\r\n\r\n    <div class="container">\r\n\r\n      <div class="starter-template">\r\n        <h1>All Workers</h1>\r\n        <p class="lead">I guess some kind of list should be here</p>\r\n      </div>\r\n      <div class="container">\r\n          <table class="table table-bordered">\r\n          <thead>\r\n            <tr>\r\n              <th>#</th>\r\n              <th>Name</th>\r\n              <th>Email</th>\r\n              <th>Birthday</th>\r\n              <th>Wage</th>\r\n              <th>Department</th>\r\n            </tr>\r\n          </thead>\r\n          <tbody>\r\n            <tr>\r\n              <td>1</td>\r\n              <td>Mark</td>\r\n              <td>Otto</td>\r\n              <td>@mdo</td>\r\n              <td>123</td>\r\n              <td>qa</td>\r\n            </tr>\r\n            <tr>\r\n              <td>2</td>\r\n              <td>Jacob</td>\r\n              <td>Thornton</td>\r\n              <td>@fat</td>\r\n              <td>123</td>\r\n              <td>qa</td>\r\n            </tr>\r\n            <tr>\r\n              <td>3</td>\r\n              <td>Larry</td>\r\n              <td>the Bird</td>\r\n              <td>@twitter</td>\r\n              <td>123</td>\r\n              <td>qa</td>\r\n            </tr>\r\n            <td>')
        # SOURCE LINE 94
        __M_writer(escape(c.txttosend))
        __M_writer(u'</td>\r\n          </tbody>\r\n        </table>\r\n      </div>\r\n\r\n    </div><!-- /.container -->\r\n\r\n\r\n    <!-- Bootstrap core JavaScript\r\n    ================================================== -->\r\n    <!-- Placed at the end of the document so the pages load faster -->\r\n    <script src="http://code.jquery.com/jquery-1.10.2.min.js"></script>\r\n    <script src="/js/bootstrap.min.js"></script>\r\n </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


