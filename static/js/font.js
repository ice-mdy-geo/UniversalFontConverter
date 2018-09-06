(document).ready(function(){
	$('label[for=myinput]').change(function(){
		if(this.value == 'Zawgyi') {
			$('#myinput').css("font-family", "Zawgyi-One")
			console.log("Source is Zawgyi-One");
		}
		if(this.value == 'Unicode') {
			$('#myinput').css("font-family", "pyidaungsu")
		}
		if(this.value == 'WinMyanmar'){
			$('#myinput').css("font-family", "win_innwaregular");
		}
	});
	$('label[for=myinput]').change(function(){
		if(this.value == 'Zawgyi') {
			$('#output').css("font-family", "Zawgyi-One")
			console.log("Source is Zawgyi-One");
		}
		if(this.value == 'Unicode'){
			$('#output').css("font-family", "pyidaungsu")
		}
		if(this.value == 'WinMyanmar') {
			$('#output').css("font-family", "win_innwaregular");
		}
	});
});
