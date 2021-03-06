<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <title>Add new Employee</title>

    <!-- Bootstrap core CSS -->
    <link href="/css/bootstrap.css" rel="stylesheet" />
      
    <!-- Custom styles for this template -->
    <link href="/css/starter-template.css" rel="stylesheet">
    <script type="text/javascript">
      
      var monthtext=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec'];
      
      function populatedropdown(dayfield, monthfield, yearfield){
      var today=new Date()
      var dayfield=document.getElementById(dayfield)
      var monthfield=document.getElementById(monthfield)
      var yearfield=document.getElementById(yearfield)
      for (var i=0; i<31; i++)
      dayfield.options[i]=new Option(i, i+1)
      dayfield.options[today.getDate()]=new Option(today.getDate(), today.getDate(), true, true) //select today's day
      for (var m=0; m<12; m++)
      monthfield.options[m]=new Option(monthtext[m], monthtext[m])
      monthfield.options[today.getMonth()]=new Option(monthtext[today.getMonth()], monthtext[today.getMonth()], true, true) //select today's month
      var thisyear=today.getFullYear()
      for (var y=0; y<20; y++){
      yearfield.options[y]=new Option(thisyear, thisyear)
      thisyear+=1
      }
      yearfield.options[0]=new Option(today.getFullYear(), today.getFullYear(), true, true) //select today's year
      }
    
    </script>

    <link href="/css/new.css" rel="stylesheet">
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
            <input type="text" class="form-control" placeholder="Username" name="uname" value="${c.uname}" required>
                 % if c.uname_msg:
                    <p class="text-danger">${c.uname_msg}</p>
                 % endif
            <input type="text" class="form-control" placeholder="Email address" name="umail" value="${c.umail}" required>
                  % if c.umail_msg:
                    <p class="text-danger">${c.umail_msg}</p>
                  % endif
            <input type="password" class="form-control" placeholder="Password" name="upass" required>
                 % if c.upass_msg: 
                   <p class="text-danger">${c.upass_msg}</p>
                 % endif
            Day<select id="daydropdown">
            </select> 
            Month<select id="monthdropdown">
            </select> 
            Year<select id="yeardropdown">
            </select> 
            
            <script type="text/javascript">
            
            //populatedropdown(id_of_day_select, id_of_month_select, id_of_year_select)
            window.onload=function(){
            populatedropdown("daydropdown", "monthdropdown", "yeardropdown")
            }
            </script>

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

	<script src="/js/jquery-2.0.3.min.js"></script>
    <script src="/js/bootstrap.min.js"></script>
 </body>
</html>
