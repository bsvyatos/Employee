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
    <link href="/css/new.css" rel="stylesheet">
    <!-- Just for debugging purposes. Don't actually copy this line! -->
    <!--[if lt IE 9]><script src="../../docs-assets/js/ie8-responsive-file-warning.js"></script><![endif]-->

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="http://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="http://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
    <![endif]-->
    <script>
      function Selected(){
        var temp = "${c.depart}";
        var mySelect = document.getElementById('MySelect');
        
        for(var i, j = 0; i = mySelect.options[j]; j++) {
            if(i.value == temp) {
                mySelect.selectedIndex = j;
                break;
            }
        }
       }
    </script>
    
  </head>

  <body onload="Selected()">

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
            <li><a href="list">List All</a></li>
            <li class="active"><a href="newemployee">Add Employee</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </div>

    <div class="container">

      <div class="starter-template">
        <div class="container">
    
          <form class="form-signin" method="post" action="validate">
            <h2 class="form-signin-heading">Add Employee</h2>
            <input type="text" class="form-control" placeholder="Name and Surname" name="sname" value="${c.sname}" required>
                 % if c.sname_msg:
                    <p class="text-danger">${c.sname_msg}</p>
                 % endif
            <input type="text" class="form-control" placeholder="Email address" name="umail" value="${c.umail}" required>
                  % if c.umail_msg:
                    <p class="text-danger">${c.umail_msg}</p>
                  % endif
            <input type="password" class="form-control" placeholder="Password" name="upass" required>
                 % if c.upass_msg: 
                   <p class="text-danger">${c.upass_msg}</p>
                 % endif
            <input type="date" class="form-control" name="birthday" value="${c.ubirth}" required>
            <input type="number" class="form-control" placeholder="Wage" name="wage" value="${c.wage}"required>
            <select class="form-control" name="select" id="MySelect">
                  <option class="form-control" value="sd">Select Department</option>
                  <option value="qa">QA</option>
                  <option value="it">IT</option>
                  <option value="pr">PR</option>
            </select>
                 % if c.select_msg:
                    <p class="text-danger">${c.select_msg}</p>
                 % endif
            <input type="hidden" name="edit" value="">
            <button class="btn btn-lg btn-primary btn-block" type="submit">Add</button>
          </form>
    
        </div> <!-- /container -->      </div>

    </div><!-- /.container -->


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="http://code.jquery.com/jquery-1.10.2.min.js"></script>
    <script src="/js/bootstrap.min.js"></script>
 </body>
</html>
