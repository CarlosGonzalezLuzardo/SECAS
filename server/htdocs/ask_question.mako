<%inherit file="root.mako" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<body onload="myFunction()">

<div class="col-md-4 col-md-offset-4 header">
<h1>${title}</h1>
</div>
<div class="col-md-4 col-md-offset-4 registration_form top_form" class="block">
    <form method="post" class="login form" id="recoveryQuestionForm">
        <table>
            <tr>
                <td>${question}</td>
                <td>${question_str}</td>
            </tr>
            <tr>
                <td>${answer}</td>
                <td><input class="form-control" id="answer"type="text" name="question_ans" onkeyup='check_answer();'/></td>
                <td><input class="form-control" id="wrong_answer" type="hidden" name="wrong_answer" value="${wrong_answer}"hidden/></td>
            </tr>
        </table>
        <p style="display:inline; color:red;"  name="wrong_code" id="wrong_code" ></p>
        <div><input class="form-control" type="hidden" name="url" value="${url}"/></div>
         ## --------New Button----------------
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
// -----------My script-----------
function checkFields() {
    var answer = document.getElementById("answer").value;
    
    if( answer == "" ){
         //alert("Answer must be filled out");
         wrong_code.innerHTML = "Answer must be filled out";
         document.getElementById("answer").style.borderColor = "red";
         exit(0);
    }

    document.getElementById("recoveryQuestionForm").submit();
}


function myFunction(){
    var wrong = document.getElementById('wrong_answer');

    console.log('myFunction');
    console.log(wrong.value);
    if(wrong.value == 1){
        //alert("Wrong Answer");
        wrong_code.innerHTML = "Wrong answer";
        document.getElementById("answer").style.borderColor = "red";
    }
  }

  var check_answer = function(){
        document.getElementById("answer").style.borderColor = "#d3d3d3";
        document.getElementById("wrong_code").innerHTML = "  ";
    }
//---------------

</script>