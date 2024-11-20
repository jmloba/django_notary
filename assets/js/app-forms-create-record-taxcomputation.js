
$(document).ready(function() { 



var amount = document.getElementById('input-amount')
amount.addEventListener('submit',function(event){
  event.preventDefault() // prevent forms from auto submitting
  var input_amount = document.getElementById('input-amount')
  console.log ('amount entered ', input_amount)
  })
  let csrf_token = $('input[name=csrfmiddlewaretoken]').val()



})

  
  
