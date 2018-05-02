# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1525278337.3872156
_enable_loop = True
_template_filename = 'htdocs/biom_form.mako'
_template_uri = 'biom_form.mako'
_source_encoding = 'utf-8'
_exports = ['add_js']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'root.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        url = context.get('url', UNDEFINED)
        action = context.get('action', UNDEFINED)
        button_label = context.get('button_label', UNDEFINED)
        title = context.get('title', UNDEFINED)
        submit_text = context.get('submit_text', UNDEFINED)
        file_label = context.get('file_label', UNDEFINED)
        username = context.get('username', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="col-md-4 col-md-offset-4 header">\n    <h1>')
        __M_writer(str(title))
        __M_writer('</h1>\n</div>\n<div class="col-md-4 col-md-offset-4 login_form top_form" class="block">\n    <p>You must introduce a different file than others you have already added</p>\n    <p>')
        __M_writer(str(file_label))
        __M_writer('</p>\n    <p>\n    <input class="form-control" type="file" accept="audio/*" capture="microphone" id="recorder"><br>\n    <audio id="player" controls></audio>\n    </p>\n    <form name="biom" id="biom" action="')
        __M_writer(str(action))
        __M_writer('" class="login form" method="post"\n    >\n        <table>\n            <input type="hidden" name="username" value="')
        __M_writer(str(username))
        __M_writer('"/>\n            <input name="thefile" id="thefile" type="text" value=\'\' hidden>\n        </table>\n        <p>')
        __M_writer(str(button_label))
        __M_writer('</p>\n        <div><input class="btn btn-primary btn-lg btn-block" type="submit" value=')
        __M_writer(str(submit_text))
        __M_writer(' /></div>\n\n    </form>\n</div>\n\n<script type="text/javascript">\n    function validateForm() {\n        var recorder = document.getElementById(\'recorder\');\n\n        var reader  = new FileReader();\n\n        reader.onload = (function()\n        { return function(e)\n            {\n                var myform = document.getElementById(\'thefile\');\n                myform.value = window.btoa(e.target.result);\n                console.log(\'Voiceprint ready to submit\');\n            };\n        })();\n\n        reader.readAsDataURL(recorder.files[0]);\n\n        filename = recorder.value;\n        if (filename == "") {\n            alert("Name must be filled out");\n            return false;\n        }\n    }\n</script>\n\n<script>\n\n  var recorder = document.getElementById(\'recorder\');\n  var player = document.getElementById(\'player\');\n\n  recorder.addEventListener(\'change\', function(e) {\n    var file = e.target.files[0];\n    // Preparing the audio file.\n      validateForm();\n\n    player.src =  URL.createObjectURL(file);\n    console.log(player.src);\n  });\n\n</script>\n\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n    <div class="col-md-4 col-md-offset-4 header">\n        <h1>')
        __M_writer(str(title))
        __M_writer('</h1>\n    </div>\n    <div class="col-md-4 col-md-offset-4 login_form top_form" class="block">\n        <p>You must introduce a different file than others you have already added</p>\n        <p>')
        __M_writer(str(file_label))
        __M_writer('</p>\n        <p>\n            <button type="button" class="btn btn-success" id="start-btn"><span class="glyphicon glyphicon-record"></span> Start recording</button>\n            <button type="button" class="btn btn-danger" id="stop-btn" ><span class="glyphicon glyphicon-stop"></span> Stop recording</button>\n        </p>\n        <form name="biom" id="biom" action="')
        __M_writer(str(action))
        __M_writer('" class="login form" method="post">\n            <table>\n                <input type="hidden" name="username" value="')
        __M_writer(str(username))
        __M_writer('"/>\n                <input name="thefile" id="thefile" type="text" value=\'\' hidden>\n                <ul id="recordingslist"></ul>\n            </table>\n            <p>')
        __M_writer(str(button_label))
        __M_writer('</p>\n            <div><input class="btn btn-primary btn-lg btn-block" type="submit" value=')
        __M_writer(str(submit_text))
        __M_writer(' /></div>\n\n        </form>\n        <a href="')
        __M_writer(str(url))
        __M_writer('"><strong>BACK</strong></a><br>\n    </div>\n\n    <script>\n        // Expose globally your audio_context, the recorder instance and audio_stream\n        var audio_context;\n        var recorder;\n        var audio_stream;\n\n        /**\n         * Patch the APIs for every browser that supports them and check\n         * if getUserMedia is supported on the browser.\n         *\n         */\n        function Initialize() {\n            try {\n                // Monkeypatch for AudioContext, getUserMedia and URL\n                window.AudioContext = window.AudioContext || window.webkitAudioContext;\n                navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia;\n                window.URL = window.URL || window.webkitURL;\n\n                // Store the instance of AudioContext globally\n                audio_context = new AudioContext;\n                document.getElementById("stop-btn").disabled = true;\n                console.log(\'Audio context is ready !\');\n                console.log(\'navigator.getUserMedia \' + (navigator.getUserMedia ? \'available.\' : \'not present!\'));\n            } catch (e) {\n                alert(\'No web audio support in this browser!\');\n            }\n        }\n\n        /**\n         * Starts the recording process by requesting the access to the microphone.\n         * Then, if granted proceed to initialize the library and store the stream.\n         *\n         * It only stops when the method stopRecording is triggered.\n         */\n        function startRecording() {\n            // Access the Microphone using the navigator.getUserMedia method to obtain a stream\n            navigator.getUserMedia({ audio: true }, function (stream) {\n                // Expose the stream to be accessible globally\n                audio_stream = stream;\n                // Create the MediaStreamSource for the Recorder library\n                var input = audio_context.createMediaStreamSource(stream);\n                console.log(\'Media stream succesfully created\');\n\n                // Initialize the Recorder Library\n                recorder = new Recorder(input, { numChannels: 1, sampleRate: 8000 });\n                console.log(\'Recorder initialised\');\n\n                // Start recording !\n                recorder && recorder.record();\n                console.log(\'Recording...\');\n\n                // Disable Record button and enable stop button !\n                document.getElementById("start-btn").disabled = true;\n                document.getElementById("stop-btn").disabled = false;\n            }, function (e) {\n                console.error(\'No live audio input: \' + e);\n            });\n        }\n\n        /**\n         * Stops the recording process. The method expects a callback as first\n         * argument (function) executed once the AudioBlob is generated and it\n         * receives the same Blob as first argument. The second argument is\n         * optional and specifies the format to export the blob either wav or mp3\n         */\n        function stopRecording(callback, AudioFormat) {\n            console.log("AudioFormat: "+AudioFormat);\n            // Stop the recorder instance\n            recorder && recorder.stop();\n            console.log(\'Stopped recording.\');\n\n            // Stop the getUserMedia Audio Stream !\n            audio_stream.getAudioTracks()[0].stop();\n\n            // Disable Stop button and enable Record button !\n            document.getElementById("start-btn").disabled = true;\n            document.getElementById("stop-btn").disabled = true;\n\n            // Use the Recorder Library to export the recorder Audio as a .wav file\n            // The callback providen in the stop recording method receives the blob\n            if(typeof(callback) == "function"){\n\n                /**\n                 * Export the AudioBLOB using the exportWAV method.\n                 * Note that this method exports too with mp3 if\n                 * you provide the second argument of the function\n                 */\n                recorder && recorder.exportWAV(function (blob) {\n                    callback(blob);\n                    // create WAV download link using audio data blob\n                    // createDownloadLink();\n\n                    // Clear the Recorder to start again !\n                    recorder.clear();\n                }, (AudioFormat || "audio/wav"));\n            }\n        }\n\n        // Initialize everything once the window loads\n        window.onload = function(){\n            // Prepare and check if requirements are filled\n            Initialize();\n\n            // Handle on start recording button\n            document.getElementById("start-btn").addEventListener("click", function(){\n                startRecording();\n            }, false);\n\n            // Handle on stop recording button\n            document.getElementById("stop-btn").addEventListener("click", function(){\n                // Use wav format\n                var _AudioFormat = "audio/wav";\n                // You can use mp3 to using the correct mimetype\n                //var AudioFormat = "audio/mpeg";\n\n                stopRecording(function(AudioBLOB){\n                    // Note:\n                    // Use the AudioBLOB for whatever you need, to download\n                    // directly in the browser, to upload to the server, you name it !\n\n                    // In this case we are going to add an Audio item to the list so you\n                    // can play every stored Audio\n                    var url = URL.createObjectURL(AudioBLOB);\n                    var li = document.createElement(\'li\');\n                    var au = document.createElement(\'audio\');\n                    //var hf = document.createElement(\'a\');\n\n                    au.controls = true;\n                    au.src = url;\n                    //hf.href = url;\n                    // Important:\n                    // Change the format of the file according to the mimetype\n                    // e.g for audio/wav the extension is .wav\n                    //     for audio/mpeg (mp3) the extension is .mp3\n                    //hf.download = new Date().toISOString() + \'.wav\';\n                    //hf.innerHTML = hf.download;\n                    li.appendChild(au);\n                    //li.appendChild(hf);\n                    recordingslist.appendChild(li);\n                }, _AudioFormat);\n            }, false);\n        };\n    </script>\n\n    <!-- Include the recorder.js library from a local copy -->\n    <!-- <script src="recorder.js"></script> -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_add_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n    <script type="text/javascript">\n        $(document).ready(function() {\n            bookie.login.init();\n        });\n    </script>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "uri": "biom_form.mako", "filename": "htdocs/biom_form.mako", "line_map": {"64": 114, "65": 114, "66": 115, "67": 115, "68": 118, "69": 118, "75": 67, "79": 67, "85": 79, "27": 0, "39": 1, "40": 4, "41": 4, "42": 8, "43": 8, "44": 13, "45": 13, "46": 16, "47": 16, "48": 19, "49": 19, "50": 20, "51": 20, "52": 74, "53": 87, "54": 95, "55": 97, "56": 99, "57": 99, "58": 103, "59": 103, "60": 108, "61": 108, "62": 110, "63": 110}}
__M_END_METADATA
"""
