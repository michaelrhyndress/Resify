$(document).ready(function(){
 	$('#new_tag_add').tabcomplete([
 				"array",
 				"arrays",
 				"arraies",
 				"with",
 				"words",
 				"to",
 				"complete"
 			]);
	/* AUTO SAVE */
	$("#autosaving").hide();
	// $('#full-form').sayt({'autosave': false, 'autorecover': true, 'days': 3});
	//$('#full-form').sayt({'savenow': true});
	/* / AUTO SAVE */ 

    $(".image-picker").imagepicker();

	$("#handle").on('keyup', function(){
		var handle=$("#handle").val();
		handle=slugify(handle); 
		$(".url").html("Resify.info/"+handle);
	});
  
  
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
		var elementValue = $("#"+elementId).val()
		var iframe = $("#resume, #mobile-iframe");
		if(elementId != ''){
			elementSubstr = elementId.substr(0, elementId.indexOf('-')); //Get iframe item id
			iframe.contents().find('#'+elementSubstr).text(elementValue);
		}
	});
	
	/* Directly save resume */
	$('#full-form').on('change', '.directEdit',  function(){
		var elementId = $(this).attr('id');
		var elementValue = $("#"+elementId).val()
		var iframe = $("#resume, #mobile-iframe");
		if(elementId != ''){
			elementSubstr = elementId.substr(0, elementId.indexOf('-')); //Get iframe item id
			iframe.contents().find('#'+elementSubstr).text(elementValue);
		}
		nameAttr = $("#"+elementId).attr("name")
		primaryKey = nameAttr.replace(/[^0-9]/g,'');
		saveResume(elementSubstr, elementValue, primaryKey, "update");
	});
	
	$('#full-form').on('change', '.checker',  function(){
		var elementId = $(this).attr('id');
		var elementValue = $("#"+elementId).prop( "checked" );
		nameAttr = $("#"+elementId).attr("name")
		primaryKey = nameAttr.replace(/[^0-9]/g,'');
		saveResume(elementId, elementValue, primaryKey, "update");
		
	});
	
	// $('#full-form').on('change', 'select.directEdit', function(){ #for select
