$(document).ready(function(){

	

	$('#question .likeform').submit(function(){
		var csrf = $(this).find('input[name=csrfmiddlewaretoken]').val();
		var answerId = $(this).find('input[name=answerId]').val();
		
		$.ajax({
		  	type: "POST",
			url: "",
		  	data: { submit:'likeSubmit', csrfmiddlewaretoken:csrf, answerId:answerId}
		}).done(function( likes ) {

				$('#answer'+answerId+' table td.big').text(likes);
				$('#answer'+answerId+' table td.small').text('Vous aimez');
				return false			
		});

		return false;
	});

	$('.followForm').submit(function(){
		var csrf = $(this).find('input[name=csrfmiddlewaretoken]').val();
		var questionId = $(this).find('input.questionId').val();
		var hidden = $(this).find('input[name=hidden]').val();
		var divcontent = "<input name='hidden' type='hidden' value='follow' /><button class='btn btn-primary btn-block vcenter' name='submit' type='submit' value='followSubmit'>Suivre</button>";		
		if (hidden == 'follow')
			divcontent = "<input name='hidden' type='hidden' value='unfollow' /><button class='btn btn-danger btn-block vcenter' name='submit' type='submit' value='followSubmit'>Ne plus suivre</button>";	


		$.ajax({
		  	type: "POST",
			url: "",
		  	data: { submit:'followSubmit', hidden: hidden, csrfmiddlewaretoken:csrf, questionId:questionId}
		}).done(function( msg ) {
			$('#question'+questionId+' .follow').html(divcontent);
			return false;			
		});

		return false;
	});


	$('.followTagForm').submit(function(){
		var csrf = $(this).find('input[name=csrfmiddlewaretoken]').val();
		var tagId = $(this).find('input.tagId').val();
		var hidden = $(this).find('input[name=hidden]').val();
		var divcontent = "<input name='hidden' type='hidden' value='follow' /><button class='btn btn-primary btn-block vcenter' name='submit' type='submit' value='followTagSubmit'>Suivre ce tag</button>";		
		if (hidden == 'follow')
			divcontent = "<input name='hidden' type='hidden' value='unfollow' /><button class='btn btn-danger btn-block vcenter' name='submit' type='submit' value='followTagSubmit'>Ne plus suivre</button>";	

		$.ajax({
		  	type: "POST",
			url: "",
		  	data: { submit:'followTagSubmit', hidden: hidden, csrfmiddlewaretoken:csrf, tagId:tagId}
		}).done(function( msg ) {
			$('.followTagForm .follow').html(divcontent);
			return false;			
		});

		return false;
	});


	$('#id_filter').change(function(){

		var filter = $(this).val();
		var csrf = $('#filterform').find('input[name=csrfmiddlewaretoken]').val();
				
		$.ajax({
		  	type: "POST",
			url: "",
		  	data: { submit:'filterSubmit', filter: filter, csrfmiddlewaretoken:csrf}
		}).done(function( data ) {
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


 	$('#questionForm select').change(function(){
		var val = $(this).val();
		var csrf = $('#questionForm').find('input[name=csrfmiddlewaretoken]').val();		
		var selectClass = $(this).attr('class');
		var selectClassToUpdate = '.technical';
		if (selectClass == 'technical'){
			selectClassToUpdate = '.software';
		}
		var parent = '#'+ $(this).closest("div").attr("id");

		$.ajax({
		  	type: "POST",
			url: "",
		  	data: { csrfmiddlewaretoken:csrf }
		}).done(function( data ) {
            if (val != 0){
       			$(parent + ' ' + selectClassToUpdate +' option[value=0]').attr('selected', 'selected');
           	}

			return false;			
		});
 
 		return false;
 	});


 	$('#filtertag a').click(function(){
		$('#filtertag a').removeClass('bold')
		$(this).addClass('bold')
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


