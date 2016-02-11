// var React = require('react')
// var ReactDOM = require('react-dom')


require('vide');
require('../../../scss/modules/Homepage/homepage.scss')
require('../../../scss/modules/Homepage/HowSection.scss')

// Video
$("header").vide({
    webm: require('./media/video/interview.webm'),
    poster: require('./media/img/interview.jpg'),
}, {
	loop: false,
	posterType: "jpg"
});


//Header
$(function() {
	$('.navbar-collapse ul li a').click(function() {
	    $('.navbar-toggle:visible').click();
	});
	setTimeout(function(){
		$("a#learn.button").animate({top:-200, opacity: 1}, 600, function() {
		});
	}, 600);
});


$(function() {
	//Flipper
	$(".slide2").hide();
	$(".slide3").hide();
	$(".slide4").hide();
	
	var flips = 0;
	$('.flip').click(function(){
		if(flips == 4){
			return true;
		}
		if(flips != 4){
			flips++;
	        $(this).parent().find('.card').toggleClass('flipped');
			if(flips == 1){
				if($("#boring-percent").hasClass("p0")){
					$("#boring-percent").removeClass("p0");
					var initial = $("#boring-percent > span").text();
					initial = initial.replace("%", "");
					$("#boring-percent > span").text("0");
					for(var i=0; i < initial; i++){
						setTimeout(function(){
							var value = parseInt($("#boring-percent > span").text(), 10) + 1;
							$("#boring-percent").addClass("p"+initial);
							$("#boring-percent > span").text(value+"%");
						}, (i * 25));  
					}
					setTimeout(function(){
						$(".slide1").first().hide();
						$(".slide2").first().show();
					}, 500);
					setTimeout(function(){
						$("#boring-percent > span").text("Click");
					}, 6000);  
				}
			} //if flip == 1
			if(flips == 2){
				setTimeout(function(){
					$(".slide1").hide();
					$(".slide2").show();
					$(".slide3").show();
				}, 500);  	
			}
			if(flips == 3){
				setTimeout(function(){
					$(".slide2").hide();
					$(".slide4").show(); 
				}, 500);  

			}
		} //if flip != 4
	        return false;
	});
});


