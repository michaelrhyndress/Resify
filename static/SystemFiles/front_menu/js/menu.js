$(document).ready(function() {
	$('.sidebar-menu').hide();
    $('.sidebar-menu-trigger').click(function(){
        $('.sidebar-menu').animate({width: 'toggle'}, 400);
    });
	$('.sidebar-menu > ul li').click(function(){
		$(this).find('.drop-down').slideToggle(400);
	});
});