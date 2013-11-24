function handle_form(id,callback){
  $(id).submit(function (e) {
    var postData = $(this).serializeArray();
    var formURL = $(this).attr("action");
    $.ajax(
      {
        url: formURL,
        type: "POST",
        data: postData,
        success: function (data, textStatus, jqXHR) {
          if (data["status"] == "ok"){
            callback(data);
          }
          if (data["status"] == "notfound"){
            alert("Item not found in database. Refresh your browser");
          }
          $(id).filter(".todo_form_inner").html(data["formhtml"]);


        },
        error: function (jqXHR, textStatus, errorThrown) {
          alert("Ajax call failed");
        }
      });
    e.preventDefault(); //STOP default action
  });
 };

function handle_edit(item){
  handle_form($(item), function(data){
    $("#form-"+data["id"]).modal('hide');
    $('li#entry-'+data["id"]).html(data["html"]);
    handle_edit($('li#entry-'+data["id"]+" form.edit-form"));
    handle_delete($('li#entry-'+data["id"]+" form.delete-form"));
    $('.modal-backdrop').remove(); // Workaround Bootstrap bug
  });
}
function handle_delete(item){
  handle_form($(item), function(data){
    $('li#entry-'+data["id"]).fadeOut(400,function(){this.remove()});

  });
}
function register_handlers(){
  //Rebind the submit handlers when the list changes
  $("form.delete-form").each(function(){
    handle_delete(this);
  });
  $("form.edit-form").each(function(){
    handle_edit(this);
  });

}

$(document).ready(function () {
  handle_form($("#newform"),function(data){
    $('ul#todolist').append(data["html"]);
    //Bind handlers
    handle_edit($('ul#todolist li:last-child form.edit-form'));
    handle_delete($('ul#todolist li:last-child form.delete-form'));
    $('#newform input[type="text"]').val("");
    $('#newform textarea').val("");

  });
  register_handlers();
});