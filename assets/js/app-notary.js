$(document).ready(function(){
  
  let clear_data_entries=() =>{
    $('#stuid').val('')
    $('#id_category').val('')
    $('#id_firstname').val('')
    $('#id_lastname').val('')
  }  
  
  const alertBox = document.getElementById('alert-box')

  const handleAlerts =(type, text)=>{
    alertBox.innerHTML=`<div class="alert alert-${type}" role="alert"> ${text}</div>`
  } 
  function html_record(x)  {
    html_template = ''
    for ( i=0; i < x.length; i++ ){


      html_template += '<tr id="categ-id-'+x[i].id+'"><td>'+x[i].firstname+'</td><td>'+x[i].lastname+'</td><td>'+x[i].category__doc_category+'</td><td><button class="btn btn-danger btn-sm" data-sid="'+x[i].id+'" id="btn-notary-delete"data-url="/app_notary/notary-delete/"><i class="bi bi-trash3"></i></button></td></tr> '


    }    
    return html_template
  }

  $('#btn-notary-delete').click(function(e){
    e.preventDefault();
    console.log('btn notry delete ')
    
    
    let id = $(this).attr("data-sid")
    var csrf_token = $('input[name=csrfmiddlewaretoken]').val()
    url= $(this).attr('data-url');
    mydata= {
      'sid':id ,
      'csrfmiddlewaretoken':csrf_token,
    }
    mythis = $(this)
    console.log ('mydata   : ', mydata)
    $.ajax({
      url:url,
      method :"POST",
      data : mydata,
      success:function(data){
        console.log('returned data-->>',data)
        if (data.status==1){
          console.log('Item  deleted')
          $(mythis).closest("tr").fadeOut()
            // swal(response.status,response.message,'success')
            // $('#sum-total-qty').html(data.invoice_total_qty)
            // $('#sum-total-amount').html(data.invoice_amount)
          }
        if (data.status==0) {
            console.log('student --- unable to deleted')
          }
      },
    })  

  })  

  $('#btn-save-notary').click(function(e){
    e.preventDefault();
    console.log('btn save ')
    let html_template=''
    
    let id = $('#stuid').val()  
    let category = $('#id_category').val()  
    let firstname = $('#id_firstname').val()  
    let lastname = $('#id_lastname').val()  
    let url= $(this).attr('data-url');  // save notary
    let csrf_token = $('input[name=csrfmiddlewaretoken]').val()
    mythis = $(this)
    mydata={}
    console.log ('id', id)
    console.log ('category', category)
    console.log ('firstname', firstname)
    console.log ('lastname', lastname)
    if (category==''){
      swal('Please enter category','Category is required ','error')
    } else if (firstname==''){
      swal('Please enter firstname','firstname is required ','error')
    } else if (lastname==''){
      swal('Please enter lastname','lastname is required ','error')
    } else {
      mydata={'csrfmiddlewaretoken':csrf_token,
        'stuid':id, 
        'category': category,
        'firstname':firstname,
        'lastname':lastname,
        }
        $.ajax({
          url: url,
          method : 'POST',
          data : mydata,
          success: function(data){  
            console.log('** successsssss...')
            mfirst= data.firstname
            console.log('',mfirst)
            x= data.datalist

            html_template=''
            if (data.status=='Success'){
              swal('Data has been Saved','Record :'+mfirst,'success')
              console.log('returned record ',x)

              html_template=html_record(x)

              $('#tbody').html(html_template)

              $('#notary_entry_form')[0].reset()

              clear_data_entries()
            }
          }
        });  

    }
   
   
  });



  

});