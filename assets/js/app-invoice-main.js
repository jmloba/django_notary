$(document).ready(function(){
  let clear_data_entries=() =>{
    $('#stuid').val('')
    $('#id_description').val('')
    $('#id_customer').val('')
   }  

  const alertBox = document.getElementById('alert-box')
  const handleAlerts =(type, text)=>{
  
    alertBox.innerHTML=`<div class="alert alert-${type}" role="alert">
                         ${text}
                      </div>`
  }

  function  reformat(mdate){
    console.log(mdate)
  mdate='joven'
  return mdate
  
  }

  function html_record(x)  {
    html_template=''
    for ( i=0; i < x.length; i++ ){
      html_template+='   <tr id="invoice-id-'+x[i].id+'" ><th scope="row">'+x[i].customer__name+'</th><td>'+x[i].invoice_date+'</td><td>'+x[i].itemnumber+'</td><td>'+x[i].description+'</td><td id="rec-quantity-'+x[i].id+'">'+x[i].quantity+'</td><td>'+x[i].price+'</td><td id="rec-amount-'+x[i].id+' ">'+x[i].amount+'</td><td><button class="btn btn-info btn-sm"  data-sid="'+x[i].id+'"    id="btn-invoice-edit" data-url="/app_invoice/invoice-edit/">  <i class="bi bi-pencil"></i> </button>&ensp;&ensp;&ensp;<button class="btn btn-danger btn-sm"  data-sid="'+x[i].id+'"  id="btn-invoice-delete" data-url="/app_invoice/invoice-delete/"> <i class="bi bi-trash3"></i></button></td> </tr>'
    }    
    return html_template
  }

  $('#btn-create-invoice').click(function(e){
    e.preventDefault();

    let html_template=''
    let id = $('#stuid').val()  
    let customer = $('#id_customer').val()  
    let itemnumber = $('#id_itemnumber').val()  
   
    let description = $('#id_description').val()  
    let quantity = $('#id_quantity').val()  
    let price = $('#id_price').val()  


    let url= $(this).attr('data-url');
    let csrf_token = $('input[name=csrfmiddlewaretoken]').val()
    mythis = $(this)
    mydata={}

    console.log ('id', id)
    console.log ('customer', customer)
    console.log ('description', description)

    if (customer=='' || customer == null){
      swal('Please enter customer','Customer is required ','error')
    }else if (description==''){
      swal('Please enter description','Description is required ','error')
    }else  if (quantity==''){
      swal('Please enter quantity','Quantity is required ','error')
    }else  if (price ==''){
      swal('Please enter price','Price is required ','error')
    } else {
      mydata={'csrfmiddlewaretoken':csrf_token,
      'stuid':id, 
      'itemnumber': itemnumber,
      'description':description,
      'customer':customer,
      'quantity': quantity, 'price':price
      }
      
      $.ajax({
        url: url,
        method : 'POST',
        data : mydata,
        success: function(data){  
          console.log('** successsssss...')
          x= data.invoice_data
        
          html_template=''
          if (data.status=='Success'){
            swal('Data has been Saved','Record saved'+x.length,'success')
            // create a record to display in table
            html_template=html_record(x)


            $('#tbody').html(html_template)
            $('#invoiceForm')[0].reset()
            clear_data_entries()
            console.log('total quantity', data.invoice_total_qty)
            console.log('total amount', data.invoice_amount)
            $('#sum-total-qty').html( data.invoice_total_qty)
            $('#sum-total-amount').html(data.invoice_amount)

            

          }
        }
      });
    }// end else
  });
  function html_record2(x)  {
    html_template=''
    for ( i=0; i < x.length; i++ ){
      html_template+=' <tr id="invoice-id-'+x[i].id+'" ><th scope="row">'+x[i].itemnumber+'</th><td>'+x[i].description+'</td><td  id="rec-quantity-'+x[i].id+'" >'+x[i].quantity+'</td><td>'+x[i].price+'</td><td id="rec-amount-'+x[i].id+'">'+x[i].amount+'</td><td><button class="btn btn-info btn-sm"data-sid="'+x[i].id+'" id="btn-invoice-edit2"data-url="/app_invoice/invoice-edit2/"><i class="bi bi-pencil"></i></button>&ensp;&ensp;&ensp;<button class="btn btn-danger btn-sm"data-sid="'+x[i].id+'" id="btn-invoice2-delete"data-url="/app_invoice/invoice2-delete/"><i class="bi bi-trash3"></i></button></td></tr>'
    }    
    return html_template

  }  
  $('#btn-create-invoice2').click(function(e){

    e.preventDefault();
    console.log ('save invoice version 2 ')
    let html_template=''
    let id = $('#stuid').val()  
    let itemnumber = $('#id_itemnumber').val()  
    let description = $('#id_description').val()  
    let quantity = $('#id_quantity').val()  
    let price = $('#id_price').val()  
    let url= $(this).attr('data-url');
    let csrf_token = $('input[name=csrfmiddlewaretoken]').val()
    mythis = $(this)
    mydata={}
    console.log ('button -> item entry 2 -> ,id', id, 'description',description, ' quantity:', quantity, ' Price : ',price)
    if (itemnumber==''){
      swal('Please enter itemnumber','Item NUmber is required ','error')
    }else  if (description==''){
      swal('Please enter description','Description is required ','error')
    }else  if (quantity==''){
      swal('Please enter quantity','Quantity is required ','error')
    }else  if (price ==''){
      swal('Please enter price','Price is required ','error')
    } else {
      mydata={'csrfmiddlewaretoken':csrf_token,
        'stuid':id, 
        'itemnumber': itemnumber,
        'description':description,
        'quantity': quantity, 'price':price
        }
        $.ajax({
          url: url,
          method : 'POST',
          data : mydata,
          success: function(data){  
            console.log('** successsssss...')
            x= data.invoice_data
          
            html_template=''
            if (data.status=='Success'){
              swal('Data has been Saved','Record saved'+x.length,'success')
              // create a record to display in table
              html_template=html_record2(x)
  
  
              $('#tbody').html(html_template)
              $('#invoiceForm')[0].reset()
              clear_data_entries()
              console.log('total quantity', data.invoice_total_qty)
              console.log('total amount', data.invoice_amount)
              $('#sum-total-qty').html( data.invoice_total_qty)
              $('#sum-total-amount').html(data.invoice_amount)
  
              
  
            }
          }
        });

    }

    


  });    



  $('#btn-get-date-formvalues').click(function(e){
    e.preventDefault();
    console.log('get form inputs')
    let mdt_date = $('#dt-date').val()  
    let mdt_datetime = $('#dt-datetime').val()  
    let mdt_datetime_local = $('#dt-datetime-local').val()      

    console.log('dt_date : ', mdt_date)
    console.log('dt_datetime : ', mdt_datetime)
    console.log('dt_date_local : ', mdt_datetime_local)        
  });

  $('#btn-read-invoice-file').click(function(e){  
    e.preventDefault();
    console.log(' *** read invoice file button ')
    let url= $(this).attr('data-url');
    let mdt_date = $('#dt-date').val()  
    let csrf_token = $('input[name=csrfmiddlewaretoken]').val()
    

    mydata={'mdt_date':mdt_date,'csrfmiddlewaretoken':csrf_token,}

    $.ajax({
      type : 'POST',
      url:url,
      data:mydata,
      success:function(response){
        x= response.invoice_data
        if (response.status=='Success'){
          html_template=''
          for ( i=0; i < x.length; i++ ){
            html_template += '<tr id="invoice-id-'+x[i].item_no+'"><th scope="row">'+x[i].customer__name+'</th><td>'+x[i].invoice_date+'</td><td>'+x[i].description+'</td><td>'+x[i].quantity+'</td><td>'+x[i].price+'</td><td>'+x[i].amount+'</td><td><button class="btn btn-info btn-sm"data-sid="'+x[i].item_no+'" id="btn-invoice-edit"data-url="/app_invoice/invoice-edit/"><i class="bi bi-pencil"></i></button>&ensp;&ensp;&ensp;<button class="btn btn-danger btn-sm"data-sid="'+x[i].item_no+'" id="btn-invoice-delete"data-url="/app_invoice/invoice-delete/"><i class="bi bi-trash3"></i></button></td></tr>'

          }
    
          $('#tbody').html(html_template)  
        }else if (response.status=='Failed'){
          // const sText = `Failed ${response.first_name}`
          const sText = `Failed`
          handleAlerts('success',sText)
          setTimeout(()=>{
            // clear entries
            alertBox.innerHTML=''
          },2000)          


        }


        

      }

      

    })
    
  })
  $('#tbody').on('click','#btn-invoice-delete', function(e){
    e.preventDefault()
    console.log('button delete ')
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
        console.log(data)
        if (data.status==1){
          console.log('Item  deleted')
          $(mythis).closest("tr").fadeOut()
            // swal(response.status,response.message,'success')
            $('#sum-total-qty').html(data.invoice_total_qty)
            $('#sum-total-amount').html(data.invoice_amount)
          }
        if (data.status==0) {
            console.log('student --- unable to deleted')
          }
      },
    })    
  })

  $('#tbody').on('click','#btn-sales-entry-delete', function(e){
    console.log ('btn-sales-entry-delete')


  })

  $('#tbody').on('click','#btn-invoice2-delete', function(e){
    e.preventDefault()
    console.log('invoice 2 delete') 
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
        console.log(data)
        if (data.status==1){
          console.log('Item  deleted')
          $(mythis).closest("tr").fadeOut()
            // swal(response.status,response.message,'success')
            $('#sum-total-qty').html(data.invoice_total_qty)
            $('#sum-total-amount').html(data.invoice_amount)
          }
        if (data.status==0) {
            console.log('student --- unable to deleted')
          }
      },
    })  
  
  })

  $('#tbody').on('click','#btn-invoice-edit', function(e){
    e.preventDefault()  
    console.log ('btn-edit')
    let id = $(this).attr("data-sid")
    var csrf_token = $('input[name=csrfmiddlewaretoken]').val()
    url= $(this).attr('data-url');
    mydata= {
      'sid':id ,
      'csrfmiddlewaretoken':csrf_token,
    }
    $.ajax({
      url:url,
      method :"POST",
      data : mydata,
      success:function(data){
        console.log('data--->js', data)

        $('#stuid').val(data.id)  
        $('#id_description').val(data.description)

        $('#id_customer').val('zzz')
      
        console.log('customer name: ???', data.customer_name)
        console.log('customer id:', data.id )
        
      },
      
    })
  


  })   

  $('#tbody').on('click','#btn-invoice-edit2', function(e){
    e.preventDefault()  
    console.log ('btn-edit')
    let id = $(this).attr("data-sid")
    var csrf_token = $('input[name=csrfmiddlewaretoken]').val()
    url= $(this).attr('data-url');
    mydata= {
      'sid':id ,
      'csrfmiddlewaretoken':csrf_token,
    }
    $.ajax({
      url:url,
      method :"POST",
      data : mydata,
      success:function(data){
        console.log('data--->js', data)

        $('#stuid').val(data.id)  
        $('#id_itemnumber').val(data.itemnumber)       
        $('#id_description').val(data.description)        
        $('#id_quantity').val(data.quantity)
        $('#id_price').val(data.price)

        
        
        console.log('customer id:', data.id )
        
      },
      
    })
  


  })   
  $('#create-an-invoice').click(function(e){
    e.preventDefault();
    console.log('create an invoice ')
    var csrf_token = $('input[name=csrfmiddlewaretoken]').val()
    url= $(this).attr('data-url');
    mydata= {
      'csrfmiddlewaretoken':csrf_token,
    }
    $.ajax({
      url:url,
      method :"POST",
      data : mydata,
      success:function(data){
        x= data.invoice_data
        if (data.status=='Success'){
          console.log(data)

          // create a record to display in table
          html_template=html_record(x)
          $('#tbody').html(html_template)
          $('#sum-total-qty').html( data.invoice_total_qty)
          $('#sum-total-amount').html(data.invoice_amount)          
        }
        // $('#stuid').val(data.id)  
        // $('#id_description').val(data.description)
        // $('#id_customer').val('zzz')
      },
      
    })
  })   


  $('#print-invoice').click(function(e){
    e.preventDefault();

    console.log('print invoice now')

    var csrf_token = $('input[name=csrfmiddlewaretoken]').val()
    url= $(this).attr('data-url');

    mydata= {
      'csrfmiddlewaretoken':csrf_token,
    }    

    $.ajax({
      url:url,
      method :"POST",
      data : mydata,
      success:function(data){
        // x= data.invoice_data
        if (data.status=='Success'){
          console.log(data)
          console.log('new invoice :', data.new_invoice)
          // create a record to display in table
          swal('Printing',data.mval,'success')

        }
        

        // $('#stuid').val(data.id)  
        // $('#id_description').val(data.description)
        // $('#id_customer').val('zzz')
      

        
      },
      
    })    
  });  
  function selectElement(id, valueToSelect) {    
    let element = document.getElementById(id);
    element.value = valueToSelect;
}

//============= load ===============
var loadForm_search = function(){
  var btn = $(this);
  console.log ('add record button' )
  
  url= $(this).attr('data-url')
  console.log('url is :', url)
  $.ajax({
    url :url,
    type : 'get',
    dataType:'json',
    beforeSend:function(){
      console.log('before search')
      
      $('#modal-product .modal-content').html("");
      $('#modal-product').modal('show')
    },
    success: function(data){
      console.log ('success search ', data.status)
      // $('#modal-product .modal-content').html(data.html_form)
    }
  });

}
// ====== search product


// $('#js-search-product').click(loadForm_search);
 

}); // end maindoc