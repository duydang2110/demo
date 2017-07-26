$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-asset").modal("show");
      },
      success: function (data) {
        $("#modal-asset .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#asset-table tbody").html(data.html_asset_list);
          $("#modal-asset").modal("hide");
        }
        else {
          $("#modal-asset .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create book
  $(".js-create-asset").click(loadForm);
  $("#modal-asset").on("submit", ".js-asset-create-form", saveForm);

  // Update book
  $("#asset-table").on("click", ".js-update-asset", loadForm);
  $("#modal-asset").on("submit", ".js-asset-update-form", saveForm);

  // Delete book
$("#asset-table").on("click", ".js-delete-asset", loadForm);
$("#modal-asset").on("submit", ".js-asset-delete-form", saveForm);

});