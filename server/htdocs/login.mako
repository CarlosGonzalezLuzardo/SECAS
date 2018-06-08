<%inherit file="root.mako" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<body onload="myFunction()">

<div class="col-md-4 col-md-offset-4 header">
     ##<h1><a href="/">${title}</a></h1>
    <h1><font color="#428bca">${title}</font></h1>
</div>
<div class="col-md-4 col-md-offset-4 login_form top_form" class="block">
    <form action="${action}" method="post" class="login form" id="loginForm">
        <input type="hidden" name="query" value="${query}"/>
        <input type="hidden" name="acr_values" value="${acr}"/>
        ## <input type="visible" name="url" id="url" value="${url}"/>
        <table>
            <tr>
                <td>${login_title}</td>
                <td><input class="form-control" id="username" type="text" name="login" value="${login}" onkeyup='check_username();'/></td>
            </tr>
            <tr>
                <td>${passwd_title}</td>
                <td><input class="form-control" id="password" type="password" name="password" value="${password}" onkeyup='check_password();'/></td>
            </tr>
        </table>
        <p style="display:inline; color:red;"  name="wrong_code" id="wrong_code" ></p>
        <td><input class="form-control" id="wrong_value" type="hidden" name="wrong_value" value="${wrong_value}" hidden/></td>
        <input class="form-control" type="hidden" name="url" id="url" value="${url}"/>
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
    var wrong_code = document.getElementById('wrong_code');

    if(username == "" && password == ""){
        //alert("Username & Password must be filled out");
        wrong_code.innerHTML = "Username & Password must be filled out";
        document.getElementById("username").style.borderColor = "red";
        document.getElementById("password").style.borderColor = "red";
        exit(0);
    }
    if( username == "" ){
         //alert("Username must be filled out");
         wrong_code.innerHTML = "Username must be filled out";
         document.getElementById("username").style.borderColor = "red";
         exit(0);
    }
    if( password == "" ){
        //alert("Password must be filled out");
        wrong_code.innerHTML = "Password must be filled out";
        document.getElementById("password").style.borderColor = "red";
         exit(0);
    }


    document.getElementById("loginForm").submit();
}

function myFunction(){
    var wrong_value = document.getElementById('wrong_value');
    var wrong_code = document.getElementById("wrong_code");
    var read = 0;

    console.log('myFunction');
    //console.log(wrong_value.value);

    if ((sessionStorage.getItem("wrong_code_storage")) && (read == 0)) {
      // Restaura el contenido al campo de texto
      wrong_value.value = sessionStorage.getItem('wrong_code_storage');
      read = 1;
    }

    console.log("wrong_value = " + wrong_value.value);

    if (wrong_value.value != 0){
        wrong_code.innerHTML = "Unknown user or wrong password";
        console.log("read = " + read);
        if (read != 1){
            sessionStorage.setItem('wrong_code_storage', wrong_value.value);
            console.log("wrong_code_storage = " + wrong_value.value);
        }
        else{
            sessionStorage.clear();
            console.log("Clear");
        }

        if ((wrong_value.value == 1) && (read == 0)){
            ##alert("Unknown user or wrong password");
            window.location.href = document.getElementById('url').value;
        }
        if(wrong_value.value == 2){
            alert("Wrong Password");
            window.location.href = document.getElementById('url').value;
        }
        if(wrong_value.value == 3){
            wrong_code.innerHTML = "Biometric Authentication Failed";
            window.location.href = document.getElementById('url').value;
            alert("Biometric Authentication Failed");
            ##window.location.href = document.getElementById('url').value;
        }
    }
    else{
        console.log("read = " + read);
        sessionStorage.clear();
        console.log("Clear");
    }
  }


    var check_username = function(){
        document.getElementById("username").style.borderColor = "#d3d3d3";
        document.getElementById("wrong_code").innerHTML = "";
    }

    var check_password = function(){
        document.getElementById("password").style.borderColor = "#d3d3d3";
        document.getElementById("wrong_code").innerHTML = "";
    }


//---------------

</script>