$(document).ready(function(){




	function sleep(ms) {
		  return new Promise(resolve => setTimeout(resolve, ms));
		}	

		// ADD COMMENT
	$("#commentform").submit(function(e){
		e.preventDefault();
		var form = $(this);
		var link = form.attr('action');
		var button = form.find("#subcomment");
		var input= form.find("#id_text");
		var block = $("#commentsblock");
		if (input.val() != ""){
			var form_ser = form.serialize();
			$.ajax({
				method: "POST",
				type: "json",
				url: link,
				data: form_ser,
				success: async function(data){
					if(data['success'] == 'submit'){
						var sender = data['sender'];
						var pk = data['pk'];
						var date = data['date'].substr(0,16).replace("T", " ")
						var avatar = data['avatar'];
						var text = data['text'];
						var html = '<div id="bigcomment" class="col-lg-12"><div class="col-lg-1">\
						<img id="imgcomment" src="'+ avatar + '" style="width:40px; height:40px;" class="img-responsive img-circle"/>\
						</div><div id="comment" class="col-lg-11"><h4><b>'+ sender +'</b><small> '+ date + '</small></h4>\
							<p>'+ text + '</p>\
							<hr></div></div>';
						

						input.val("");
						button.prop('disabled', true);
						await sleep(1000)
						block.prepend(html);
						button.prop('disabled', false);
						$("#sumcomment").text(function(i, origText){
						
						return Number(origText) +1
					});

					}
				}


			})
		
		
		} else {
		 alert("Şərh yazmamısız");
		}
		
		
		});		
		
		// COMMENT DELETE
		$(".comdelete").click(function(e){
		e.preventDefault();
		var comment= $(this).parents("#bigcomment");
		var link= $(this).attr('href');
		

		
		
		$.ajax({
			method: "GET",
			type: "json",
			url: link,
			success: function(data){
				if(data['success'] == 'true'){
					
					var htmlkod='<div id="messagediv" class="alert alert-danger fade in text-center">\
						<span id="message">Şərh Silindi!</span><a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a></div>';
					comment.html(htmlkod);
					
					$("#sumcomment").text(function(i, origText){
						
						return Number(origText) -1
					});
					comment.fadeOut(4000);


				}



			}


		})
		
		}); // END COMMENT DELETE

		
		
		
		
		
		
		// ADD REPLY
		$(".replyform").submit(function(e){
		e.preventDefault();
		var form = $(this);
		var input = form.find("#id_rtext");
		var button = form.find("#replysub");
		//console.log($(this).parents("form"));
		if (input.val() != ""){
		
		var action = form.attr('action');
		var form_ser = form.serialize();
		$.ajax({
			method: "POST",
			type: "json",
			url: action,
			data: form_ser,
			success: async function(data){
			if (data["success"] == 'submit') {
			var div = "#"+"replies" + data['pk'];
			var date = data['date'].substr(0,16).replace("T", " ")
			var rep = data['text'];
			var sender = data['sender'];
			
			var html1 = '<h5><strong>'+sender+'</strong>'+' '+'<small>['+date+']</small></h5>';
			var html2 = $("<p></p>").text(rep);
			input.val("");
			button.prop('disabled', true);
			await sleep(1000)
			button.prop('disabled', false);
			$(div).prepend(html2);
			$(div).prepend(html1);
			
			}
			
			}
		
		
		})
		
		
		
		
		} else {
		alert("Cavab yazmamısız")
		}
		});
		
		// DELETE BUTTON
		$("#delslide").click(function(){
    	$("#del").slideToggle();
			});
		$('[data-toggle="popover"]').popover(); 


//LIKE BUTTON
$('#likebtn').click(function(e){
	e.preventDefault();
	var a = $(this);
	var link=a.attr('href');
	var icon =$("#icon");
	var likes=$("#likenum");
	var likers=$("#likers");
	var name
	var txt=' ';
	
	$.ajax({

		method: "GET",
		type: 'json',
		url: link ,
		success: function(data){
			var names=data['names']
			for (name in names){
				txt= txt + names[name] + '<br>';
			
			}
			
			
			if(data['success'] =='like'){
			likes.text(function(i, origText){
			return Number(origText)+1
			
			});
			
			icon.attr("class","glyphicon glyphicon-thumbs-down");
			a.attr("class","btn btn-danger");
			} else if (data['success'] =='unlike'){
			likes.text(function(i, origText){
			return Number(origText)-1
			
			});
			
			icon.attr("class","glyphicon glyphicon-thumbs-up");
			a.attr("class","btn btn-success");
			
				}
				
				likers.attr("data-content",txt);
				
				}


		
		
		})

});



    });   