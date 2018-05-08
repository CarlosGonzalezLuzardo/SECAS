<%inherit file="root.mako" />

<body onload="myFunction()">

<div class="col-md-4 col-md-offset-4 header">
    <h1>${title}</h1>
</div>
<div class="col-md-6 col-md-offset-3 registration_form top_form" class="block">
    <form method="post" class="login form" id="registrationForm">
        <table class="registration-table">
            <tr>
                <td  class="col-md-4">${username_title}</td>
                <td class="col-md-8"><input class="form-control" type="text" name="username" id="username" value="${username_title_value}"/></td>
            </tr>
            <tr>
                <td class="col-md-4">${password_title}</td>
                <td class="col-md-8"><input class="form-control" type="password" name="password" id="password"/></td>
            </tr>
            <tr>
                <td class="col-md-4">${password_title2}</td>
                <td class="col-md-8"><input class="form-control" type="password" name="password2" id="conf_password"/></td>
            </tr>
            <tr>
                <td class="col-md-4">${question_title}</td>
                <td class="col-md-8"><input class="form-control" type="text" name="question" value="${question_title_value}" id="question"/></td>
            </tr>
            <tr>
                <td class="col-md-4">${answer_title}</td>
                <td class="col-md-8"><input class="form-control" type="password" name="answer" id= "answer"/></td>
            </tr>
            <tr>
                <td class="col-md-4">${answer_title2}</td>
                <td class="col-md-8"><input class="form-control" type="password" name="answer2" id="conf_answer"/></td>
            </tr>
            <tr>
                <td class="col-md-4">${audio_title}</td>
                <td class="col-md-8"><input class="btn btn-secondary btn-block" type="button" name="audioButton" id="audioButton"
                        value="${audio_button}"/></td>
            </tr>
        </table>
        <input name="username_used" id="username_used" type="number" value="${username_used}" hidden>
        <div><input class="form-control" type="hidden" name="url" value="${url}"/></div>
        ##<div class="submit"><input class="btn btn-primary btn-lg btn-block" type="submit" name="form.commit" value="${submit_text}"/></div>

        ## --------New Login Button
        <input class="btn btn-primary btn-lg btn-block top_form" type="button" onclick="checkFields()" value="New ${submit_text}">
        ##--------------------------

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

            var childWin = window.open(url, "Voiceprint enrollment", "width=500,height=350");
            return false;
        }
  });

  function myFunction(){
    var error = document.getElementById('username_used');

    if(error.value == 1){
        alert("Usuario ya existente");
    }
    else if (error.value == 2){
        alert("Password mismatch");
    }
    else if (error.value == 3){
        alert("Answer mismatch");
    }
  }

  function shenanigans(val1){
##       shenanigans
      if (val1) {
          successes+=1;
          console.log(successes);
      }
  }
</script>



<script>
// -----------My script-----------
function checkFields() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var conf_password = document.getElementById("conf_password").value;
    var question = document.getElementById("question").value;
    var answer = document.getElementById("answer").value;
    var conf_answer = document.getElementById("conf_answer").value;

    if( username == "" ){
         alert("Username must be filled out");
         exit(0);
    }
    if( password == "" ){
        alert("Password must be filled out");
         exit(0);
    }
    if( conf_password == "" ){
        alert("You must confirm your password");
         exit(0);
    }
    if(password != conf_password){
        alert("You must repeat correctly your password");
         exit(0);
    }
    if( question == "" ){
        alert("Question must be filled out");
         exit(0);
    }
    if( answer == "" ){
        alert("Answer must be filled out");
         exit(0);
    }
    if( conf_answer == "" ){
        alert("You must confirm your answer");
         exit(0);
    }
    if(answer != conf_answer){
        alert("You must repeat correctly your answer");
         exit(0);
    }

    document.getElementById("registrationForm").submit();
}
//---------------

</script>