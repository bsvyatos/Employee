<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">
    
    <title>List All Employees</title>

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

    <script type="text/javascript">
    function click_edit(clicked_id)
      {
        var edt = document.getElementById("eid")
        var dlt = document.getElementById("edel")
        edt.value = clicked_id;
        dlt.value = 'no';
      }
    function click_del(clicked_id)
      {
        var edt = document.getElementById("eid")
        var dlt = document.getElementById("edel")
        edt.value = clicked_id;
        dlt.value = "yes";
      }
    </script>
  </head>

  <body>

    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="home">EM Pro</a>
        </div>
        <div class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
            <li><a href="home">Home</a></li>
            <li class="active"><a href="#">List All</a></li>
            <li><a href="newemployee">Add Employee</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </div>

    <div class="container">

      <div class="starter-template">
        <h1>All Workers</h1>
        <p class="lead">I guess some kind of list should be here</p>
      </div>
      <form id = "edtdlt" method="get" action="edit">
      <div class="container">
          <table class="table table-bordered">
          <thead>
            <tr>
              <th>#</th>
              <th>Full name</th>
              <th>Username</th>
              <th>Email</th>
              <th>Birthday</th>
              <th>Wage</th>
              <th>Department</th>
              <th>Edit</th>
              <th>Delete</th>
            </tr>
          </thead>
            <tbody>
              ${c.txttosend | n}
            </tbody>
        </table>
        <input type="hidden" id="eid" name="iid" value="">
        <input type="hidden" id="edel" name="del" value="">
      </div>
      </form>

    </div><!-- /.container -->


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="http://code.jquery.com/jquery-1.10.2.min.js"></script>
    <script src="/js/bootstrap.min.js"></script>
    
 </body>
</html>
