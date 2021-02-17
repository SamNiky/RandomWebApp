$(document).ready(function(){
	circle = $('.circle')
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
