
$(document).ready(function() { 


  let clear_data_entries=() =>{
    // $('#stuid').val('')
    $('#id_category').val('')
    $('#id_firstname').val('')
    $('#id_lastname').val('')

    // $('#id_bookno').val('')
    // $('#id_pageno').val('')
    // $('#id_recordno').val('')
    // $('#id_amount_paid').val('')

    };
    function html_record(x)  {
      html_template=''
      for ( i=0; i < x.length; i++ ){
        html_template +=' <tr id="categ-id-'+x[i].id+'"><td><img src="/media/'+x[i].myimage+'" alt="pic" class="item-image-size-inlist" ></td><td class="td-text td-text-name">'+x[i].firstname+'</td><td class="td-text  td-text-name">'+x[i].lastname+'</td><td class="td-text-category">'+x[i].category__doc_category+'</td><td class="td-text-ref">'+x[i].bookno+'</td><td class="td-text-ref">'+x[i].pageno+'</td><td class="td-text-ref">'+x[i].recordno+'</td><td class="td-amount">'+x[i].amount_paid+'</td><td><button class="btn btn-info btn-sm"  id="btn-notary-sample1-edit"  data-sid="'+x[i].id+'" data-url="/app_notary/notary-edit/"><i class="bi bi-pencil"></i></button> &emsp;  <button class="btn btn-danger btn-sm"  id="btn-notary-sample1-delete"  data-sid="'+x[i].id+'" data-url="/app_notary/notary-delete/"><i class="bi bi-trash3"></i></button></td></tr>'
  
      }    
      return html_template
    };    
    $('kalimutan  #btn-saveForm1-notary').click(function(e){
      e.preventDefault();
      console.log('ajax begin')
  
      var fd = new FormData()
      let html_template=''
      let csrf_token = $('input[name=csrfmiddlewaretoken]').val()
      
      let id = $('#stuid').val()  
      let category = $('#id_category').val()  
      let firstname = $('#id_firstname').val()  
      let lastname = $('#id_lastname').val()  
      
      // let bookno = $('#id_bookno').val()  
      // let pageno = $('#id_pageno').val()  
      // let recordno = $('#id_recordno').val()  
      // let amount_paid = $('#id_amount_paid').val()  
    
      let url= $(this).attr('data-url');  // save notary
      
  
      mythis = $(this)
      mydata={}
  
      if (firstname==''){
        swal('Please enter firstname','firstname is required ','error')
      } else if (lastname==''){
        swal('Please enter lastname','lastname is required ','error')
      } else {

          
      // if (category==''){
      //   swal('Please enter category','Category is required ','error')
      // } else
        fd.append('csrfmiddlewaretoken', csrf_token )
        fd.append('stuid', id )              
        fd.append('lastname', lastname )
        fd.append('firstname', firstname )
        
        
        fd.append('category', category )
        // fd.append('bookno', bookno )
        // fd.append('pageno', pageno )
        // fd.append('recordno', recordno )
        // fd.append('amount_paid', amount_paid )      
        
        // fd.append('myfile', $('#id_myfile')[0].files[0] )
        // fd.append('myimage', $('#id_myimage')[0].files[0] )
        console.log('end - begin-ajax app-forms-entry.js')

          $.ajax({
            url: url,
            method : 'POST',
            data : fd,
            cache: false,
            processData:false,
            contentType: false,
            enctype:'multipart/form-data',

            success: function(data){  
              x= data.datalist
              console.log('** success -->> datalist : ', x)
              html_template=''
              if (data.status=='Success'){
                swal('Data has been Saved','Record has been saved','success')
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

    $('kalimutan #tbody').on('click','#btn-notary-sample1-delete', function(e){
      e.preventDefault();
      console.log('btn delete')
      
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
  
            }
          if (data.status==0) {
              console.log('student --- unable to deleted')
            }
        },
      })  
  
    });
  

  });