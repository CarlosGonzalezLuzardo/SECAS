<%inherit file="root.mako" />

<div class="col-md-4 col-md-offset-4 header">
## <h1>${title}</h1>
</div>

<div class="col-md-4 col-md-offset-4 login_form top_form" class="block">
    <form action="${form_action}">
        <input type="hidden" name="query" value="${query}"/>
        <input type="hidden" name="acr_values" value="${acr}"/>
        <input type="hidden" name="username" value="${username}"/>
        <label for="totp">TOTP (Time-based One Time Password)</label>
        <p>Introduce your code from Google Autenticator</p>
        <input class="form-control" name="totp" type="text"></br>
        <input class="form-control" type="hidden" name="url" id="url" value="${url}"/>
        <input class="btn btn-primary btn-lg btn-block" type="submit"><br/>
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