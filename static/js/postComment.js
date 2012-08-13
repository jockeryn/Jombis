
function postComment(id){
				txtcomment = "";		
  					$('textarea.mention').mentionsInput('val', function(data) {
      		txtcomment = JSON.stringify(data);   			
    	});
  					tm = new Date();
  					mes = tm.getMonth()+1;
  					ahora = tm.getFullYear()+'-'+mes+'-'+tm.getDate()+' '+tm.getHours()+':'+tm.getMinutes()+':'+tm.getSeconds();
  					
  					$.post("/comments/post/", {
  						name:$('#id_name').val(),
  						email:$('#id_email').val(),
  						url:$('#id_url').val(),
  						comment:txtcomment,
  						honeypot:$('#id_honeypot').val(),
  						content_type:$('#id_content_type').val(),
  						object_pk:id,
  						timestamp:$('#id_timestamp').val(),
  						security_hash:$('#id_security_hash').val()
  					},
   						function(data) {
     					$('#comentList').prepend('<article class="comentario"><table><tr><td valign="top"><div class="imgComment"><a href="/'+user+'/"><img src="'+avatar+'" width="32"/></a></div></td><td><div><a href="/'+user+'" class="userNameLink">'+user+'</a><span class="comentText"> '+ txtcomment + '<div><time class="timeago" datetime=\''+ahora+'\'></time></div></span></div></td></tr></table></article>');
     					$('#id_comment').val('');
              resizeComentList();
     					$("time.timeago").timeago();
  					 }).error(function(){alert('error')});
            mCustomScrollbars();
  				
}
function loadComment(tipo, id){
   $('#comentList').html('cargando...');

              var api = $('.scroll-pane').jScrollPane(
          {
            showArrows:true,
            maintainPosition: false
          }
        ).data('jsp');

              api.getContentPane().load("/comments/load/"+tipo+"/"+id+"/", 
              function(data) {              
                api.reinitialise();
                data = data.replace(/&lt;/gi,'<');
                data = data.replace(/&quot;/gi,'"');
                data = data.replace(/&gt;/gi,">")
                data = data.replace(/\\/gi, "")
                $('#comentList').html(data);
                $("time.timeago").timeago();
            }
            
          );
              
        }

function refreshFormComment(id){
   $.post("/comments/loadFrm/"+id+"/", { 
              id: id }, 
              function(data) {
                data = data.replace(/&lt;/gi,'<');
                data = data.replace(/&quot;/gi,'"');
                data = data.replace(/&gt;/gi,">");
                data = data.replace(/\\/gi, "");
                $('#cmntFrm').html(data);
            })
            .success(function() { $("time.timeago").timeago(); reScroll(); })
            .error(function() { alert('error')});
}

function makeExpresiones(){
  id = "";
  $('img.menu_class').click(function () {
    $('.the_menu').fadeOut();
    $('#ul' + this.id).slideToggle('medium');
    id = this.id;
    //alert('#ul' + id + ' li a');
  });
  $('.optXpresion').click(function () {
    $('#ul' + id).fadeOut();
  });
}
function reScroll(){
  var api = $('.scroll-pane').jScrollPane(
          {
            showArrows:true,
            maintainPosition: false
          }
        ).data('jsp');
      
}