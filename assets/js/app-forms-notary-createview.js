const inputImg_myfile = document.getElementById('myfile')
const inputImg_myimage = document.getElementById('myimage')

const img_myimage = document.getElementById('display_myimage')

const img_myfile = document.getElementById('display_myfile')


function getImg(event){
     const file = event.target.files[0]; // 0 = get the first file

     // console.log(file);

     let url = window.URL.createObjectURL(file);

     // console.log(url)

     img_myimage.src = url
}
function getmyfile(event){
const file = event.target.files[0]; // 0 = get the first file

// console.log(file);

let url = window.URL.createObjectURL(file);

// console.log(url)

img_myfile.src = url
}

inputImg_myimage?.addEventListener('change', getImg)

inputImg_myfile?.addEventListener('change', getmyfile)