$(document).ready(function(){

  $('.save-newrecord-ajax').click(function(e){
    
    console.log('saving time')
    var $myform = $(".new_AccountCreate")
    $myform.submit(function(event){
      event.preventDefault()
      var $formData = $(this).serialize()
      console.log( $formData) 
      var $endpoint = $myform.attr('data-url')
      console.log( $endpoint) 
      $.ajax({
        method :'POST',
        url : $endpoint ,
        data :$formData ,
        success: handleFormSuccess,
        error : handleFormFailed,
      })
      function handleFormSuccess(data,textStatus,URL){
        console.log(data)
        console.log(textStatus)
        console.log(jqXHR)
        $myform.reset();
      }
      function handleFormFailed(jqXHR,textStatus,errorThrown){
        console.log(jqXHR)
        console.log(textStatus)
        console.log(errorThrown)

      }


    })

  })

  

})