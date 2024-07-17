$(document).ready(function(){

  let clear_data_entries=() =>{
    $('#stuid').val('')
    $('#id_doc_category').val('')
    
    };
  function html_record(x)  {
    html_template=''
    for ( i=0; i < x.length; i++ ){



      html_template += '<tr  id="categ-id-'+x[i].id+'" ><th scope="row">>'+x[i].doc_category+'</th><td><button class="btn btn-danger btn-sm"data-sid="'+x[i].id+'" id="btn-category-delete" data-url="/app_notary/notary-category-delete/ "><i class="bi bi-trash"></i></button></td></tr>'

    }    
    return html_template
  };
  

  $('#btn-save-notary-category').click(function(e){
    e.preventDefault();
    
    let html_template=''
    let id = $('#stuid').val()
    let category = $('#id_doc_category').val()  

    let url= $(this).attr('data-url');  // save_notary_category
    let csrf_token = $('input[name=csrfmiddlewaretoken]').val()

    mythis = $(this)
    mydata={}

    if (category==''){
      swal('Please enter category','Category is required ','error')
    } else{


      console.log('ready to save')
      mydata={'csrfmiddlewaretoken': csrf_token,
        'stuid':id,
        'category': category}
      console.log('>>> mydata',mydata)

      $.ajax({
        url: url,
        method : "POST",
        data : mydata,    
        success: function(data){  
          x= data.datalist
          console.log('** success -->> datalist : ', x)

          html_template=''
          if (data.status=='Success'){
            swal('Data has been Saved','Record has been saved','success')
            console.log('returned record ',x)
            html_template=html_record(x)

            $('#tbody').html(html_template)

            $('#category_form')[0].reset()

            clear_data_entries()
          }
        }        
      })   
    }   
  })  
  
})  