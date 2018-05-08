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
                <td><input class="form-control" id="new_pwd" type="password" name="password"/></td>
            </tr>
            <tr>
                <td>${newpassword_title}</td>
                <td><input class="form-control" id="confirm_pwd" type="password" name="newpassword"/></td>
            </tr>
        </table>
            <div><input class="form-control" type="hidden" name="url" value="${url}"/></div>
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

    if( new_pwd == "" && confirm_pwd == ""){
         alert("Your password fields must be filled out");
         exit(0);
    }
    if( new_pwd == "" ){
         alert("You have to choose a new password");
         exit(0);
    }
    if( confirm_pwd == "" ){
         alert("You have to confirm your new password");
         exit(0);
    }
    if( new_pwd != confirm_pwd){
        alert("Fields must have the same value!");
        exit(0);
    }

    document.getElementById("recoveryNewpwdForm").submit();
}
//---------------

</script>