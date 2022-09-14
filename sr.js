var final_transcript = ''
var recognizing = false

if ('webkitSpeechRecognition' in window) {
    var recognition = new webkitSpeechRecognition()

    recognition.continuous = true
    recognition.interimResults = true

    recognition.onstart = function () {
        console.log("onstart")
        recognizing = true
    }
    recognition.onerror = function (event) {
        console.log(event.error)
    }

    recognition.onend = function () {
        recognizing = false
        console.log("onend")
    };

    recognition.onresult = function (event) {
        console.log("onresult")
        var interim_transcript = ''
        for (var i = event.resultIndex; i < event.results.length; ++i) {
            if (event.results[i].isFinal) {
                final_transcript += event.results[i][0].transcript
            } else {
                interim_transcript += event.results[i][0].transcript
            }
        }
        final_transcript = capitalize(final_transcript)
        document.getElementById("resultholder").value = linebreak(final_transcript)
        document.getElementById("preresultext").innerHTML = linebreak(interim_transcript)

    }
}

var two_line = /\n\n/g
var one_line = /\n/g
function linebreak(s) {
    return s.replace(two_line, '<p></p>').replace(one_line, '<br>')
}

function capitalize(s) {
    return s.replace(s.substr(0, 1), function (m) { return m.toUpperCase() })
}
currentimg = "record"
function recordstart(event){
    console.log(currentimg)
    if (currentimg == "record"){

        recognition.lang = 'am-ET'
        recognition.start()
        document.getElementById("resultholder").value = ''
        final_transcript = ""
        document.getElementById("record-btn").src = "images/stop.png"
        document.getElementById("preresult").style.display = "block"
        document.getElementById("recordinfo").innerHTML = "recording"
        currentimg = "stop"

    }else if (currentimg == "stop"){
        recognition.stop()
        document.getElementById("record-btn").src = "images/record.png"
        document.getElementById("recordinfo").innerHTML = "Tap to start"
        document.getElementById("preresult").style.display = "none"
        currentimg = "record"
        
    }
}
