
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
      // url= form.attr('action')
      // let csrf_token = $('input[name=csrfmiddlewaretoken]').val()
      // var category = $('#id_category').val()
      // var firstname = $('#id_firstname').val()
      // var amount_page = $('#id_amount_page').val()
      // let image = document.getElementById('id_photo')

      
      // var fd = new FormData();
      // fd.append('csrfmiddlewaretoken',csrf_token)
      // fd.append('category',category)
      // fd.append('firstname',firstname)    
      // fd.append('amount_page',amount_page)
      // // fd.append('photo', image.files[0])
      var fd = new FormData(this);

      $.ajax({
        url :url,
        data : fd,
        // data:  form.serialize(),
        type : form.attr('method'),
        processData: false,
        contentType: false,
  
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
  
    $(".product-table #tbody").on("click",".js-update-modal-ver2-notary", loadForm) 

    $("#modal-product").on("submit",".js-notary-v2-update-form", saveForm)

    
    // //============= delete item ===============
    $(".product-table #tbody").on("click",".js-delete-v2-notary", loadForm) 
    $("#modal-product").on("submit",".js-notary-v2-delete-form", saveForm)
  
  
  });