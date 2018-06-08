<%inherit file="root.mako" />

<div class="col-md-4 col-md-offset-4 header">
    <h1>${title}</h1>
   ## <h1>${url}</h1>
</div>
<div class="col-md-4 col-md-offset-4 registration_form top_form" class="block">
    <form method="post" class="login form" id="recoveryNewpwdForm">
        <table>
            <tr>
                <td>${password_title}</td>
                <td><input class="form-control" id="new_pwd" type="password" name="password" onkeyup='check_password();'/></td>
            </tr>
            <tr>
                <td>${newpassword_title}</td>
                <td><input class="form-control" id="confirm_pwd" type="password" name="newpassword" onkeyup='check_password();'/></td>
            </tr>
        </table>
            <div><input class="form-control" type="hidden" name="url" value="${url}"/></div>
            <p style="display:inline; color:red;"  name="wrong_code" id="wrong_code" ><br><br></p>
        ## --------New Button----------------
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
    var new_pwd = document.getElementById("new_pwd").value;
    var confirm_pwd = document.getElementById("confirm_pwd").value;
    var wrong_code = document.getElementById("wrong_code");

    if( new_pwd == "" && confirm_pwd == ""){
         //alert("Your password fields must be filled out");
         wrong_code.innerHTML = "Username must be filled out";
         document.getElementById("new_pwd").style.borderColor = "red";
         document.getElementById("confirm_pwd").style.borderColor = "red";
         exit(0);
    }
    if( new_pwd == "" ){
         //alert("You have to choose a new password");
         wrong_code.innerHTML = "You have to choose a new password";
         document.getElementById("new_pwd").style.borderColor = "red";
         exit(0);
    }
    if( confirm_pwd == "" ){
         //alert("You have to confirm your new password");
         wrong_code.innerHTML = "You have to confirm your new password";
         document.getElementById("confirm_pwd").style.borderColor = "red";
         exit(0);
    }
    if( new_pwd != confirm_pwd){
        //alert("Fields must have the same value!");
        wrong_code.innerHTML = "Fields must have the same value!";
        document.getElementById("new_pwd").style.borderColor = "red";
        document.getElementById("confirm_pwd").style.borderColor = "red";
        exit(0);
    }
    document.getElementById("recoveryNewpwdForm").submit();
}

var check_password = function() {
  if ((document.getElementById('new_pwd').value ==
    document.getElementById('confirm_pwd').value) &&  (document.getElementById('new_pwd').value != "")){
    document.getElementById('new_pwd').style.color = 'green';
    document.getElementById('new_pwd').innerHTML = 'matching';
    document.getElementById('confirm_pwd').style.color = 'green';
    document.getElementById('confirm_pwd').innerHTML = 'matching';
    //document.getElementById('ok').style.visibility = "visible";
    //document.getElementById('ok').style.color = "green"
    document.getElementById("new_pwd").style.borderColor = "green";
    document.getElementById("confirm_pwd").style.borderColor = "green";
    document.getElementById("wrong_code").innerHTML = "<br><br>";
    //document.getElementById("new_pwd").style.borderColor = "#d3d3d3";
    //document.getElementById("confirm_pwd").style.borderColor = "#d3d3d3";
    document.getElementById("wrong_code").innerHTML = "  ";
  } else {
    document.getElementById('new_pwd').style.color = 'red';
    document.getElementById('new_pwd').innerHTML = 'not matching';
    document.getElementById('confirm_pwd').style.color = 'red';
    document.getElementById('confirm_pwd').innerHTML = 'not matching';
    //document.getElementById('ok').style.visibility = "hidden";
    document.getElementById("new_pwd").style.borderColor = "red";
    document.getElementById("confirm_pwd").style.borderColor = "red";
    //document.getElementById("new_pwd").style.borderColor = "#d3d3d3";
    //document.getElementById("confirm_pwd").style.borderColor = "#d3d3d3";
    document.getElementById("wrong_code").innerHTML = "  ";
  }
}
//---------------

</script>