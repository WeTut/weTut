$(document).ready(function(){

	$('.likeForm').submit(function(){
		var csrf = $(this).find('input[name=csrfmiddlewaretoken]').val();
		var answerId = $(this).find('input.answerId').val();
		var likes = $(this).find('input.nbLikes').val();
		
		$.ajax({
		  	type: "POST",
			url: "",
		  	data: { submit: "likeSubmit", csrfmiddlewaretoken:csrf, answerId:answerId}
		}).done(function( msg ) {
			if (msg=='OK'){
				$('#answer'+answerId+' table td.big').text(likes + 1);
				$('#answer'+answerId+' table td.small').text('Vous aimez');
				return false;
			}
			
		});
	});


	$('#id_filter').change(function(){
		var filter = $(this).val();
		var csrf = $('#filterform').find('input[name=csrfmiddlewaretoken]').val();
				
		$.ajax({
		  	type: "POST",
			url: "",
		  	data: { filter: filter, csrfmiddlewaretoken:csrf}
		}).done(function( data ) {
			//alert(data)
            $('body').html(data);
            $('#filterform option[value='+filter+']').attr("selected", "selected");
			return false;			
		}
		);

		return false;
	});


});


