$(document).ready(function(){

  $('#btn-print-report1').click(function(e){
    e.preventDefault();
    console.log('test dataxxx')
     
    let url= $(this).attr('data-url');
    let passed_data= $(this).attr('data-filtered');
    
    let csrf_token = $('input[name=csrfmiddlewaretoken]').val()
    console.log('test csrf_token', csrf_token)

    mydata={
      'passed_data':passed_data,
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

    });   

  });   

});