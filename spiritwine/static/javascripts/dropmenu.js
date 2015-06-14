function navmenu(){
	$("#nav ul li ul").css({display: "none"});
	$("#nav ul li").hover(function(){
		$(this).find('ul:first').css({visibility: "visible"}).show(400);}, function(){
			$(this).find('ul:first').css({visibility: "hidden"});
		});
}

$(document).ready(function(){
	navmenu();
});