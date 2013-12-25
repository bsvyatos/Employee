# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1387018719.779
_enable_loop = True
_template_filename = 'C:\\Users\\Svyatoslav\\Documents\\Pylon_script\\mydev\\Scripts\\Employee\\employee\\templates/newemp.mako'
_template_uri = '/newemp.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\r\n<!DOCTYPE html>\r\n<html lang="en">\r\n  <head>\r\n    <meta charset="utf-8">\r\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\r\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\r\n    <meta name="description" content="">\r\n    <meta name="author" content="">\r\n    <link rel="shortcut icon" href="../../docs-assets/ico/favicon.png">\r\n\r\n    <title>Signin Template for Bootstrap</title>\r\n\r\n    <!-- Bootstrap core CSS -->\r\n    <link href="/css/bootstrap.css" rel="stylesheet">\r\n\r\n    <!-- Custom styles for this template -->\r\n    <link href="/css/signin.css" rel="stylesheet">\r\n\r\n    <!-- Just for debugging purposes. Don\'t actually copy this line! -->\r\n    <!--[if lt IE 9]><script src="../../docs-assets/js/ie8-responsive-file-warning.js"></script><![endif]-->\r\n\r\n    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->\r\n    <!--[if lt IE 9]>\r\n      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>\r\n      <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>\r\n    <![endif]-->\r\n  </head>\r\n\r\n  <body>\r\n\r\n    <div class="container">\r\n\r\n      <form class="form-signin" role="form">\r\n        <h2 class="form-signin-heading">Please sign in</h2>\r\n        <input type="text" class="form-control" placeholder="Email address" required autofocus>\r\n        <input type="password" class="form-control" placeholder="Password" required>\r\n        <label class="checkbox">\r\n          <input type="checkbox" value="remember-me"> Remember me\r\n        </label>\r\n        <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>\r\n      </form>\r\n\r\n    </div> <!-- /container -->\r\n\r\n\r\n    <!-- Bootstrap core JavaScript\r\n    ================================================== -->\r\n    <!-- Placed at the end of the document so the pages load faster -->\r\n  </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


