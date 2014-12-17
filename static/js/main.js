$( function() {
	$(".slide2").hide();
	$(".slide3").hide();
	$(".slide4").hide();
	
	$('#register-block').hide();
	$('#recover-block').hide();
	var last="login"
	$(".button").click(function(e){
		$("#"+last+"-block").slideUp( "slow");
		last=e.target.id;
		$("#"+last+"-block").slideDown( "slow");
	});
	
	$('#register-submit').click(function(){
		var isTermsChecked = $('#termsAgree').prop('checked');
		if(!isTermsChecked){
			alert("To register you must check the Terms & Conditions.");
			return false;
		};
		return true;
	});
	
	setTimeout(function(){
		$("a#learn.button").animate({top:-200, opacity: 1}, 600, function() {
		});
	}, 600);  
		
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




$(function() {
  $('a[href*=#]:not([href=#])').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        $('html,body').animate({
          scrollTop: target.offset().top
        }, 1000);
        return false;
      }
    }
  });
});