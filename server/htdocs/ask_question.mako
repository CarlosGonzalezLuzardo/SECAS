<%inherit file="root.mako" />

<div class="col-md-4 col-md-offset-4 header">
<h1>${title}</h1>
</div>
<div class="col-md-4 col-md-offset-4 registration_form top_form" class="block">
    <form method="post" class="login form" id="recoveryQuestionForm">
        <table>
            <tr>
                <td>${question}${question_str}</td>
            </tr>
            <tr>
                <td>${answer}</td>
                <td><input class="form-control" id="answer"type="text" name="question_ans"/></td>
            </tr>
        </table>
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
         alert("Answer must be filled out");
         exit(0);
    }

    document.getElementById("recoveryQuestionForm").submit();
}
//---------------

</script>