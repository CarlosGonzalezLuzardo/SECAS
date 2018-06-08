<%inherit file="root.mako" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<body onload="myFunction()">

<!--

<div class="col-md-4 col-md-offset-4 header">
    <h1>${title}</h1>
</div>
<div class="col-md-4 col-md-offset-4 login_form top_form" class="block">
    <p>You must introduce a different file than others you have already added</p>
    <p>${file_label}</p>
    <p>
    <input class="form-control" type="file" accept="audio/*" capture="microphone" id="recorder"><br>
    <audio id="player" controls></audio>
    </p>
    <form name="biom" id="biom" action="${action}" class="login form" method="post"
    >
        <table>
            <input type="hidden" name="username" value="${username}"/>
            <input name="thefile" id="thefile" type="text" value='' hidden>
        </table>
        <p>${button_label}</p>
        <div><input class="btn btn-primary btn-lg btn-block" type="submit" value=${submit_text} /></div>

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

</script>


<%def name="add_js()">
    <script type="text/javascript">
        $(document).ready(function() {
            bookie.login.init();
        });
    </script>

</%def>
//-->

## <!DOCTYPE html>
## <html>
##     <head>
##         <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
##         <script src="/static/recorder.js"></script>
##         <title>Live input record and playback</title>
##         <style type='text/css'>
##             ul {
##                 list-style: none;
##             }

