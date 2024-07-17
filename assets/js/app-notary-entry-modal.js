
$(document).ready(function(){
//============= load ===============
  var loadForm = function(){
    var btn = $(this);
    console.log ('add record button notary..' )
    
    url= $(this).attr('data-url')
    console.log('url is :', url)
    $.ajax({
      url :url,
      type : 'get',
      dataType:'json',
      beforeSend:function(){
        
        $('#modal-product .modal-content').html("");
        $('#modal-product').modal('show')
      },
      success: function(data){
        $('#modal-product .modal-content').html(data.html_form)
      }
    });

  }
  //============= save button on modal ===============

  var saveForm = function(){
    var form = $(this);
    url= form.attr('action')
    $.ajax({
      url :url,
      data : form.serialize(),
      type : form.attr('method'),

      dataType:'json',
      success: function(data){
        if (data.form_is_valid){
          $(".table #tbody").html(data.html_notary_list);
          $("#modal-product").modal("hide");

        }else{
          // console.log('data form is not valid ')
          $("#modal-product .modal-content").html(data.html_form)
        }
      }
    });
    return false;

  }
  //============= create ===============
  $('.js-create-notary').click(loadForm);
  $("#modal-product").on("submit",".js-notary-create-form", saveForm)
  //============= Update form  ===============

  $(".product-table #tbody").on("click",".js-update-modal-notary", loadForm) 
  
  $("#modal-product").on("submit",".js-notary-update-form", saveForm)
  //============= delete item ===============
  $(".product-table #tbody").on("click",".js-delete-notary", loadForm) 
  $("#modal-product").on("submit",".js-notary-delete-form", saveForm)


});