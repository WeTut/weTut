$(document).ready(function(){



	$('.likeForm').submit(function(){
		
		var csrf = $(this).find('input[name=csrfmiddlewaretoken]').val();
		var answerId = $(this).find('input.answerId').val();
		
		$.ajax({
		  	type: "POST",
			url: "",
		  	data: { submit: "likeSubmit", csrfmiddlewaretoken:csrf, answerId:answerId}
		}).done(function( likes ) {

				$('#answer'+answerId+' table td.big').text(likes);
				$('#answer'+answerId+' table td.small').text('Vous aimez');
				//innerHTML'<p>Vous aimez</p>')
				return false

			
		});

		return false;
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
		});
 
 		return false;
 	});

 	$('#tag1 select').change(function(){
		var val = $(this).val();
		var csrf = $('#questionForm').find('input[name=csrfmiddlewaretoken]').val();

		$.ajax({
		  	type: "POST",
			url: "",
		  	data: { csrfmiddlewaretoken:csrf }
		}).done(function( data ) {
            if (val != 0)
           		document.getElementById('tag2').style.display = 'block';
			return false;			
		});
 
 		return false;
 	});

 	$('#tag2 select').change(function(){
		var val = $(this).val();
		var csrf = $('#questionForm').find('input[name=csrfmiddlewaretoken]').val();

		$.ajax({
		  	type: "POST",
			url: "",
		  	data: { csrfmiddlewaretoken:csrf }
		}).done(function( data ) {
            if (val != 0)
           		document.getElementById('tag3').style.display = 'block';
			return false;			
		});
 
 		return false;
 	});



});







/*


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
		});

		return false;
	});


*/


