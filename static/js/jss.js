$(document).ready(function(){
var gos = 1;  /* attach a submit handler to the form */
 $("#id_username").blur(function(event) {
	 $('#result').fadeOut();
    /* stop form from submitting normally */      
    /* get some values from elements on the page: */
    var $form = $( this ),
        url = $('#frmsingup').attr('action') + 'chkusr/';
		//alert (url);
		$.post(url, 
			{username: $('#id_username').val()}, 
			function(e){
				
				$('#result').html(e);
				if(e.length > 0){ $('#result').fadeIn(); gos = 0;}
				else{ $('#result').fadeOut(); gos = 1;}
				
			})
    		.error(function(e) { alert(e); })

	
	});
$("#id_email").blur(function(event) {
	$('#result').fadeOut();
    /* stop form from submitting normally */      
    /* get some values from elements on the page: */
    var $form = $( this ),
        url = $('#frmsingup').attr( 'action' )  + 'chkemail/';
		$.post(url, 
			{email: $('#id_email').val()}, 
			function(e){
				$('#result').html(e);
				if(e.length > 0) { $('#result').fadeIn(); gos = 0; }
				else {$('#result').fadeOut(); gos = 1;}
				
			})
    		.error(function(e) { alert(e); })

	
	});

$('#frmsingup').submit(function(event)
{
	if (gos == 0) {event.preventDefault(); return false;}
})
});