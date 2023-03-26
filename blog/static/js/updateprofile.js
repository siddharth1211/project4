const profileForm = document.getElementById("profile-form");
const alertBox = document.getElementById("alert-box");
const cancelBtn = document.getElementById("cancel-btn");
const input = document.getElementById("id_user_image");
const progressBar = document.getElementById("progress-bar");
const csrf = document.getElementsByName("csrfmiddlewaretoken");
console.log("----------------------------------------------")
if (input == undefined && input === null) {
  console.log("not ok");
}

input.addEventListener("change", ()=>{
console.log("----------------------------------------------")

console.log(csrf[0].value);
console.log(input.files[0]);
const fd = new FormData();
fd.append('csrfmiddlewaretoken', csrf[0].value);
fd.append('image', input.files[0]);
console.log(fd);
cancelBtn.classList.remove("not-visible");

$.ajax(
{
type: "POST",
url: profileForm.action,
data: fd,
enctype: "multipart/form-data",
beforeSend: function(){

progressBar.classList.remove("not-visible");
cancelBtn.classList.remove("not-visible");

},
xhr: function(){
const xhr = new window.XMLHttpRequest();
xhr.upload.addEventListener("progress", (e)=>
{
if (e.lengthComputable)
{
const percent = (e.loaded/e.total)*100;
//console.log(percent);
progressBar.innerHTML = `<div class="progress">
  <div class="progress-bar" role="progressbar" style="width: ${ percent.toFixed(1) }%" aria-valuenow="${ percent.toFixed(1) }" aria-valuemin="0" aria-valuemax="100"></div>
</div>
<p>${ percent.toFixed(1) } </p>`

}


}

)

cancelBtn.addEventListener("click", ()=>
{

xhr.abort();
progressBar.classList.add("not-visible");
profileForm.reset();
cancelBtn.classList.add("not-visible");
}
)


return xhr
},
success: function(){
           progressBar.classList.add("not-visible");
           alertBox.innerHTML = `<div class="alert alert-warning" role="alert">
  image uploaded!
</div>
`
cancelBtn.classList.add("not-visible");
           console.log("hii");
},
error: function(error){

console.log(error);

},
cache: false,
contentType:false,
processData: false

}
)


}
)