// 		var elementId = $(this).attr('id');
// 		var iframe = $("#resume, #mobile-iframe");
// 		if(elementId != ''){
// 			elementSubstr = elementId.substr(0, elementId.indexOf('-')); //Get iframe item id
// 			iframe.contents().find('#'+elementSubstr).text($("#"+elementId).val());
// 		}
// 		//nameAttr = $("#"+elementId).attr("name")
// 		//primaryKey = nameAttr.replace(/[^0-9]/g,'');
// 		//saveResume(elementSubstr, elementValue, primaryKey, "update");
// 	});
	
	
	$('#full-form').on('slide', '.animateSlide', function(){
		var elementId = $(this).attr('id');
		var idNum=elementId.replace(/[^0-9]/g,'');
		if(elementId != ''){
			elementSubstr = elementId.substr(0, elementId.indexOf('-'));
			var $theVal=$("#"+elementId).find(".noUi-origin")[0].style.left;
			$("#percentage"+idNum+"-edit").html($theVal);
			$("#form_percentage"+idNum).attr("value", $theVal);
			$("#form_percentage_New_"+idNum).attr("value", $theVal);
			$("#percentage_New_"+idNum+"-edit").html($theVal);
			$theVal=$theVal.replace(/[%$]/g,'');
			var iframe = $("#resume, #mobile-iframe");
			iframe.contents().find('#percentage'+idNum).text($theVal);
			iframe.contents().find('#percentage_New_'+idNum).text($theVal);
			iframe.contents().find('#'+elementSubstr).attr("style", "width: "+$theVal+"%;");
			iframe.contents().find('#'+elementSubstr).attr("aria-valuenow", $theVal);
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
			$('#slider_New_'+number+"-edit").noUiSlider({
				start: [ 0 ],
				connect: "lower",
				step: 5,
				range: {
					'min': 0,
					'max': 100
				}
			});
		}
		
		number++;
		$(this).attr('id', number);
	});
	
	$('#full-form').on('keydown', '#new_tag_add',  function(e){ //May be possible to combine with old Add
		var keys = {
			tab: 9,
			enter: 13,
			up: 38,
			down: 40,
			comma: 188,
			semicolon: 186
		};
		var options = {
			arrowKeys: true
		};
		var elementValue = $(this).val();
		var elementId = 0;
		var key = e.keyCode;
		//188: comma ; 9: tab ; 186: semi-colon ; 13: enter 
		if(key == keys.comma || key == keys.semicolon || key == keys.enter){
			$('.hint').val("");
			e.preventDefault();
			if(elementValue != ""){
				elementId = saveResume("tags", elementValue, "None", "add");
			}
			else{
				return false;
			}
			if(elementId != 0){
				if(tags.indexOf(elementValue) == -1 && elementValue){ //Case sensitive?
					var stepUp = $(this).parent();
					var parentEl = stepUp.parent(); // gets div.info-item which is the main container
					var template = $('#'+parentEl.attr('id')+"-template"); //Selects the appropriate template
					var templateClone = template.clone(true); //Clone Template
					var searchFor = $(templateClone).find("*[id*='{counter}']");
					$(searchFor).each(function() { //Replaces id counter with number
						var id = $(this).attr('id');
						var newId = id.replace('{counter}', elementId);
						$(this).attr('id', newId);
					});
					
					stepUp.before(templateClone.html());
					var newVal=$("#tag"+elementId).html().replace("{value}", elementValue);
					$("#tag"+elementId).html(newVal.replace("{value}", elementValue));
					tags[elementId]=elementValue;
					$(this).val(''); //Clear input
				}
			}
		}
		// if(key == keys.tab || (options.arrowKeys && (key == keys.up || key == keys.down))){
		//
		// }
		else{
			//offer words, autocomplete!
			
			
		}
		
	});
	
	$('#full-form').on('click', '.delete-item', function(){
		var itemID = $(this).attr('id');
		splitID = itemID.split("_");
		$("#"+itemID+".delete-item").parents(".info-item").remove(); //Hide the box
		saveResume(splitID[0], "None", splitID[1], "delete");
		tags.pop([splitID[1]])
		amounts.push({ action: "delete", id: splitID[1] }); //stack of deletions
	});	
	
	$('#full-form').on('click', '.cancelInputAfter', function(){
		$(this).next('input').val("");
		$(this).prev('i').addClass("fa-bell-o");
		$(this).prev('i').html(" Save and refresh to add again");
		$(this).hide();
	});
	
});

function show_saving(t){
	$("#autosaving").show();
	window.setTimeout( hide_saving, t );
};
function hide_saving(){
      $("#autosaving").hide()
};

//Take experience-info-template and put it into ul experience-info before #blank-"experience"

/*
	IDEA: Make stack to for removed information
		  Also, could log changes "initial" "What it is" with
*/




/*!
 * tabcomplete
 * http://github.com/erming/tabcomplete
 * v1.5.0
 */
