<%inherit file="root.mako" />

<div class="header">
    <h1>${title}</h1>
</div>

<div class="login_form" class="block">
    <form action="${form_action}">
        <input type="hidden" name="query" value="${query}"/>
        <input type="hidden" name="acr_values" value="${acr}"/>
        <input type="hidden" name="username" value="${username}"/>
        <label for="totp">TOTP (Time-based One Time Password)</label>
        <input name="totp" type="text"></br>
        <input type="submit"><br/>
    </form>
</div>

<%def name="add_js()">
    <script type="text/javascript">
        $(document).ready(function() {
            bookie.login.init();
        });
    </script>
</%def>
