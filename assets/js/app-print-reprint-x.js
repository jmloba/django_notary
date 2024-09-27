$(document).ready(function(){

  $('#btn-reprint-button').click(function(e){
    e.preventDefault();
    
    let url= $(this).attr('data-url');
    let invoice =$(this).attr("data-invoice")
    let csrf_token = $('input[name=csrfmiddlewaretoken]').val()
    console.log(typeof(invoice))
    console.log('invoice :'+invoice)  
    // pass value to print_invoice_ajax  (app_print:print-invoice-ajax)
    mydata= {
      'new_invoice':Math.floor(invoice),
      'csrfmiddlewaretoken':csrf_token,
    }
    $.ajax({
      url:url,
      data : mydata,
      method :'POST',
      success:function(response){
        if (response.status=='Success'){
          swal(response.status,response.Message,'success')
        }
        if (response.status=='No Record Found') {
          swal(response.status,response.Message,'warning')

        }
      }

    })    
  });


  $('#btn-reportlab-password-protected').click(function(e){
    e.preventDefault();

    console.log(' ***** password protected ccc:')  
    let url= $(this).attr('data-url');
    let mname = 'joven mname'
    // let csrf_token = $('input[name=csrfmiddlewaretoken]').val()
    mydata= {
      'mname':mname,
      // 'csrfmiddlewaretoken':csrf_token,
    }
    $.ajax({
      url:url,
      data : mydata,
      type :'GET',
      success:function(response){
        if (response.status=='Success'){
          swal(response.status,response.Message,'success')
        }
        if (response.status=='No Record Found') {
          swal(response.status,response.Message,'warning')

        }
        if (response.status=='not POST') {
          swal(response.status,response.Message,'warning')

        }


      },
      error:function(response){
        if (response.status=='not POST') {
          swal(response.status,response.Message,'warning')

        }

      }

    })    

  });

  $('#btn-reportlab-invoice-template').click(function(e){
    e.preventDefault();
    console.log(' ***** draw circle')  
    let url= $(this).attr('data-url');
    let mname = 'joven draw circle'
    // let csrf_token = $('input[name=csrfmiddlewaretoken]').val()
    mydata= {
      'mname':mname,
      // 'csrfmiddlewaretoken':csrf_token,
    }
    $.ajax({
      url:url,
      data : mydata,
      type :'GET',
      success:function(response){
        if (response.status=='Success'){
          swal(response.status,response.Message,'success')
        }
      },
   

      

    })       

  });
});
