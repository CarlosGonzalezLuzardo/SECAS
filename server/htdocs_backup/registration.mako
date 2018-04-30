<%inherit file="root.mako" />

<div class="header">
    <h1>${title}</h1>
</div>
<div class="registration_form" class="block">
    <form method="post" class="login form">
        <table>
            <tr>
                <td>${username_title}</td>
                <td><input type="text" name="username" id="username" /></td>
            </tr>
            <tr>
                <td>${password_title}</td>
                <td><input type="password" name="password"/></td>
            </tr>
            <tr>
                <td>${password_title2}</td>
                <td><input type="password" name="password2"/></td>
            </tr>
            <tr>
                <td>${question_title}</td>
                <td><input type="text" name="question"/></td>
            </tr>
            <tr>
                <td>${answer_title}</td>
                <td><input type="password" name="answer"/></td>
            </tr>
            <tr>
                <td>${answer_title2}</td>
                <td><input type="password" name="answer2"/></td>
            </tr>
            <tr>
                <td>${audio_title}</td>
                <td><input type="button" name="audioButton" id="audioButton"
                        value=${audio_button}/></td>
            </tr>
            <tr>
                <td><input type="submit" name="form.commit"
                        value="${submit_text}"/></td>
            </tr>
        </table>
    </form>
</div>

<%def name="add_js()">
    <script type="text/javascript">
        $(document).ready(function() {
            bookie.login.init();
        });
    </script>
</%def>
<script>

  var audioButton = document.getElementById('audioButton');

  var successes = 0;

  audioButton.addEventListener('click', function() {
        var username = document.getElementById('username').value;

        if (username == "") {
            alert("Username must be filled out");
            console.log("Username must be filled out");
            return false;
        }else{

            if (successes>=3){
                return true;
            }

            var url = "biom_enroll?id=" + username;

            var childWin = window.open(url, "Voiceprint enrollment", "width=400,height=250");
            return false;
        }
  });

  function shenanigans(val1){
##       shenanigans
      if (val1) {
          successes+=1;
          console.log(successes);
      }
  }
</script>