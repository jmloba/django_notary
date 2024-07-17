
$(document).ready(function(){
//============= load ===============
  var loadForm = function(){
    var btn = $(this);
    console.log ('add record button' )
    
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
          $(".table #tbody").html(data.html_product_list);
          $("#modal-product").modal("hide");

        }else{
          $("#modal-product .modal-content").html(data.html_form)
        }
      }
    });
    return false;

  }
  //============= save button on modal ===============  

  $('.js-create-product').click(loadForm);
  $("#modal-product").on("submit",".js-product-create-form", saveForm)



  //============= Update form  ===============
  /* click edit button in table   class is:-->> js-update-product  */

  $(".product-table #tbody").on("click",".js-update-product", loadForm) 

  $("#modal-product").on("submit",".js-product-update-form", saveForm)

  //============= delete item ===============
  /* click delete button in table   class is:-->> js-delete-product  */
  $(".product-table #tbody").on("click",".js-delete-product", loadForm) 
  $("#modal-product").on("submit",".js-product-delete-form", saveForm)
  //============= delete item ===============

  $(".product-table #tbody").on("click",".js-delete-product", loadForm) 

  
  $("#modal-product").on("submit",".js-product-delete-form", saveForm)





});