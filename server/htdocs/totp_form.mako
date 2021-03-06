<%inherit file="root.mako" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<body onload="myFunction()">

<div class="col-md-4 col-md-offset-4 header">
## <h1>${title}</h1>
</div>

<div class="col-md-4 col-md-offset-4 login_form top_form" class="block">
    <div class="form-group">
    <form action="${form_action}" id="form_action">
        <input type="hidden" name="query" value="${query}"/>
        <input type="hidden" name="acr_values" value="${acr}" id="acr"/>
        <input type="hidden" name="username" value="${username}"/>
        <input type="hidden" name="wrong_value" value="${wrong_value}" id="wrong_value"/>
        <label for="totp">TOTP (Time-based One Time Password)</label>
        <p>Introduce your code from Google Autenticator</p>
        <input class="form-control form-control-warning" name="totp" type="text" id="totp" pattern="[0-9]{6}" onkeyup='check_totp();' title="Code must contain 6 numbers">
        <p style="display:inline; color:red;"  name="wrong_code" id="wrong_code" ><br><br></p>
        <input class="form-control" type="hidden" name="url" id="url" value="${url}"/>
        <input class="btn btn-primary btn-lg btn-block" type="submit"><br/>
    </form>
    </div>
    <a href="${url}"><strong>Back to login page</strong></a><br>
</div>


<script>
    function myFunction(){
        var wrong_value = document.getElementById('wrong_value');
        var wrong_code = document.getElementById('wrong_code');

        wrong_code.value = "";
        console.log('myFunction');

        if(wrong_value.value == 1){
            ##alert("Wrong TOTP");
            wrong_code.innerHTML = "Wrong code<br><br>";
            document.getElementById("totp").style.borderColor = "red";
            ##window.location.href = document.getElementById('acr').value;
        }
        if(wrong_value.value == 2){
            alert("Wrong Password");
            ##window.location.href = document.getElementById('url').value;
        }
        if(wrong_value.value == 4){
            ##alert("Wrong TOTP");
            wrong_code.innerHTML = "Wrong code<br><br>";
            document.getElementById("totp").style.borderColor = "red";
            window.location.href = document.getElementById('url').value;
            alert("TOTP Authentication Failed");
            ##window.location.href = document.getElementById('acr').value;
        }
    }

    var check_totp = function(){
        document.getElementById("totp").style.borderColor = "#d3d3d3";
        document.getElementById("wrong_code").innerHTML = "<br><br>";
    }

</script>

<%def name="add_js()">
    <script type="text/javascript">
        $(document).ready(function() {
            bookie.login.init();
        });
    </script>

</%def>