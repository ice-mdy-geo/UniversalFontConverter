$(document).ready(function(){
  $('form').on('submit', function (event){
	$.ajax({
  		type: "POST",
		url: "/convert4",
		data: {
			myinput: $('#myinput').val()
		}
	})
  .done(function(data){
    if(data.error){
      //Do something
    }
    else{
      $("#output").val(data.output).show();
    }
  });

  event.preventDefault();
});
});