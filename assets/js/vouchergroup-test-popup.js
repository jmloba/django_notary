


  function createPopup(id){
    console.log('create popup ---xxx')
    let popup_node = document.querySelector(id);
    let overlay = popup_node.querySelector(".overlay")  
    let closebutton = popup_node.querySelector(".close-btn")
    function openPopup(){
      popup_node.classList.add("active");
    }
    function closePopup(){
      popup_node.classList.remove("active");
    }
    overlay.addEventListener('click', closePopup);
    closebutton.addEventListener('click', closePopup);
    console.log ('before opening')
    return openPopup;
  }
  
  let popup = createPopup('#popup');
  document.querySelector('#open-popup').addEventListener('click',popup);


// for popup sample2
let popup2 = document.getElementById('popup_2');

function open_Popup_2(){
  popup2.classList.add('open-popup-2')

}
function close_Popup_2(){
  popup_2.classList.remove('open-popup-2')

}




