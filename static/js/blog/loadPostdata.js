const postsBox = document.getElementById('posts-box');
const spinnerBox = document.getElementById('spinner-box');
const loadBtn = document.getElementById('load-btn');
const endBox = document.getElementById('end-box');
const postLike = document.getElementById('post-like');
const editBox = document.getElementById('post-edit-box');
const editblogForm = document.getElementById('post-edit-newform');

const url = window.location.href;

const getCookie = (name) =>
  {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

const likeUnlikePosts = ()=>
{
const likeUnlikeForms = [...document.getElementsByClassName("like-unlike-forms")]
likeUnlikeForms.forEach(form=>form.addEventListener("submit", e=>
{
           e.preventDefault();
           const clickedId = e.target.getAttribute('data-form-id');
           const clickedBtn = document.getElementById(`like-unlike-${clickedId}`);
//         const UnlikedBtn = document.getElementById(`unlike-like-${clickedId}`);
           const postLike = document.getElementById(`blog-like-${clickedId}`);
//         const postunLike = document.getElementById(`blog-unlike-${clickedId}`);

$.ajax(
{
type: 'POST',
url: "/like_post/",
data:
{
'csrfmiddlewaretoken': csrftoken,
'pk': clickedId,
},
success: function(response)
{
//  console.log(response.nooflike);
  if (response.nooflike > 0)
  {
              postLike.textContent = `${response.nooflike}`;
  }
  else
  {
    //   postLike.textContent = ``;
       alert(response.data);
  }

//  console.log(response.nooflike);
//  alert(response.data);
},
error: function(error)
{
         console.log(error);
},
})

})
)
}


const editPosts = ()=>
{
//const editForms = [...document.getElementsByClassName("edit-blog-forms")]
const editForms = [...document.getElementsByClassName("edit-blog-forms")]
const csrf = document.getElementsByName("csrfmiddlewaretoken");
editForms.forEach(form=>form.addEventListener("submit", e=>
{
           e.preventDefault();
           console.log(e);
           const clickedId = e.target.getAttribute('data-form-id');
//           const editBtn = document.getElementById(`blog-edit-${clickedId}`);
           const editblogForm = document.getElementById("blog-edit-form1");
           const body = document.getElementById("id_blog_body");
           console.log(csrf[0].value);
           console.log(body.value)
           const fd = new FormData()
           fd.append('csrfmiddlewaretoken', csrf[0].value)
           fd.append('body', body.value)
           console.log(fd)
           window.location.href = 'postData' + '/' + 'edit' + '/' + clickedId
           body.value = "hii";


}))
}

const postDetails = [...document.getElementsByClassName("card-body")];
console.log(postDetails)



//const editnewPosts = ()=>
//{
////const editForms = [...document.getElementsByClassName("edit-blog-forms")]
//const editForms = [...document.getElementsByClassName("edit-blog-forms")]
//const csrf = document.getElementsByName("csrfmiddlewaretoken");
//editForms.forEach(form=>form.addEventListener("submit", e=>
//{
//           e.preventDefault();
//           console.log(e);
//           const clickedId = e.target.getAttribute('data-form-id');
//           const editblogForm = document.getElementById("blog-edit-form1");
//           const body = document.getElementById("id_blog_body");
//           console.log(csrf[0].value);
//           console.log(body.value)
//           const fd = new FormData()
//           fd.append('csrfmiddlewaretoken', csrf[0].value)
//           fd.append('body', body.value)
//           const editNewForm = document.getElementById(`blog-editForm-${clickedId}`);
//
//$.ajax(
//{
//type: 'POST',
//url: `postData/edit/${clickedId}`,
//enctype: "multipart/form-data",
//data: fd,
//dataType: "json",
////xhr: function(){
////const xhr = new window.XMLHttpRequest();
////
////console.log(xhr)
////console.log(body);
////console.log(editblogForm);
////
////return xhr
////},
//success: function(response)
//{
////       var x = JSON.parse(response["instance"]);
////       const x = JSON.parse(response["instance"])
//       console.log(response.django_backend)
//       editNewForm.classList.remove("not-visible");
//
////       editNewForm.insertAdjacentElement("afterend", `${editblogForm}`);
//       console.log(editblogForm)
//
//       editNewForm.innerHTML += `<form action=" " method="post" id="my_form">
//      <label>Body</label>
//      <input type=${response.django_backend} name=${response.editblogForm} />
//      <input type="submit" name="submit" value="Submit Form" />
//      <input type="submit" name="cancel" value="Cancel Form" />
//      <div id="server-results">
//        <!-- For server results -->
//      </div>
//    </form>
//`
//
//},
//error: function(error)
//{
//         console.log(error);
//},
//cache: false,
//contentType: false,
//processData: false,
//
//})
//}))
//}


//const clickedId = 1;
//
//$.ajax(
//{
//type: 'POST',
//url: `postData/edit/${clickedId}`,
//enctype: "multipart/form-data",
//data:
//{
//'csrfmiddlewaretoken': csrf[0].value,
////'data1': $(this).serialize(),
//'pk': clickedId
//},
////xhr: function(){
////const xhr = new window.XMLHttpRequest();
////
////console.log(xhr)
////console.log(body);
////console.log(editblogForm);
////
////return xhr
////},
//success: function(response)
//{
//       console.log(response);
//       var x = JSON.parse(response["instance"]);
//       var fields = x[0];
//       console.log(fields['fields'].body);
//
//       editBox.innerHTML = `${fields['fields'].body}`
//
//},
//error: function(error)
//{
//         console.log(error);
//},
//})
//}))
//$.ajax(
//{
//type: 'POST',
//url: "/edit/",
//data:
//{
//'csrfmiddlewaretoken': csrftoken,
//'pk': clickedId,
//},
//success: function(response)
//{
//console.log(response.noofunlike);
//
//
//
////
//},
//error: function(error)
//{
//         console.log(error);
//},

console.log("loaded");
let visible = 3;

const getData = () =>{

$.ajax({
        type: "GET",
        url: `postData/${visible}`,
        success: function(response){
        setTimeout(()=>
               {
                spinnerBox.classList.add("not-visible");
                const post_data = response.data;
//                console.log(post_data);
                post_data.forEach(t1 =>{
                postsBox.innerHTML += `<div class="card mb-2">
                                                  <div class="card-body" class="text-center">
                                                    <h6 class="card-title">
                                                       <a href="${url}details/${t1.id}">
                                                       ${t1.title} </a>
                                                    </h6>
                                                        <p class="card-text">${t1.author}

                                                        <img src=${ t1.pic } width="30"
                                                        class="user-img rounded-circle mr-2"> </p>
                                                  </div>
                                                  <div class="card-footer">
                                                      <div class="row">
                                                        <div class="col-2">
                                                             <form class="edit-blog-forms" data-form-id=${t1.id}>
                                                                <button href="{% url 'edit_post' ${t1.id} %}"
                                                                  class="btn btn-primary btn-sm"
                                                                  id="blog-edit-${t1.id}">Edit</button>
                                                             </form>
                                                             <div id="blog-editForm-${t1.id}" class='not-visible'></div>
                                                        </div>
                                                        <div class="col-2">
                                                              <form class="like-unlike-forms" data-form-id=${t1.id}>
                                                                 <button href="{% url 'like_post'  %}"
                                                                    class="btn btn-primary btn-sm" id="like-unlike-${t1.id}">Likes
                                                                 </button>
                                                              </form>
                                                        <div id="blog-like-${t1.id}">${t1.no_of_like}</p>
                                                      </div>
                                                  </div>`

                });
                likeUnlikePosts();
                editPosts();
//                editnewPosts();

}, 2000)

console.log(response.size);
if (response.size ===0)
{
   endBox.textContent = 'no posts added yet..'

}
else if (response.size <= visible)
{
         loadBtn.classList.add('not-visible');
         endBox.textContent = 'no posts to show ..'

}

},
error: function(error)
        {
              console.log(error);

        },
async: true,
cache: true,
contentType:false,
processData: false
})
}
if (loadBtn != null)
{
loadBtn.addEventListener("click", ()=>{
                 spinnerBox.classList.add("not-visible");
                 visible += 3
                 getData();

})
}

setTimeout(()=>
{
console.log(document.location.toString());
console.log(url);
if (document.location.toString()==="http://127.0.0.1:8000/")
{
getData()
}
}, 5000)
