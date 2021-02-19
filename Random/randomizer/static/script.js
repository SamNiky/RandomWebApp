$(document).ready(function(){
    $('#logout').click(function(){window.location.href = "/auth-logouts"});
    circle = $('.circle')

//AJAX request
	setInterval(function(){
		$.ajax({
			url: '',
			type: 'get',
			data: '',
			success: function(response){
				circle.text(response.cur);
			}
		});	
	}, 5000);
});