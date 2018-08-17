$(document).ready(function(){
	function sleep(ms) {
		  return new Promise(resolve => setTimeout(resolve, ms));
		}

	$("#form").submit(function(event){
		event.preventDefault();
		var form = $(this);
		var block = $(".list-group");
		var input = form.find("#id_title")
		var formdata = form.serialize();
		var button = form.find(".btn");
		var options = { day: 'numeric', month: 'long', year: 'numeric',  hour: '2-digit', minute: '2-digit' };

		$.ajax({
			method: "POST",
			type: "json",
			url: "",
			data: formdata,
			success: async function(data){
				if (data['success'] == 'true' ){
					
					var created = dateFormat(data['created'], "d mmmm yyyy, HH:MM");
					
					function completed(){
						if (data['completed'] == true){
							return '<span class="badge">Tamamlanıb</span>'
						}else{
							return ''
						}
					}
					var title = data['title'];
					var pk = data['pk'];
					var html = '<li class="list-group-item list-group-item-success"><h4>\
					' + title + '<small> ' + created + '</small>' + completed() + '</h4></li>';
					input.val("");
					button.prop('disabled', true);
					
					block.prepend(html);
					await sleep(1000)
					$('.list-group-item-success').removeClass('list-group-item-success')
					button.prop('disabled', false);
					
					
				

				}

			}
		}) //AJAX

	}); // FORM SUBMIT

$('.complete').click(function(event){

	event.preventDefault();
	var link = $(this).attr('href');
	var object = $(this).parents('.list-group-item');

	$.ajax({
		method: 'GET',
		type: 'json',
		url: link,
		success: async function(data){
			if(data['success'] == true){
				
				object.addClass('list-group-item-success')
				await sleep(1000)
				object.hide('slow');

			}
		}



	})



}); //OBJECT COMPLETE

$('#list').change(function(event){
	$('#listform').submit();
});




	}); // DOCUMENT READY
