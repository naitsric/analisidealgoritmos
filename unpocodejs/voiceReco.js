
if (!('webkitSpeechRecognition' in window)) {
	upgrade();
} else {
	var recognition = new webkitSpeechRecognition();
	recognition.continuous = true;
	recognition.interimResults = true;
	recognition.onstart = function() { 
		recognizing = true;
		alert("Comenzamos"); 
	}
	recognition.onresult = function(event) {
		debugger;
    	var interim_transcript = '';

    	for (var i = event.resultIndex; i < event.results.length; ++i) {
			if (event.results[i].isFinal) {
				final_transcript += event.results[i][0].transcript;
			} else {
	        	interim_transcript += event.results[i][0].transcript;
	      	}
	    }
	    final_transcript = capitalize(final_transcript);
	    //final_span.innerHTML = linebreak(final_transcript);
	    debugger;
	    $("#final_span").append(linebreak(final_transcript));
	    $("#interim_span").append(linebreak(interim_transcript));
	    //interim_span.innerHTML = linebreak(interim_transcript);
	};
	//recognition.onerror = function(event) { ... }
	recognition.onend = function() { alert("Terminamos"); }
	function startButton(event) {
		final_transcript = '';
		recognition.lang = "es-CO";//select_dialect.value;
		debugger;
		recognition.start();
		debugger;
	}
}