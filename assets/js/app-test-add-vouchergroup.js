$(document).ready(function() { 

  $('#id_accno').change(function (e) {
    e.preventDefault();
    // let url= $(this).attr('data-url');
    url = $('.form-area #id-accno').data('url')
    console.log('url:' , url)

    var e = document.getElementById('id_accno');
    var strSel = "The Value is: " + e.options[e.selectedIndex].value + " and text is: " + e.options[e.selectedIndex].text;
    // alert(strSel);

    var accno =e.options[e.selectedIndex].text
    // $('.ac-name').html(accname)
    mydata={}
    let csrf_token = $('input[name=csrfmiddlewaretoken]').val()
    console.log('accno : ' , accno)
    
    mydata={'csrfmiddlewaretoken':csrf_token,
      'accno':accno, }
        
    $.ajax({
      url : url,
      data:mydata,
      method : 'POST',
      
      success: function(response){
        x=response.data
        // console.log('** successsssss...', x)
        
        html_template=''

        if (response.status=="Success"){
          $('.ac-name').html(x)
          toggleTools()

          
        }
        if (response.status=='failed') {
          $('.ac-name').html(response.Message)
          

        }


      }
      

    })





  });

/* modal  */
  

})