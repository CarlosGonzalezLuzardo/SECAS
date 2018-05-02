
<%inherit file="root.mako" />

<h1 class="col-md-4 col-md-offset-4 header">Updating TOTP</h1>
<div class="col-md-8 col-md-offset-2 login_form">
    <h2>Name</h2>
    <div class="user-name"  name="username" id="username">${username}</div>
    <h2>Two-factor authentication</h2>
    <p>Insert this code (${totp_secret}) or scan the following QR code in your two-factor authentication app (ie. Google Authenticator).</p>
    <p><img src="data:image/png;base64,${qr_blob}"/></p>
    ## <input class="btn btn-secondary btn-block" type="button" name="back" id="back" value=${home_uri}/>
    % if home_uri:
        <a href="${home_uri}"><strong>BACK</strong></a><br>
    % endif
</div>