##             #recordingslist audio {
##                 display: block;
##                 margin-bottom: 10px;
##             }
##         </style>
##     </head>
## <body>

    ## <%inherit file="root.mako" />

    <div class="col-md-4 col-md-offset-4 header">
        <h1>${title}</h1>
        <script src="/static/recorder.js"></script>
        <script src="/static/main.js"></script>
    </div>
    <div class="col-md-4 col-md-offset-4 login_form top_form" class="block">
        <p>You must introduce a different file than others you have already added</p>
        <p>${file_label}</p>
        <p>
            <button type="button" class="btn btn-success" id="start-btn"><span class="glyphicon glyphicon-record"></span> Start recording</button>
            <button type="button" class="btn btn-danger" id="stop-btn" ><span class="glyphicon glyphicon-stop"></span> Stop recording</button>
        </p>
        <audio id="player2" controls></audio>

        <form name="biom2" id="biom2" action="${action}" class="login form" method="post">
            <table>
                <input type="text" name="username" value="${username}" id="username" hidden/>
                <input name="thefile2" id="thefile2" type="text" value="${thefile2}" hidden />
                <input class="form-control" type="hidden" name="url" id="url" value="${url}"/>
                <input type="text" name="wrong_value" value="${wrong_value}" id="wrong_value" hidden/>
                <ul id="recordingslist"></ul>
            </table>
            <p>${button_label}</p>
            <p style="display:inline; color:red;"  name="wrong_code" id="wrong_code" ></p>
        ## --------New Login Button
            <input class="btn btn-primary btn-lg btn-block top_form" type="button" onclick="checkFields()" value="New ${submit_text}">
        ##--------------------------
        </form>
        <a href="${url}"><strong>BACK</strong></a><br>
    </div>




    <script>
        // Expose globally your audio_context, the recorder instance and audio_stream
        var audio_context;
        var recorder;
        var audio_stream;

        /**
         * Patch the APIs for every browser that supports them and check
         * if getUserMedia is supported on the browser.
         *
         */
        function Initialize() {
            try {
                // Monkeypatch for AudioContext, getUserMedia and URL
                window.AudioContext = window.AudioContext || window.webkitAudioContext;
                navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia;
                window.URL = window.URL || window.webkitURL;

                // Store the instance of AudioContext globally
                audio_context = new AudioContext;
                document.getElementById("stop-btn").disabled = true;
                console.log('Audio context is ready !');
                console.log('navigator.getUserMedia ' + (navigator.getUserMedia ? 'available.' : 'not present!'));
            } catch (e) {
                alert('No web audio support in this browser!');
            }
        }

        /**
         * Starts the recording process by requesting the access to the microphone.
         * Then, if granted proceed to initialize the library and store the stream.
         *
         * It only stops when the method stopRecording is triggered.
         */
        function startRecording() {
            // Access the Microphone using the navigator.getUserMedia method to obtain a stream
            navigator.getUserMedia({ audio: true }, function (stream) {
                // Expose the stream to be accessible globally
                audio_stream = stream;
                // Create the MediaStreamSource for the Recorder library
                var input = audio_context.createMediaStreamSource(stream);
                console.log('Media stream succesfully created');

                // Initialize the Recorder Library
                recorder = new Recorder(input, { numChannels: 1, sampleRate: 8000 });
                console.log('Recorder initialised');

                // Start recording !
                recorder && recorder.record();
                console.log('Recording...');

                // Disable Record button and enable stop button !
                document.getElementById("start-btn").disabled = true;
                document.getElementById("stop-btn").disabled = false;
            }, function (e) {
                console.error('No live audio input: ' + e);
            });
        }

        /**
         * Stops the recording process. The method expects a callback as first
         * argument (function) executed once the AudioBlob is generated and it
         * receives the same Blob as first argument. The second argument is
         * optional and specifies the format to export the blob either wav or mp3
         */
        function stopRecording(callback, AudioFormat) {
            console.log("AudioFormat: "+AudioFormat);
            // Stop the recorder instance
            recorder && recorder.stop();
            console.log('Stopped recording.');

            // Stop the getUserMedia Audio Stream !
            audio_stream.getAudioTracks()[0].stop();

            // Disable Stop button and enable Record button !
            document.getElementById("start-btn").disabled = false;
            document.getElementById("stop-btn").disabled = true;

            // Use the Recorder Library to export the recorder Audio as a .wav file
            // The callback providen in the stop recording method receives the blob
            if(typeof(callback) == "function"){

                /**
                 * Export the AudioBLOB using the exportWAV method.
                 * Note that this method exports too with mp3 if
                 * you provide the second argument of the function
                 */
                recorder && recorder.exportWAV(function (blob) {
                    callback(blob);
                    // create WAV download link using audio data blob
                    // createDownloadLink();

                    // Clear the Recorder to start again !
                    recorder.clear();
                }, (AudioFormat || "audio/wav"));
            }
        }

        // Initialize everything once the window loads
        window.onload = function(){

            var wrong_value = document.getElementById('wrong_value');

            console.log('myFunction');

            if(wrong_value.value == 1){
                ##window.location.href = document.getElementById('url').value;
                ##alert("Voice not recognized");
                wrong_code.innerHTML = "Voice not recognized";
            }
            if(wrong_value.value == 3){
                window.location.href = document.getElementById('url').value;
                alert("Biometric Authentication Failed");
                ##window.location.href = document.getElementById('url').value;
            }
            // Prepare and check if requirements are filled
            Initialize();

            // Handle on start recording button
            document.getElementById("start-btn").addEventListener("click", function(){
                startRecording();
            }, false);

            // Handle on stop recording button
            document.getElementById("stop-btn").addEventListener("click", function(){
                // Use wav format
                var _AudioFormat = "audio/wav";
                // You can use mp3 to using the correct mimetype
                //var AudioFormat = "audio/mpeg";

                stopRecording(function(AudioBLOB){
                    // Note:
                    // Use the AudioBLOB for whatever you need, to download
                    // directly in the browser, to upload to the server, you name it !

                    // In this case we are going to add an Audio item to the list so you
                    // can play every stored Audio
                    var url = URL.createObjectURL(AudioBLOB);

                    //var li = document.createElement('li');
                    var au = document.getElementById('player2');

                    au.controls = true;
                    au.src = url;
                    //hf.href = url;
                    // Important:
                    // Change the format of the file according to the mimetype
                    // e.g for audio/wav the extension is .wav
                    //     for audio/mpeg (mp3) the extension is .mp3
                    //hf.download = new Date().toISOString() + '.wav';
                    //hf.innerHTML = hf.download;
                    ////li.appendChild(au);
                    //li.appendChild(hf);
                    ////recordingslist.appendChild(li);
                    var reader2  = new FileReader();

                    reader2.onload = (function()
                    { return function(e)
                        {
                            var myform = document.getElementById('thefile2');
                            myform.value = '';
                            myform.value = window.btoa(e.target.result);
                            console.log('Voiceprint ready to submit');
                        };
                    })();

                    reader2.readAsDataURL(AudioBLOB);

                }, _AudioFormat);
                document.getElementById("start-btn").disabled = false;

            }, false);
        };


        function checkFields() {
        var file2 = document.getElementById('thefile2');
        var username = document.getElementById('username').value;

        console.log('checkFields');
        if(file2.value == ''){
            alert("No voice record found");
        }
        else {
            //var url = "biom_form?id=" + username;
            //var childWin = window.open(url, "Voiceprint enrollment", "width=500,height=350");
            document.getElementById("biom2").submit();
        }


        }


        function myFunction(){
        var wrong_value = document.getElementById('wrong_value');

        console.log('myFunction');

        if(wrong_value.value == 1){
            window.location.href = document.getElementById('url').value;
            alert("Voice not recognized");
        }
        if(wrong_value.value == 3){
            window.location.href = document.getElementById('url').value;
            alert("Biometric Authentication Failed");
            ##window.location.href = document.getElementById('url').value;
        }
         }

    </script>

    <!-- Include the recorder.js library from a local copy -->
    <!-- <script src="recorder.js"></script> -->
## </body>
## </html>