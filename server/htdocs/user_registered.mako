<%inherit file="root.mako" />

<h1>User registered</h1>
<h2>Name</h2>
${username}
<h2>Two-factor authentication</h2>
<p>Insert this code (${totp_secret}) or scan the following QR code in your two-factor authentication app (ie. Google Authenticator).</p>
<p><img src="data:image/png;base64,${qr_blob}"/></p>
##% if login:
##        <a href="${login}"><strong>New user?</strong></a><br>
##% endif
