<%inherit file="root.mako" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<body onload="myFunction()">

<div class="col-md-4 col-md-offset-4 header">
    <h1>${title}</h1>
</div>
<div class="col-md-4 col-md-offset-4 registration_form login_form" class="block">
    <form method="post" class="login form" id="recoveryUserForm">
        <table>
            <tr>
                <td>${username_title}</td>
                <td><input class="form-control" id="username" type="text" name="username" onkeyup='check_username();'/></td>
                <input class="form-control" id="username_used" type="hidden" name="username_used" value="${username_used}"/>
            </tr>
        </table>
        <p style="display:inline; color:red;"  name="wrong_code" id="wrong_code" ></p>
        <div><input class="form-control" type="hidden" name="url" value="${url}"/></div>
        ## --------New Button--------------
        <input class="btn btn-primary btn-lg btn-block top_form" type="button" onclick="checkFields()" value="New ${submit_text}">
        ##--------------------------

    </form>
    <a href="${url}"><strong>Back to login page</strong></a><br>
</div>

<%def name="add_js()">
    <script type="text/javascript">
        $(document).ready(function() {
            bookie.login.init();
        });
    </script>
</%def>

<script>
// -----------My script-----------
function checkFields() {
    var username = document.getElementById("username").value;
    var wrong_code = document.getElementById("wrong_code");
    
    if( username == "" ){

         //alert("Username must be filled out");
         wrong_code.innerHTML = "Username must be filled out";
         document.getElementById("username").style.borderColor = "red";
         exit(0);
    }

    document.getElementById("recoveryUserForm").submit();
}


function myFunction(){
    var failures = document.getElementById('username_used');
    var wrong_code = document.getElementById("wrong_code");

    console.log('myFunction');
    console.log(failures.value);
    if(failures.value == 2){
        //alert("Username not found");
        wrong_code.innerHTML = "Username not found";
        document.getElementById("username").style.borderColor = "red";
    }
  }

  var check_username = function(){
        document.getElementById("username").style.borderColor = "#d3d3d3";
        document.getElementById("wrong_code").innerHTML = "";
    }

//---------------

</script>