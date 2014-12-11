$(document).ready(function(){
 	
	/* AUTO SAVE */
	// $("#autosaving").css("visibility","hidden");
// 	$('#full-form').sayt({'autosave': false, 'autorecover': true, 'days': 3});
// 	$( "#full-form" ).change(function() {
// 		function show_saving(t){
// 		      $("#autosaving").css("visibility","visible");
// 			  window.setTimeout( hide_saving, t );
// 		};
// 		function hide_saving(){
// 		      $("#autosaving").css("visibility","hidden");
// 		};
// 		$('#full-form').sayt({'savenow': true});
// 		show_saving(1000);
// 		return false;
// 	});
	/* / AUTO SAVE */ 

	var amounts = [];  
	
	
	/* Text Area */
	var $ta = $('.textarea-box');
	$ta.autosize();
	document.body.offsetWidth; // force a reflow before the class gets applied
	$ta.addClass('textarea-transition');
	/* /TextArea */
	
	/* TOGGLE MENU BAR */
	$(window).bind('mousewheel', function(event) { /* Up or down effect*/
	    if (event.originalEvent.wheelDelta >= 0) {
			$('#menu-toggle').removeClass('invisible'); //Slide In "UP"
			$('#menu-toggle').addClass('visible');
	    }
	    else {
			$('#menu-toggle').addClass('invisible'); //Slide Out "DOWN"
			$('#menu-toggle').removeClass('visible');
		}
	});
	
	$('#menu-toggle').click(function(){
		if($('#menu-toggle').hasClass('menu-x-close')){ //Slide Out
			$('.Top-menu').animate(
				{ right: -80 }, {
					duration: 'slow',
					easing: 'easeInOutCirc'
	        });
			$('.menu-toggle').animate(
				{ right: 45 }, {
					duration: 'slow',
					easing: 'easeInOutCirc'
	        });
			$('.Left-content').css("width", "100%;");
		}
		else{ //Slide IN
			$('.Top-menu').animate(
				{ right: 0 }, {
					duration: 'slow',
					easing: 'easeInOutCirc'
			});
			$('.menu-toggle').animate(
				{ right: 65 }, {
					duration: 'slow',
					easing: 'easeInOutCirc'
	        });
		}
		$('#menu-toggle').toggleClass('menu-x-close');
	});
	/* /TOGGLE MENU BAR */
	
	/* MENU BAR */
	var last="personal";
	var next;		
	$("section").hide();
	$('.collapsable-item').slideUp();
	$("#"+last+'-section').fadeIn("slow");
	$(".Top-menu>i").click(function(){
		next=$(this).attr('id');
		if(next!==last){
			$("#"+last).removeClass('activeIcon');
			$("#"+last+'-section').hide();
			next=$(this).attr('id');
			$("#"+next).addClass('activeIcon');
			$("#"+next+'-section').fadeIn("slow");
			last=next;
		}
	});
	/* END MENU BAR */
	
	/* BUTTON ACTIONS */
	$("button").click(function(){
		var clickedBtn = $(this).attr("id");
		if(clickedBtn == "fullscreen-btn"){
			if($('.Left').is(":visible")){
				$('.Left').hide();
				$('.Right').css({ width: '100%' });
				$('#'+clickedBtn).text("Edit Mode");
			}
			else{
				$('.Left').show();
				$('.Right').css({ width: '60%' });
				$('#'+clickedBtn).text("Fullscreen");
			}
		}  
	});
	/* END BUTTON ACTIONS*/
	
	/* Directly edit resume */
	$(".directEdit").keyup(function(){
		var elementId = $(this).attr('id');
		var iframe = $("#resume, #mobile-iframe");
		if(elementId != ''){
			elementSubstr = elementId.substr(0, elementId.indexOf('-')); //Get iframe item id
			iframe.contents().find('#'+elementSubstr).text($("#"+elementId).val());
		}
	});
	$("select.directEdit").change(function(){
		var elementId = $(this).attr('id');
		var iframe = $("#resume, #mobile-iframe");
		if(elementId != ''){
			elementSubstr = elementId.substr(0, elementId.indexOf('-')); //Get iframe item id
			iframe.contents().find('#'+elementSubstr).text($("#"+elementId).val());
		}
	});
	
	$('.add-item').click(function(){
		var parentEl = $(this).parent(); //<div class="panel-group" id="accordion">
		var item = $(this).parent().prev();
		parentEl.append(item.html());
		alert(item.html());
		//appendTo
	});
	
	$('.collapse-toggle').click(function(){
		var itemID = $(this).attr('id');
		var itemToHide = itemID.substr(0, itemID.indexOf('-'));
		var icon = $("#"+itemID+".delete-item").parents(".info-item");
		$('#'+itemToHide).slideToggle();
		$("#"+itemID+".collapse-toggle ").toggleClass("fa-plus-square fa-minus-square");
		
	});	
	
	$('.delete-item').click(function(){
		var itemID = $(this).attr('id');
		var iframe = $("#resume, #mobile-iframe");
		$("#"+itemID+".delete-item").parents(".info-item").fadeOut("fast"); //Hide the box
		iframe.contents().find('#'+itemID).remove();
		amounts.push({ action: "delete", id: itemID });
		// for (i = 0; i < amounts.length; ++i) {
// 			alert(amounts[i].action + " - " +  amounts[i].id); //
// 		}
	});	
	
});


/*
	IDEA: Make stack to for removed information
		  Also, could log changes "initial" "What it is" with
*/