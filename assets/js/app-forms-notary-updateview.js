// $(window).ready(function(){

// })

$(document).ready(function(){
  
  // alert('document is ready')
  $('#button1').click(function(e){
    e.preventDefault();

    alert('button is clicked')
  })

  // SAMPLE FUNCTION 

  function runFunction(a,b){
    mtotal = a + b
    return mtotal
  }
  
  mtotal= runFunction(2,1)
  console.log('mtotal : ', mtotal)

  // displaying image
  const image_input = document.getElementById('myimage')
  const disp_myimage = document.getElementById('image-view')
  
  function getImgData() {
    const files = image_input.files[0];
    if (files) {
      const fileReader = new FileReader();
      fileReader.readAsDataURL(files);
      fileReader.addEventListener("load", function () {
        disp_myimage.style.display = "block";
        disp_myimage.innerHTML = '<img src="' + this.result + '" />';
      });    
    }
  }

  image_input.addEventListener("change", function () {
    getImgData();
  });

})