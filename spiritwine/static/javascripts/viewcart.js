$(document).ready(function(){
	$('#viewcart .viewcart').click(function(){
		$('#cart-page').css({visibility: "visible"}).show(400);
	})
	$('#cart-page .close-btn').click(function(){
		$('#cart-page').css({visibility: "hidden"});
	})
})