(function($) {
	var keys = {
		backspace: 8,
		tab: 9,
		up: 38,
		down: 40
	};

	$.tabcomplete = {};
	$.tabcomplete.defaultOptions = {
		arrowKeys: true,    // Allow the use of <up> and <down> keys to iterate
		hint: "placeholder", // "placeholder", "select", false
		match: match,
		caseSensitive: false,
		minLength: 1,
		wrapInput: true
	};

	$.fn.tabcomplete = function(args, options) {
		if (this.length > 1) {
			return this.each(function() {
				$(this).tabcomplete(args, options);
			});
		}

		// Set default options.
		this.options = options = $.extend(
			$.tabcomplete.defaultOptions,
			options
		);

		// Remove any leftovers.
		// This allows us to override the plugin if necessary.
		this.unbind(".tabcomplete");
		this.prev(".hint").remove();

		var self = this;
		var i = -1;
		var words = [];
		var last = "";
		var hint = $.noop;

		hint = placeholder;
		
		this.on("input.tabcomplete", function() {
			var input = self.val();
			var word = input.split(/ |\n/).pop();

			// Reset iteration.
			i = -1;
			last = "";
			words = [];

			// Check for matches if the current word is the last word.
			if (self[0].selectionStart == input.length
				&& word.length) {
				// Call the match() function to filter the words.
				words = options.match(word, args, options.caseSensitive);
			}

			// Emit the number of matching words with the 'match' event.
			self.trigger("match", words.length);
			if (options.hint) {
				if (word.length >= options.minLength) {
					// Show hint.
					hint.call(self, words[0]);
				} else {
					// Clear hinting.
					// This call is needed when using backspace.
					hint.call(self, "");
				}
			}

			if (backspace) {
				backspace = false;
			}
		});

		this.on("keydown.tabcomplete", function(e) {
			var key = e.keyCode;
			if (key == keys.tab
				|| (options.arrowKeys && (key == keys.up || key == keys.down))) {

				// Don't lose focus on tab click.
				e.preventDefault();

				// Iterate the matches with tab and the up and down keys by incrementing
				// or decrementing the 'i' variable.
				if (key != keys.up) {
					i++;
				} else {
					if (i == -1) return;
					if (i == 0) {
						// Jump to the last word.
						i = words.length - 1;
					} else {
						i--;
					}
				}

				// Get next match.
				var word = words[i % words.length];
				if (!word) {
					return;
				}

				var value = self.val();
				last = last || value.split(/ |\n/).pop();

				// Return if the 'minLength' requirement isn't met.
				if (last.length < options.minLength) {
					return;
				}

				// Update element with the completed text.
				var text = options.hint == "select" ? value : value.substr(0, self[0].selectionStart - last.length) + word;
				self.val(text);

				// Put the cursor at the end after completion.
				// This isn't strictly necessary, but solves an issue with
				// Internet Explorer.
				if (options.hint == "select") {
					self[0].selectionStart = text.length;
				}

				// Remember the word until next time.
				last = word;

				// Emit event.
				self.trigger("tabcomplete", last);

				if (options.hint) {
					// Turn off any additional hinting.
					hint.call(self, "");
				}
				else if (key == keys.backspace) {
					// Remember that backspace was pressed. This is used
					// by the 'input' event.
					backspace = true;

					// Reset iteration.
					i = -1;
					last = "";
				}
			}
		});

		if (options.hint) {
			// If enabled, turn on hinting.
			hint.call(this, "");
		}

		return this;
	}

	// Simple matching.
	// Filter the array and return the items that begins with 'word'.
	function match(word, array, caseSensitive) {
		return $.grep(
			array,
			function(w) {
				if (caseSensitive) {
					return !w.indexOf(word);
				} else {
					return !w.toLowerCase().indexOf(word.toLowerCase());
				}
			}
		);
	}

	// Show placeholder text.
	// This works by creating a copy of the input and placing it behind
	// the real input.
	function placeholder(word) {
		var input = this;
		var clone = input.prev(".hint");

		input.css({
			backgroundColor: "transparent",
			position: "relative",
		});

		// Lets create a clone of the input if it does
		// not already exist.
		if (!clone.length) {
			if (input.options.wrapInput) {
				input.wrap(
					$("<div>").css({position: "relative", height: input.css("height"), display: input.css("display")})
				);
			}
			clone = input
				.clone()
				.attr("tabindex", -1)
				.removeAttr("id name placeholder")
				.addClass("hint")
				.insertBefore(input);
			clone.css({
				position: "absolute",
			});
		}

		var hint = "";
		if (typeof word !== "undefined") {
			var value = input.val();
			hint = value + word.substr(value.split(/ |\n/).pop().length);
		}

		clone.val(hint);
	}

})(jQuery);

function slugify(text){
	return text.toString().toLowerCase()
	  .replace(/\s+/g, '')           // Replace spaces
	  .replace(/[^\w\-]+/g, '')       // Remove all non-word chars
	  .replace(/\-+/g, '')         // Replace multiple - with single -
	  .replace(/^-+/, '')             // Trim - from start of text
	  .replace(/-+$/, '');            // Trim - from end of text
}
