<%inherit file="root.mako" />
<body onload="myFunction()">

<div class="col-md-4 col-md-offset-4 header">
## <h1>${title}</h1>
</div>

<div class="col-md-4 col-md-offset-4 login_form top_form" class="block">
    <form action="${form_action}" id="form_action">
        <input type="visible" name="query" value="${query}"/>
        <input type="visible" name="acr_values" value="${acr}" id="acr"/>
        <input type="visible" name="username" value="${username}"/>
        <input type="visible" name="wrong_value" value="${wrong_value}" id="wrong_value"/>
        <label for="totp">TOTP (Time-based One Time Password)</label>
        <p>Introduce your code from Google Autenticator</p>
        <input class="form-control" name="totp" type="text"></br>
        <input class="form-control" type="hidden" name="url" id="url" value="${url}"/>
        <input class="btn btn-primary btn-lg btn-block" type="submit"><br/>
    </form>
    <a href="${url}"><strong>Back to login page</strong></a><br>
</div>


<script>
function myFunction(){
    var wrong_value = document.getElementById('wrong_value');

    console.log('myFunction');

    if(wrong_value.value == 1){
        alert("Wrong TOTP");
        ##window.location.href = document.getElementById('acr').value;
    }
    if(wrong_value.value == 2){
        alert("Wrong Password");
        ##window.location.href = document.getElementById('url').value;
    }
}
</script>

<%def name="add_js()">
    <script type="text/javascript">
        $(document).ready(function() {
            bookie.login.init();
        });
    </script>

</%def>