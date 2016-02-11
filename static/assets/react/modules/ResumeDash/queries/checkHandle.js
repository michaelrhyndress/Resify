function checkHandle(handle, csrf) {
	handle=handle.replace(/\s/g,''); 

	$.ajax({
		async : true,
        url : "/check_handle", // the endpoint
        type : "POST", // http method
        data : {
			handle : handle,
			'csrfmiddlewaretoken': csrf
		},
        // handle a successful response
        success : function(json) {
			if(json == 0){
				$('#handle').css("border",'solid 1px green');
				$('#resume').attr("src", handle);
				$('#mobile-resume').attr("src", handle);
				saveResume("handle", handle, "None",-1, "update");
				//Success: 0
			}else{
				$('#handle').css("border",'solid 1px red');
				// alert("That URL is taken");
				//Failed: 1
			}
        }
	});
};