function handle_form(id,callback){
  $(id).submit(function (e) {
    var postData = $(this).serializeArray();
    var formURL = $(this).attr("action");
    $(this).find('input[type="submit"]').removeClass("btn-primary").addClass("btn-warning");
    $.ajax(
      {
        url: formURL,
        type: "POST",
        data: postData,
        success: function (data, textStatus, jqXHR) {
          console.log(data);
          if (data["status"] == "ok"){
            callback(data);
          }
          if (data["status"] == "notfound"){
            alert("Item not found in database. Refresh your browser");
          }
          $(id).filter(".todo_form_inner").html(data["formhtml"]);

          register_handlers(); //Make sure to update the handler bindings
        },
        error: function (jqXHR, textStatus, errorThrown) {
          alert("Ajax call failed");
        }
      });
    e.preventDefault(); //STOP default action
  });
 };


function register_handlers(){
  //Rebind the submit handlers when the list changes
  $("form.delete-form").each(function(){
    handle_form(this, function(data){
      $('li#entry-'+data["id"]).remove();
    });
  });
  $("form.edit-form").each(function(){
    handle_form(this, function(data){
      $("#form-"+data["id"]).modal('hide');
      $('li#entry-'+data["id"]).html(data["html"]);
      $('.modal-backdrop').remove(); // Workaround Bootstrap bug

    });
  });
}

$(document).ready(function () {
  handle_form("#newform",function(data){
      $('ul#todolist').append(data["html"])
    });
  register_handlers();
});