<%inherit file="root.mako" />
<div class="col-md-4 col-md-offset-4 header">
    <h1><a href="/">${title}</a></h1>
</div>
<div class="col-md-4 col-md-offset-4 login_form top_form" class="block">
    <form action="${action}" method="post" class="login form">
        <input type="hidden" name="query" value="${query}"/>
        <input type="hidden" name="acr_values" value="${acr}"/>
        ## <input type="hidden" name="url" id="url" value="${url}"/>
        <table>
            <tr>
                <td>${login_title}</td>
                <td><input class="form-control" type="text" name="login" value="${login}"/></td>
            </tr>
            <tr>
                <td>${passwd_title}</td>
                <td><input class="form-control" type="password" name="password"
                value="${password}"/></td>
            </tr>
        </table>
        <input class="form-control" type="hidden" name="url" id="url" value="${url}"/>
        <div><input class="btn btn-primary btn-lg btn-block top_form" type="submit" name="form.commit"
                        value="${submit_text}"/></div>

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
</script>