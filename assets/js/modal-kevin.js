const modal_kevin =document.querySelector('#modal-bykevin')

const openModal = document.querySelector('.open-btn-modal')
const closeModal = document.querySelector('.close-btn-modal')

openModal.addEventListener('click',()=>{
  modal_kevin.showModal();
})

closeModal.addEventListener('click',()=>{
  modal_kevin.close();
})