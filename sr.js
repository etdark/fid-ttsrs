var final_transcript = ''
var recognizing = false

if ('webkitSpeechRecognition' in window) {
    var recognition = new webkitSpeechRecognition()

    recognition.continuous = true
    recognition.interimResults = true

    recognition.onstart = function () {
        recognizing = true
    }

    recognition.onend = function () {
        recognizing = false
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
        document.getElementById("result-holder").value = linebreak(final_transcript)
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

        recognition.lang = 'am'
        recognition.start()
        document.getElementById("result-holder").value = ''
        final_transcript = ""
        document.getElementById("record-icon").src = "./images/stop.png"
        document.getElementById("recordinfo").innerHTML = "recording"
        document.getElementById("preresult").style.display = "block"
        currentimg = "stop"

    }else if (currentimg == "stop"){
        recognition.stop()
        document.getElementById("record-icon").src = "images/record.png"
        document.getElementById("recordinfo").innerHTML = "Tap to start"
        document.getElementById("preresult").style.display = "none"
        currentimg = "record"
        
    }
}
var result = ""

function done(){
    document.getElementById("btn-upload").style.display = "block"
    document.getElementById("upload-text").style.display = "none"
    document.getElementById("btn-done").style.display = "none"
    var input = document.getElementById("upload").files[0]
    const data = new FormData()
    data.append('file', input)
    fetch("https://tmpfiles.org/api/v1/upload/", {
         method: 'POST',
         body:data,
    
        })
    .then(response => response.json())
    .then(data => {
          url_data = Object.values(data)[1]
          url = Object.values(url_data)[0]
          str_url = JSON. stringify(url)
          final_url = str_url.substr(0,21) + "/dl" + str_url.substr(21) 
          url = "https://amh-rs.herokuapp.com/?text="+ final_url 
          var xmlHttp = new XMLHttpRequest()
          xmlHttp.open( "GET", url )
          xmlHttp.onreadystatechange = function() {
            if (xmlHttp.readyState == XMLHttpRequest.DONE){
                transcript = JSON.parse(xmlHttp.responseText)["transcript"]
                document.getElementById("result-holder").value = transcript
                }
            }
           xmlHttp.send();
    })
    .catch(error => {
        console.error(error)
    
      })
}
function upload(){ 
    document.getElementById("btn-upload").style.display = "none"
    document.getElementById("upload-text").style.display = "block"
    document.getElementById("btn-done").style.display = "block"
    document.getElementById("upload").click()
}

