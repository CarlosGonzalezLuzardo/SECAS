<%inherit file="root.mako" />
<body onload="myFunction()">

<div class="col-md-4 col-md-offset-4 header">
     ##<h1><a href="/">${title}</a></h1>
    <h1><font color="#428bca">${title}</font></h1>
</div>
<div class="col-md-4 col-md-offset-4 login_form top_form" class="block">
    <form action="${action}" method="post" class="login form" id="loginForm">
        <input type="visible" name="query" value="${query}"/>
        <input type="visible" name="acr_values" value="${acr}"/>
        ## <input type="visible" name="url" id="url" value="${url}"/>
        <table>
            <tr>
                <td>${login_title}</td>
                <td><input class="form-control" id="username" type="text" name="login" value="${login}"/></td>
            </tr>
            <tr>
                <td>${passwd_title}</td>
                <td><input class="form-control" id="password" type="password" name="password" value="${password}"/></td>
            </tr>
        </table>
        <td><input class="form-control" id="wrong_value" type="number" name="wrong_value" value="${wrong_value}" visible/></td>
        <input class="form-control" type="visible" name="url" id="url" value="${url}"/>
        ## --------New Login Button
            <input class="btn btn-primary btn-lg btn-block top_form" type="button" onclick="checkFields()" value="New ${submit_text}">
             ##<input name="username_used" id="username_used" type="number" value="${username_used}" visible>
        ##--------------------------
    </form>
    % if logo_uri:
        <img src="${logo_uri}" alt="Client logo">
    % endif
    % if policy_uri:
        <a href="${policy_uri}"><strong>Client&#39;s Policy</strong></a>
    % endif
    % if tos_uri:
        <a href="${tos_uri}"><strong>Client&#39;s Terms of Service</strong></a><br>
    % endif
    ## % if recover_uri:
    ##     <form action="${recover_uri}" method="post" class="login form">
    ##         <input class="form-control" type="text" id="url" value="${url}"/>
    ##         <input class="btn btn-primary btn-lg btn-block top_form" type="submit" name="form.commit"
    ##                     value="Forgot your password?"/>
    ##     </form>
    ## % endif
    % if recover_uri:
        <a href="${recover_uri}"><strong>Forgot your password?</strong></a><br>
    % endif
    % if register_uri:
        <a href="${register_uri}"><strong>New user?</strong></a><br>
    % endif
</div>

<%def name="add_js()">
    <script type="text/javascript">
        $(document).ready(function() {
            bookie.login.init();
        });
    </script>
</%def>

<script>
    var URLactual = window.location;
    //document.getElementById("url").value = URLactual;
    //console.log("URLLLLLLLLLLLLLLLLLLLL: "+ document.getElementById('url').value);

// -----------My script-----------
function checkFields() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    //var error = document.getElementById('username_used');
    
    if(username == "" && password == ""){
        alert("Username & Password must be filled out");
        exit(0);
    }
    if( username == "" ){
         alert("Username must be filled out");
         exit(0);
    }
    if( password == "" ){
        alert("Password must be filled out");
         exit(0);
    }


    document.getElementById("loginForm").submit();
}

function myFunction(){
    var wrong_value = document.getElementById('wrong_value');

    console.log('myFunction');
    console.log(wrong_value.value);
    if(wrong_value.value == 1){
        alert("Unknown user or wrong password");
        window.location.href = document.getElementById('url').value;
    }
    if(wrong_value.value == 2){
        alert("Wrong Password");
        window.location.href = document.getElementById('url').value;
    }
    if(wrong_value.value == 3){
        window.location.href = document.getElementById('url').value;
        alert("Biometric Authentication Failed");
        ##window.location.href = document.getElementById('url').value;
    }
  }

//---------------

</script>