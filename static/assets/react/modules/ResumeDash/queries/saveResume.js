$(function(){
	function saveResume(key, value, sub, pk, option) {
		// This API is made to save info based on key and sub key.
			var data = 0;
			$.ajax({
				async : (option != "add") ? true : false, //(true, false)
		        url : dataObj.form.actionUrl, // the endpoint
		        type : "POST", // http method
		        data : {
					key : key,  // field name
					value : value,  //Value of field
					sub : sub,  //header of field (ex education)
					pk : pk,  //pk of object, if exists
					option : option,  // add, delete, update
					'csrfmiddlewaretoken': dataObj.form.csrfToken
				},
		        // handle a successful response
		        success : function(json) {
					if(json != 0){
						show_saving(1000);
						if(key == "template"){
							document.getElementById('resume').contentWindow.location.reload(true);
							document.getElementById('mobile-resume').contentWindow.location.reload(true);
						}
						if(option == "add"){
							data=json;
						}
						//Success: 0
					}else{
						$('[name="'+key+'"]').css("border",'solid 1px red');
						// alert("Save failed, please refresh the page and try again");
						//Failed: 1
					}
		        }
			});
			if(option == "add"){
				return data;
			}
	};
});