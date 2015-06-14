$(document).ready(function(){
	$('#search input[type="submit"]').attr('disabled', 'disabled');
	$('#search input[type="text"]').bind("keyup change blur", function(){
		if($("#searchtext").val() == "") {
			$('#search input[type="submit"]').attr('disabled', 'disabled');
		} else {
			$('#search input[type="submit"]').removeAttr('disabled');
		}
	})
	
	})