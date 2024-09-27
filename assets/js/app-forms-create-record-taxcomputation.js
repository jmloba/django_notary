
$(document).ready(function() { 

  const  another_button = document.getElementById('btn-sample1')
  const  text_display = document.getElementById('count_cookie')
  let cookie_counter = 0
  // another_button.addEventListener('click',do_something)

  another_button.addEventListener('click',do_count_click)
  function do_count_click(){
    cookie_counter += 1
    text_display.innerText = cookie_counter
  }

  function do_something(){  
    alert('hello world')
  }
  const  my_header_id = document.getElementById('btn-change-theme')

  my_header_id.addEventListener('click',changeId)

  // my_header_id.addEventListener('mouseover',changeId)

  function changeId(){
    var element = document.getElementById('header-form');
    element.id='blue'

  }

/*
// joven- to print to console all keys that has been pressed  

window.addEventListener  ('keydown', function(e){
  console.log('you pressed', e.code)

})

*/


const amount_entered = document.getElementById('amount-entered')

const  input_amount = document.getElementById('input-amount')

input_amount.addEventListener("input",function(e){
  console.log(e.target.value)
    
  amount_entered.innerText = "Amount: " + e.target.value



})

})

  
  
