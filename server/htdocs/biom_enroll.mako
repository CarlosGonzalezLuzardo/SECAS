<%inherit file="root.mako" />

<body onload="myFunction()">
<div class="header">
    <h1>${title}</h1>

</div>
<div class="voiceForm" class="block">

    <p>${file_label}</p>
    <p>
        <input type="file" accept="audio/*" capture="microphone" id="recorder"><br>
        <audio id="player" controls></audio>
    </p>
    <form name="biom" id="biom" action="${action}" class="login form" method="post"
    >
        <table>
            <input type="visible" name="username" value="${username}"/>
            <input name="thefile" id="thefile" type="text" value='' visible>
            <input name="nsuccess" id="nsuccess" type="number" value="${nsuccess}" visible>
            <input name="nfailures" id="nfailures" type="number" value="${nfailures}" visible>
            <tr>
                <td>${button_label}</td>
                <td><input type="submit" value=${submit_text} /></td>
            </tr>
        </table>
    </form>
</div>

<script type="text/javascript">
    function validateForm() {
        var recorder = document.getElementById('recorder');

        var reader  = new FileReader();

        reader.onload = (function()
        { return function(e)
            {
                var myform = document.getElementById('thefile');
                myform.value = window.btoa(e.target.result);
                console.log('Voiceprint ready to submit');
            };
        })();

        reader.readAsDataURL(recorder.files[0]);

        filename = recorder.value;
        if (filename == "") {
            alert("Name must be filled out");
            return false;
        }
    }
</script>

<script>

  var recorder = document.getElementById('recorder');
  var player = document.getElementById('player');

  recorder.addEventListener('change', function(e) {
    var file = e.target.files[0];
    // Preparing the audio file.
      validateForm();

    player.src =  URL.createObjectURL(file);
    console.log(player.src);
  });

  function OKClicked(){
      window.opener.shenanigans(true);
  }

  function myFunction(){
    var failures = document.getElementById('nfailures');
    var success = document.getElementById('nsuccess');

    if(failures.value == 4){
        alert("Usuario ya existente");
        window.close();
    }
    if(success.value == 3){
        alert("Archivos subidos correctamente");
        window.close();
    }
  }
</script>


<%def name="add_js()">
    <script type="text/javascript">
        $(document).ready(function() {
            bookie.login.init();
        });
    </script>

</%def>
