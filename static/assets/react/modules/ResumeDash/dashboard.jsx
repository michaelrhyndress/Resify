<<<<<<< HEAD
var React = require('react')
var ReactDOM = require('react-dom')

var $ = require('jquery');
window.jQuery = $;
window.$ = $;

//image-picker
require('../../../js/vendor/image-picker.js');
require('../../../scss/vendor/image-picker/image-picker.scss')

//
=======
'use strict';

// var React = require('react')
// var ReactDOM = require('react-dom')

//image-picker
require('vendor/image-picker.js');
require('vendor/image-picker/image-picker.scss');

//main
require('modules/ResumeDash/Resify_main.js');
require('modules/ResumeDash/Resify_main.css');

//Tab Complete
require('partials/tabcomplete.js');

//Queries
require('./queries/checkHandle.js');
require('./queries/saveResume.js');

//Social Media
require("./views/Facebook");

//Vendor
require("vendor/jquery.autosize.min.js");

$(function(){
	var APP = window.APP = window.APP || {};

	APP.dashboard = (function(){

		var dataObj = globalJSON; 
	
		var handleChange = function() {
			$("#handle").change(function() {
				var handle = slugify($('#handle').val());
				$('#handle').val(handle);
				if(dataObj.data.lastHandle !== handle){
					checkHandle(handle, dataObj.form.csrfToken)
					dataObj.data.lastHandle = handle
				}
				else{
					$('#handle').css("border",'solid 1px white');
				}
			});
		}
	
	    var bindEventsToUI = function() {

	    };
	
	    var init = function() {
	        console.log('APP.dashboard');
	        bindEventsToUI();
	    };

	    /**
	     * interfaces to public functions
	     */
	    return {
	        init: init
	    };

	}());
)};

// var db_tag_list = [];
//  //Makes the tag list from db for tab complete
// {% for tag in tag_list %}
// 	db_tag_list[{{forloop.counter0}}]="{{tag}}";
// 	{%if forloop.last%}$('#new_tag_add').tabcomplete(db_tag_list);{%endif%}
// {% endfor %}

>>>>>>> oldish-state
