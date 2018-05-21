<%inherit file="root.mako" />

<body onload="myFunction()">

<div class="col-md-4 col-md-offset-4 header">
    <h1>${title}</h1>
</div>
<div class="col-md-4 col-md-offset-4 registration_form login_form" class="block">
    <form method="post" class="login form" id="modify_pwd">
        <table>
            <tr>
                <td>${username_title}</td>
                <td>${username}</td>
            </tr>
            <tr>
                <td>${password_title}</td>
                <td><input class="form-control" id="password" type="password" name="password" onkeyup='check_oldpassword();'/></td>
            </tr>
            <tr>
                <td>${newpassword_title}</td>
                <td><input class="form-control" id="newpassword" type="password" name="newpassword" onkeyup='check_password();'/></td>
            </tr>
            <tr>
                <td>${confnewpassword_title}</td>
                <td><input class="form-control" id="confnewpassword" type="password" name="confnewpassword" onkeyup='check_password();'/></td>
            </tr>
            <tr>
        </table>

        <p style="display:inline; color:red;"  name="wrong_code" id="wrong_code" ></p>
        <div><input class="form-control" type="hidden" name="wrong_value" value="${wrong_value}" id="wrong_value"/></div>
        <div><input class="form-control" type="hidden" name="url" value="${url}" id="url"/></div>
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
    var password = document.getElementById("password").value;
    var newpassword = document.getElementById("newpassword").value;
    var confnewpassword = document.getElementById("confnewpassword").value;
    var wrong_code = document.getElementById("wrong_code");

    if( password == "" ){
         //alert("You have to choose a new password");
         wrong_code.innerHTML = "You have to confirm your old password";
         document.getElementById("password").style.borderColor = "red";
         exit(0);
    }
    if( newpassword == "" ){
         //alert("You have to choose a new password");
         wrong_code.innerHTML = "You have to choose your new password";
         document.getElementById("newpassword").style.borderColor = "red";
         exit(0);
    }
    if( confnewpassword == "" ){
         //alert("You have to confirm your new password");
         wrong_code.innerHTML = "You have to confirm your new password";
         document.getElementById("confnewpassword").style.borderColor = "red";
         exit(0);
    }
    if( newpassword != confnewpassword){
        //alert("Fields must have the same value!");
        wrong_code.innerHTML = "Fields must have the same value!";
        document.getElementById("newpassword").style.borderColor = "red";
        document.getElementById("confnewpassword").style.borderColor = "red";
        exit(0);
    }
    document.getElementById("modify_pwd").submit();
}

var check_password = function() {
  if ((document.getElementById('newpassword').value ==
    document.getElementById('confnewpassword').value) &&  (document.getElementById('newpassword').value != "")){
    document.getElementById('newpassword').style.color = 'green';
    document.getElementById('newpassword').innerHTML = 'matching';
    document.getElementById('confnewpassword').style.color = 'green';
    document.getElementById('confnewpassword').innerHTML = 'matching';
    //document.getElementById('ok').style.visibility = "visible";
    //document.getElementById('ok').style.color = "green"
    document.getElementById("newpassword").style.borderColor = "green";
    document.getElementById("confnewpassword").style.borderColor = "green";
    document.getElementById("wrong_code").innerHTML = "";
    document.getElementById("newpassword").style.borderColor = "#d3d3d3";
    document.getElementById("confnewpassword").style.borderColor = "#d3d3d3";
    document.getElementById("wrong_code").innerHTML = "  ";
  } else {
    document.getElementById('newpassword').style.color = 'red';
    document.getElementById('newpassword').innerHTML = 'not matching';
    document.getElementById('confnewpassword').style.color = 'red';
    document.getElementById('confnewpassword').innerHTML = 'not matching';
    //document.getElementById('ok').style.visibility = "hidden";
    document.getElementById("newpassword").style.borderColor = "red";
    document.getElementById("confnewpassword").style.borderColor = "red";
    document.getElementById("newpassword").style.borderColor = "#d3d3d3";
    document.getElementById("confnewpassword").style.borderColor = "#d3d3d3";
    document.getElementById("wrong_code").innerHTML = "  ";
  }
}

var check_oldpassword = function(){
        document.getElementById("password").style.borderColor = "#d3d3d3";
        document.getElementById("wrong_code").innerHTML = "";
    }


    function myFunction(){
    var wrong_value = document.getElementById('wrong_value');

    if(wrong_value.value == 1){
        //alert("Usuario ya existente");
        document.getElementById("wrong_code").style.borderColor = "black";
        wrong_code.innerHTML = "Password updated";
        //window.location.href = document.getElementById('url').value;
        window.setTimeout(function(){

        // Move to a new location or you can do something else
        window.location.href = document.getElementById('url').value;

        }, 2000);
    }
    else if (wrong_value.value == 2){
        //alert("Password mismatch");
        wrong_code.innerHTML = "Wrong Password";
    }
  }
//---------------

</script>