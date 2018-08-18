$(document).ready(function(){
	function sleep(ms) {
		  return new Promise(resolve => setTimeout(resolve, ms));
		}
	$("#form").submit(function(event){
		event.preventDefault();
		var form = $(this);
		var block = $(".list-group");
		var input = form.find("#id_title");
		var inputtext = form.find('#id_text');
		var formdata = form.serialize();
		input.val("");
		inputtext.val("");
		var button = form.find(".btn");

		$.ajax({
			method: "POST",
			type: "json",
			url: "",
			data: formdata,
			success: async function(data){
				if (data['success'] == 'true' ){
					 /*
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
					var html = '<a href="#" class="list-group-item list-group-item-success"><h4>\
					' + title + '<small> ' + created + '</small>' + completed() + '</h4></a>\
					<div style="display: none;" class="detail">\
					Əlavə olunub:'+ created +'<br>\
					Haqqında:<br>\
					'+ data['text'] +'</div>';
					*/
					form.hide('slow');
					$('#openform').show('slow');
					button.prop('disabled', true);
					//block.prepend(html);
					await sleep(1000)
					//$('.list-group-item-success').removeClass('list-group-item-success')
					button.prop('disabled', false);
					location.reload();
					
					
				

				}

			}
		}) //AJAX

	}); // FORM SUBMIT 

$('.complete').click(function(event){

	event.preventDefault();
	var link = $(this).attr('url');
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

// OBJECT DELETE
$('.delete').click(function(event){
	event.preventDefault();
	var link = $(this).attr('url');
	var div = $(this).parents(".list-group-item");
	console.log(div);
	$.ajax({
		method: 'GET',
		type: 'json',
		url: link,
		success: async function(data){
			if(data['success'] == true){

				div.addClass('list-group-item-danger')
				await sleep(1000)
				div.hide('slow');

			}
		}
	}) //ajax
}); // OBJECT DELETE



$('#list').change(function(event){
	$('#listform').submit();
});

// DETAİL
$('.name').click(function(event){
	event.preventDefault();
	var a = $(this);
	var div = a.find('.detail');
	div.removeClass('detail');
	$('.detail').slideUp();
	div.addClass('detail');
	div.slideToggle();

}); // DETAİL

$('#openform').click(function(event){
	event.preventDefault();
	$(this).hide('slow');
	$('#form').show('slow');
});


	}); // DOCUMENT READY
