<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <title>Edit employee information</title>

    <!-- Bootstrap core CSS -->
    <link href="/css/bootstrap.css" rel="stylesheet" />
      
    <!-- Custom styles for this template -->
    <link href="/css/starter-template.css" rel="stylesheet"> 
    <link href="/css/new.css" rel="stylesheet">
	<script src="/js/jquery-2.0.3.min.js"></script>
	<script src="/js/bootstrap.min.js"></script>
    <script type="text/javascript">
      
      var monthtext=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec'];
      
	  if ("${c.ubirth}") {
        var birth = "${c.ubirth}".split("/");
		$.each(monthtext, function(i, item) {
			if (birth[1] == item) {
				birth[1]=i;
				return false;
			}
		});
      }
            
      function populatedropdown(dayfield, monthfield, yearfield){
		  var today=new Date();
		  var dayfield=document.getElementById(dayfield);
		  var monthfield=document.getElementById(monthfield);
		  var yearfield=document.getElementById(yearfield);
		  for (var i=0; i<31; i++)
			dayfield.options[i]=new Option(i, i+1)
		  if (birth) {
			dayfield.options[birth[0]]=new Option(birth[0], birth[0], true, true)
		  } else {
			dayfield.options[today.getDate()]=new Option(today.getDate(), today.getDate(), true, true) //select today's day
		  }
		  for (var m=0; m<12; m++)
			monthfield.options[m]=new Option(monthtext[m], monthtext[m])
      
		  if (birth) {
			monthfield.options[birth[1]]=new Option(monthtext[birth[1]], monthtext[birth[1]], true, true)
		  } else {
			monthfield.options[today.getMonth()]=new Option(monthtext[today.getMonth()], monthtext[today.getMonth()], true, true) //select today's month
		  }
		  var yearstart=today.getFullYear() - 13;
		  var defaultchoise=yearstart;
		  for (var y=0; y<100; y++){
			yearfield.options[y]=new Option(yearstart, yearstart);
			yearstart-=1;
		  }

		  if (birth) {
			yearfield.options[defaultchoise - birth[2]]=new Option(birth[2], birth[2], true, true)
		  } else {
			yearfield.options[0]=new Option(defaultchoise, defaultchoise, true, true)
		  }
	  }
    
    </script>
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
            <li><a href="newemployee">Add Employee</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </div>

    <div class="container">

      <div class="starter-template">
        <div class="container">
    
          <form class="form-signin" method="post" action="validate">
            <h2 class="form-signin-heading">${c.state} Employee</h2>
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
            <input type="number" class="form-control" placeholder="Wage" name="wage" value="${c.wage}"required>
            <select class="form-control" name="select" id="MySelect">
                  <option class="form-control" value="sd">Select Department</option>
				  ${c.txttosend | n}
            </select>
            <div class="bs-example">
              Day<select  id="daydropdown" name="birthday_day">
              </select> 
              Month<select id="monthdropdown" name="birthday_month">
              </select> 
              Year<select id="yeardropdown" name="birthday_year">
              </select> 
            </div>
            <script type="text/javascript">
				window.onload=function(){
					populatedropdown("daydropdown", "monthdropdown", "yeardropdown")
				}
            </script>
                 % if c.select_msg:
                    <p class="text-danger">${c.select_msg}</p>
                 % endif
            <input type="hidden" name="state" value="${c.state}">
            <input type="hidden" name="iid" value="${c.iid}">
            <button class="btn btn-lg btn-primary btn-block" type="submit">${c.submit}</button>
          </form>
    
        </div> <!-- /container -->      </div>

    </div><!-- /.container -->

 </body>
</html>
