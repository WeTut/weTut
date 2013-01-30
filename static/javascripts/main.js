$(document).ready(function(){

	$('#likeForm').submit(function(){
		
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
				//innerHTML'<p>Vous aimez</p>')
				return false
			}
			
		});

		return false;
	});

});