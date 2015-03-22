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
	$('#full-form').on('keyup', '.directEdit',  function(){
		var elementId = $(this).attr('id');
		var iframe = $("#resume, #mobile-iframe");
		if(elementId != ''){
			elementSubstr = elementId.substr(0, elementId.indexOf('-')); //Get iframe item id
			iframe.contents().find('#'+elementSubstr).text($("#"+elementId).val());
		}
	});
	$('#full-form').on('change', 'select.directEdit', function(){
		var elementId = $(this).attr('id');
		var iframe = $("#resume, #mobile-iframe");
		if(elementId != ''){
			elementSubstr = elementId.substr(0, elementId.indexOf('-')); //Get iframe item id
			iframe.contents().find('#'+elementSubstr).text($("#"+elementId).val());
		}
	});
	
	$('#full-form').on('click', '.collapse-toggle', function(){
		var itemID = $(this).attr('id');
		var itemToHide = itemID.substr(0, itemID.indexOf('-'));
		var icon = $("#"+itemID+".delete-item").parents(".info-item");
		$('#'+itemToHide).slideToggle();
		$("i#"+itemID+".collapse-toggle ").toggleClass("fa-plus-square fa-minus-square");
		/** ADD INTO LAYOUT OF <li> IN TEMPLATE **/	
	});	
	
	$('#full-form').on('click', '.add-item', function(){
		var isSlider = $(this).attr('class').split(' ')[1];
		var iframe = $("#resume, #mobile-iframe");
		var number = $(this).attr('id'); //Last count
		var parentEl = $(this).parent(); // gets div.info-item which is the main container
		var template = $('#'+parentEl.attr('id')+"-template"); //Selects the appropriate template
		var templateClone = template.clone(true); //Clone Template
		var searchFor = $(templateClone).find("*[id*='{counter}']");
		$(searchFor).each(function() { //Replaces id counter with number
			var id = $(this).attr('id');
			var newId = id.replace('{counter}', "_New_"+number);
			$(this).attr('id', newId);
		});
		var searchFor = $(templateClone).find("*[name*='{counter}']");//Replaces name counter with number
		$(searchFor).each(function() { //Replaces counter with number
			var nameAttr = $(this).attr('name');
			var newNameAttr = nameAttr.replace('{counter}', number);
			$(this).attr('name', newNameAttr);
		});
		$(this).before(templateClone.html());//Place into page
		
		//Insert into Resume
		var inResume = iframe.contents().find('#'+parentEl.attr('id')+"-template");
		var resumeClone = inResume.clone(true); //Clone Template
		var searchFor = $(resumeClone).find("*[id*='{counter}']");
		$(searchFor).each(function() { //Replaces counter with number
			var id = $(this).attr('id');
			var newId = id.replace('{counter}', "_New_"+number);
			$(this).attr('id', newId);
		});
		var blankSpot = iframe.contents().find('#blank-'+parentEl.attr('id'));
		$(blankSpot).before(resumeClone.html());

		if(isSlider == 'add-slider') {
			$('#slider_New_'+number).noUiSlider({
				start: [ 0 ],
				connect: "lower",
				step: 5,
				range: {
					'min': 0,
					'max': 100
				}
			});
			$('#full-form').on('slide', '#slider_New_'+number, { slider: 'slider_New_'+number, percentHolder: 'percentage_New_'+number }, LinkVal);
		}
		
		number++;
		$(this).attr('id', number);
	});
	
	$('#full-form').on('click', '.delete-item', function(){
		var itemID = $(this).attr('id');
		var iframe = $("#resume, #mobile-iframe");
		$("#"+itemID+".delete-item").parents(".info-item").remove(); //Hide the box
		iframe.contents().find('#'+itemID).remove();
		amounts.push({ action: "delete", id: itemID });
		// for (i = 0; i < amounts.length; ++i) {
// 			alert(amounts[i].action + " - " +  amounts[i].id); //
// 		}
	});	
	
	$('#full-form').on('click', '.cancelInputAfter', function(){
		$(this).next('input').val("");
		$(this).prev('i').addClass("fa-bell-o");
		$(this).prev('i').html(" Save and refresh to add again");
		$(this).hide();
	});
	
});

function LinkVal(param){
	var $theVal=$("#"+param.data.slider).find(".noUi-origin")[0].style.left;
	$("#"+param.data.percentHolder).html($theVal)
}

//Take experience-info-template and put it into ul experience-info before #blank-"experience"

/*
	IDEA: Make stack to for removed information
		  Also, could log changes "initial" "What it is" with
*/