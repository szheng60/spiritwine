var promotion_images = new Array();
var promotion_image_count = 4;
var ii = 1;
function load_promotion_images(){
	for (i=1; i <= promotion_image_count; i++)
	{
		promotion_images[i] = new Image();
		promotion_images[i].src = STATIC_URL + 'images/promotion/' + i + '.jpg'
	}
	display_promotion_image();
}

function display_promotion_image(){
	var promotion_image = document.getElementById('promotion');
	promotion_image.innerHTML = "<img src='" + promotion_images[ii].src + "'>";
	promotion_image.style.opacity = 1;
	setTimeout(function(){
			delay_display_promotion_image(promotion_image);
			}, 3000);
}
function delay_display_promotion_image(promotion_image){
	ii++;
	if (ii > promotion_image_count)
		ii = 1;
	promotion_image.style.opacity = 0;
	setTimeout(display_promotion_image, 2000);
}
