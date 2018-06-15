var API_ENDPOINT = "https://mr9gaszf3i.execute-api.eu-west-1.amazonaws.com/Prod"

document.getElementById("uploadTax").onclick = function(){

	var inputData = {
		"userName" : $('#userName').val(),
		"taxField1" : $('#taxField1').val(),
		"taxField2" : $('#taxField2').val(),
		"taxField3" : $('#taxField3').val(),
		"taxField4" : $('#taxField4').val()
	};

	$.ajax({
	      url: API_ENDPOINT,
	      type: 'POST',
	      data:  JSON.stringify(inputData)  ,
	      contentType: 'application/json; charset=utf-8',
	      success: function (response) {
					document.getElementById("postIDreturned").textContent="Post ID: " + response;
	      },
	      error: function () {
	          alert("error");
	      }
	  });
}


document.getElementById("searchButton").onclick = function(){

	var postId = $('#postId').val();


	$.ajax({
				url: API_ENDPOINT + '?postId='+postId,
				type: 'GET',
				success: function (response) {

					$('#posts tr').slice(1).remove();

	        jQuery.each(response, function(i,data) {

						$("#posts").append("<tr> \
								<td>" + data['id'] + "</td> \
								<td>" + data['userName'] + "</td> \
								<td>" + data['taxField1'] + "</td> \
								<td>" + data['taxField2'] + "</td> \
								<td>" + data['taxField3'] + "</td> \
								<td>" + data['taxField4'] + "</td> \
								</tr>");
	        });
				},
				error: function () {
						alert("error");
				}
		});
}

document.getElementById("postText").onkeyup = function(){
	var length = $(postText).val().length;
	document.getElementById("charCounter").textContent="Characters: " + length;
}
