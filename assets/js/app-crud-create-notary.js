$(document).ready(function() { 

  function html_record(x)  {
    html_template=''
    for ( i=0; i < x.length; i++ ){
  

      html_template += '<tr id="categ-id-'+x[i].id+'"><td class="editable" data-type="firstname">'+x[i].firstname+'</td><td class="editable" data-type="lastname">'+x[i].lastname+'</td><td class="editable_select" data-type="category">'+x[i].category__doc_category+'</td><td class="editable" data-type="bookno">'+x[i].bookno+'</td><td class="editable" data-type="pageno">'+x[i].pageno+'</td><td class="editable" data-type="recordno">'+x[i].recordno+'</td><td style="width:150px" class="btn-td-block"><button type="button"class="btn btn-warning btn-sm btn-edit  "data-url="" ><span><i class="bi bi-pencil-fill"></i></span></button><button  type="button"class="btn btn-danger btn-sm btn-delete " data-url="#"><span><i class="bi bi-trash3"></i></span></button></td></tr>'      

    }    
    return html_template
  };
  $('.btn-submit-insert-data').click(function(e){
    e.preventDefault();
    url= $(this).attr('data-url')
    
    firstname = $('#ins_firstname').val()
    lastname = $('#ins_lastname').val()
    address = $('#ins_address').val()
    category = $('#ins_category').val()
    bookno = $('#ins_bookno').val()
    pageno = $('#ins_pageno').val()
    recordno = $('#ins_recordno').val()
    if (firstname==''){
      $('#ins_error').text('firstname is required')
      $('#ins_error').show()
      return;
    } else if (lastname==''){
      $('#ins_error').text('lastname is required')
      $('#ins_error').show()
      return;
    }
    else if (address==''){
      $('#ins_error').text('address is required')
      $('#ins_error').show()
      return;
    }
    else if (category==''){
      $('#ins_error').text('category is required')
      $('#ins_error').show()
      return;
    }
    else if (bookno==''){
      $('#ins_error').text('bookno is required')
      $('#ins_error').show()
      return;
    }    
    else if (pageno==''){
      $('#ins_error').text('pageno is required')
      $('#ins_error').show()
      return;
    }    
    else if (recordno==''){
      $('#ins_error').text('recordno is required')
      $('#ins_error').show()
      return;
    } else{

      mydata={'firstname':firstname, 'lastname':lastname, 'address':address,
      'category':category, 'bookno':bookno, 'pageno':pageno,'recordno':recordno


      }
      $.ajax({
        url:url,
        type:'POST',
        data:mydata
      })
      .done(function(response){
        x= response.datalist
        html_template=''
        if (response['error']==false){
          html_template=html_record(x)    
          $('#tbody').html(html_template)                
          $("#ins_error").hide()
          $("#ins_success").text(response['error_message'])
          $("#ins_success").show()
          console.log(response)
        } else{
          $("#ins_success").hide()
          $("#ins_error").text(response['error_message'])
          $("#ins_error").show()

        }


      })
      .fail(function(){
        $("#ins_success").hide()
        $("#ins_error").text(response['error_message'])
        $("#ins_error").show()
      })


    }      



  });
  $('#update_btn').click(function(e){
    $('.editable').each(function(){
      var value = $(this).text();
      var types = $(this).data('type');
      if (types != 'category'){
        var html_data="<input type='text' name='"+types+"' class='form-control input_"+types+"' value='"+value+"'>";
        $(this).html(html_data);

      }else{
        var html_data="<select   name='"+types+"' class='form-control input_"+types+"'>";
        if(value=='Option 1'){
          html_data="<option selected>Option 1</option><option>Option 1</option>";
        }
        else{
          html_data="<option selected>Option 2</option><option>Option 2</option>";
        }
        html_data+="</select>";
        $(this).html(html_data)
   

      }



    })

  })

});
