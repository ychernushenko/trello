  $(onPageLoad);

  function onPageLoad()
  {
    $( ".column" ).sortable({
      connectWith: ".column",
      handle: ".portlet-header",
      cancel: ".portlet-toggle",
      start: function (event, ui) {
        ui.item.addClass('tilt');
      },
      stop: function (event, ui) {
        ui.item.removeClass('tilt');
        var csrf_token = Cookies.get('csrftoken');
 
	// save update of position to a server
        $.ajax({
                url : "/trello/update_pos",
                type : "POST",
                dataType: "json",
                data : {
                    task_id : ui.item.data("id"),
                    status_id: ui.item.context.parentNode.id,
                    csrfmiddlewaretoken: csrf_token,
                },
                success : function(json) {
                    //console.log("Saved position update: " + json.status);
                },
                error : function(xhr,errmsg,err) {
                    console.log("Error position update: " + xhr.status + ": " + xhr.responseText);
                }
        });

    },
      placeholder: "portlet-placeholder ui-corner-all"
    });

    $( ".portlet" )
      .addClass( "ui-widget ui-widget-content ui-helper-clearfix ui-corner-all" )
      .find( ".portlet-header" )
        .addClass( "ui-widget-header ui-corner-all" )
        .prepend( "<span class='portlet-toggle'></span>");

    $( ".portlet-toggle" ).click(function() {
        var icon = $( this );
        icon.toggleClass( "ui-icon-minusthick ui-icon-plusthick" );
        icon.closest( ".portlet" ).find( ".portlet-content" ).toggle();
    });
  }
