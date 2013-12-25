<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Starter Template for Bootstrap</title>

    <!-- Bootstrap core CSS -->
    <link href="/css/bootstrap.css" rel="stylesheet" />

    <!-- Custom styles for this template -->
    <link href="/css/starter-template.css" rel="stylesheet">

    <!-- Just for debugging purposes. Don't actually copy this line! -->
    <!--[if lt IE 9]><script src="../../docs-assets/js/ie8-responsive-file-warning.js"></script><![endif]-->

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="http://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="http://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>
  <style>
    .medium{
    width: 180px;
    height: 36px;
    }
  </style>
    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">EM Pro</a>
        </div>
        <div class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href="#">Home</a></li>
            <li><a href="list">List All</a></li>
            <li><a href="newemployee">Add Employee</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </div>

    <div class="container">

      <div class="starter-template">
        <h1>Employee Manager Pro</h1>
        <p class="lead">Best and simpliest Employee manager tool to date.<br>
            To Unleesh the power of this tool press button below. <br>
            <!-- Button trigger modal -->
            <button class="btn btn-primary medium" data-toggle="modal" data-target="#myModal">
              Add New Employee
            </button>
        </p>
      </div>

    </div><!-- /.container -->


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="http://code.jquery.com/jquery-1.10.2.min.js"></script>
    <script src="/js/bootstrap.min.js"></script>
    <!-- Modal -->
    <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
            <h4 class="modal-title" id="myModalLabel">Add Employee</h4>
          </div>
          <form action="validate" method="post">
            <div class="modal-body">
              <div class="input-group">
                Name 
                <input type="text" class="form-control" placeholder="Name and Surname" name="sname">
                Username
                <input type="text" class="form-control" placeholder="Username" name="uname">
                Password
                <input type="password" class="form-control" placeholder="Password" name="upass">
                Email
                <input type="text" class="form-control" placeholder="Email" name="umail">
                Birthday
                <input type="date" class="form-control" placeholder="Birthday" name="birthday">
                Wage
                <input type="text" class="form-control" placeholder="Wage" name="wage">
                Department
                <select class="form-control" name="select">
                  <option value="sd">Select Department</option>
                  <option value="qa">QA</option>
                  <option value="it">IT</option>
                  <option value="pr">PR</option>
                </select>
              </div>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
              <input type="hidden" name="edit" value="">
              <button type="submit" class="submit btn primary-btn">Add</button>
            </div>
          </form>
        </div><!-- /.modal-content -->
      </div><!-- /.modal-dialog -->
    </div><!-- /.modal -->

  </body>
</html>
