<%inherit file="root.mako" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<body onload="myFunction()">

<div class="col-md-4 col-md-offset-4 header">
    <h1>${title}</h1>
</div>
<div class="form-group">
    <div class="col-md-6 col-md-offset-3 registration_form top_form" class="block">
        <form method="post" class="login form" id="registrationForm">
            <table class="registration-table">
                <tr>
                    <td  class="col-md-4">${username_title}</td>
                    <td class="col-md-8"><input class="form-control" type="text" name="username" id="username" value="${username_title_value}" onkeyup='check_username();'/></td>
                </tr>
                <tr>
                    <td class="col-md-4">${password_title}</td>
                    <td class="col-md-8"><input class="form-control" type="password" name="password" id="password" onkeyup='check_password();'/></td>
                    <td class="col-md-1"><span class="glyphicon glyphicon-ok" id="ok" type="hidden"></span></td>
                </tr>
                <tr>
                    <td class="col-md-4">${password_title2}</td>
                    <td class="col-md-8"><input class="form-control" type="password" name="password2" id="conf_password" onkeyup='check_password();'/></td>
                </tr>
                <tr>
                    <td class="col-md-4">${question_title}</td>
                    <td class="col-md-8"><input class="form-control" type="text" name="question" value="${question_title_value}" id="question" onkeyup='check_question();'/></td>
                </tr>
                <tr>
                    <td class="col-md-4">${answer_title}</td>
                    <td class="col-md-8"><input class="form-control" type="password" name="answer" id= "answer" onkeyup='check_answer();'/></td>
                    <td class="col-md-1"><span class="glyphicon glyphicon-ok" id="ok2" type="hidden"></span></td>
                </tr>
                <tr>
                    <td class="col-md-4">${answer_title2}</td>
                    <td class="col-md-8"><input class="form-control" type="password" name="answer2" id="conf_answer" onkeyup='check_answer();'/></td>
                </tr>
                <tr>
                    <td class="col-md-4">${audio_title}</td>
                    <td class="col-md-8"><input class="btn btn-secondary btn-block" type="button" name="audioButton" id="audioButton"
                            value="${audio_button}"/></td>
                </tr>
            </table>
            <input name="username_used" id="username_used" type="number" value="${username_used}" hidden>
            <div><input class="form-control" type="hidden" name="url" value="${url}"/></div>
            <input name="voice_submited" id="voice_submited" type="number" value="${voice_submited}" hidden>
            <p style="display:inline; color:red;"  name="wrong_code" id="wrong_code" ><br><br></p>

            ##<div class="submit"><input class="btn btn-primary btn-lg btn-block" type="submit" name="form.commit" value="${submit_text}"/></div>

            ## --------New Login Button
            <input class="btn btn-primary btn-lg btn-block top_form" type="button" onclick="checkFields()" value="New ${submit_text}">
            ##--------------------------

        </form>
        <a href="${url}"><strong>Back to login page</strong></a><br>
    </div>
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
        var password = document.getElementById("password").value;
        var conf_password = document.getElementById("conf_password").value;
        var question = document.getElementById("question").value;
        var answer = document.getElementById("answer").value;
        var conf_answer = document.getElementById("conf_answer").value;
        var wrong_code = document.getElementById("wrong_code");
        var submit = 1;

        if( username == "" ){
             wrong_code.innerHTML = "<br>Username must be filled out";
             document.getElementById("username").style.borderColor = "red";
             document.getElementById('username').innerHTML = 'not matching';
             submit = 0;
        }
        if( password == "" ){
            //alert("Password must be filled out");
            wrong_code.innerHTML = "<br>Password must be filled out";
             submit = 0;
        }
        if( conf_password == "" ){
            //alert("You must confirm your password");
            wrong_code.innerHTML = "<br>You must confirm your password";
             submit = 0;
        }
        if(password != conf_password){
            //alert("You must repeat correctly your password");
            wrong_code.innerHTML = "<br>You must repeat correctly your password";
             submit = 0;
        }
        if( question == "" ){
            //alert("Question must be filled out");
            wrong_code.innerHTML = "<br>Question must be filled out";
            document.getElementById("question").style.borderColor = "red";
             submit = 0;
        }
        if( answer == "" ){
            //alert("Answer must be filled out");
            wrong_code.innerHTML = "<br>Answer must be filled out";
             submit = 0;
        }
        if( conf_answer == "" ){
            //alert("You must confirm your answer");
            wrong_code.innerHTML = "<br>You must confirm your answer";
             submit = 0;
        }
        if(answer != conf_answer){
            //alert("You must repeat correctly your answer");
            wrong_code.innerHTML = "<br>You must repeat correctly your answer";
             submit = 0;
        }

        if (submit == 0) {
            //wrong_code.innerHTML = "<br>Username must be filled out";
            ////alert("Username must be filled out");
            //console.log("Username must be filled out");
            //document.getElementById("username").style.borderColor = "red";
            ////document.getElementById('username').innerHTML = 'not matching';
            return false;
        }
        else{

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
    document.getElementById('ok').style.visibility = "hidden";
    document.getElementById('ok2').style.visibility = "hidden";

    if(error.value == 1){
        //alert("Usuario ya existente");
        wrong_code.innerHTML = "<br>Username in use";
    }
    else if (error.value == 2){
        //alert("Password mismatch");
        wrong_code.innerHTML = "<br>Password mismatch";
    }
    else if (error.value == 3){
        //alert("Answer mismatch");
        wrong_code.innerHTML = "<br>Answer mismatch";
    }
    else if (error.value == 4){
        //alert("Submit a voiceprint first");
        wrong_code.innerHTML = "<br>Submit a voiceprint first";
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
var checkFields = function() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var conf_password = document.getElementById("conf_password").value;
    var question = document.getElementById("question").value;
    var answer = document.getElementById("answer").value;
    var conf_answer = document.getElementById("conf_answer").value;
    var wrong_code = document.getElementById("wrong_code");

    if( username == "" ){
         wrong_code.innerHTML = "<br>Username must be filled out";
         document.getElementById("username").style.borderColor = "red";
         document.getElementById('username').innerHTML = 'not matching';
         exit(0);
    }
    if( password == "" ){
        //alert("Password must be filled out");
        wrong_code.innerHTML = "<br>Password must be filled out";
         exit(0);
    }
    if( conf_password == "" ){
        //alert("You must confirm your password");
        wrong_code.innerHTML = "<br>You must confirm your password";
         exit(0);
    }
    if(password != conf_password){
        //alert("You must repeat correctly your password");
        wrong_code.innerHTML = "<br>You must repeat correctly your password";
         exit(0);
    }
    if( question == "" ){
        //alert("Question must be filled out");
        wrong_code.innerHTML = "<br>Question must be filled out";
         exit(0);
    }
    if( answer == "" ){
        //alert("Answer must be filled out");
        wrong_code.innerHTML = "<br>Answer must be filled out";
         exit(0);
    }
    if( conf_answer == "" ){
        //alert("You must confirm your answer");
        wrong_code.innerHTML = "<br>You must confirm your answer";
         exit(0);
    }
    if(answer != conf_answer){
        //alert("You must repeat correctly your answer");
        wrong_code.innerHTML = "<br>You must repeat correctly your answer";
         exit(0);
    }

    document.getElementById("registrationForm").submit();
}


var check_password = function() {
  if ((document.getElementById('password').value ==
    document.getElementById('conf_password').value) &&  (document.getElementById('password').value != "")){
    document.getElementById('password').style.color = 'green';
    document.getElementById('password').innerHTML = 'matching';
    document.getElementById('conf_password').style.color = 'green';
    document.getElementById('conf_password').innerHTML = 'matching';
    document.getElementById('ok').style.visibility = "visible";
    document.getElementById('ok').style.color = "green"
    document.getElementById("password").style.borderColor = "green";
    document.getElementById("conf_password").style.borderColor = "green";
    document.getElementById("wrong_code").innerHTML = "<br><br>";
  } else {
    document.getElementById('password').style.color = 'red';
    document.getElementById('password').innerHTML = 'not matching';
    document.getElementById('conf_password').style.color = 'red';
    document.getElementById('conf_password').innerHTML = 'not matching';
    document.getElementById('ok').style.visibility = "hidden";
    document.getElementById("password").style.borderColor = "red";
    document.getElementById("conf_password").style.borderColor = "red";
  }
}

var check_answer = function() {
  if ((document.getElementById('answer').value ==
    document.getElementById('conf_answer').value) &&  (document.getElementById('answer').value != "")) {
    document.getElementById('answer').style.color = 'green';
    document.getElementById('answer').innerHTML = 'matching';
    document.getElementById('conf_answer').style.color = 'green';
    document.getElementById('conf_answer').innerHTML = 'matching';
    document.getElementById('ok2').style.visibility = "visible";
    document.getElementById('ok2').style.color = "green"
    document.getElementById("answer").style.borderColor = "green";
    document.getElementById("conf_answer").style.borderColor = "green";
    document.getElementById("wrong_code").innerHTML = "<br><br>";
  } else {
    document.getElementById('answer').style.color = 'red';
    document.getElementById('answer').innerHTML = 'not matching';
    document.getElementById('conf_answer').style.color = 'red';
    document.getElementById('conf_answer').innerHTML = 'not matching';
    document.getElementById('ok2').style.visibility = "hidden";
    document.getElementById("answer").style.borderColor = "red";
    document.getElementById("conf_answer").style.borderColor = "red";
  }
}

var check_username = function(){
        document.getElementById("username").style.borderColor = "#d3d3d3";
        document.getElementById("wrong_code").innerHTML = "<br><br>";
}

var check_question = function(){
        document.getElementById("question").style.borderColor = "#d3d3d3";
        document.getElementById("wrong_code").innerHTML = "<br><br>";
}

//---------------

</script>