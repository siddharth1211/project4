console.log("hello world....");
const spinnerBox1 = document.getElementById("spinner-box-new");
//const replyBtn = document.getElementsByClassName("ml-1");

setTimeout(()=>
{
spinnerBox1.classList.add("not-visible");
replyPosts();
}, 500)


const closeBtn = document.getElementById("close-btn");
const updateBtn = document.getElementById("update-btn");

const details = document.getElementsByClassName("post-new-details")
//console.log(details.id);
//let detailsId = details.getAttribute("target");
//console.log(detailsId);
const url_details = window.location.href;

//const csrftoken = getCookie('csrftoken');


closeBtn.addEventListener("click", ()=>
{

//  let newDetails = document.getElementById("{{ id }}")
//  let detailsId = newDetails.getAttribute("id");
//  console.log(detailsId);
  console.log(details[0].getAttribute("data-div-id"));
  console.log(url_details);
  history.back();

}

)

updateBtn.addEventListener("click", ()=>
{
  console.log(details[0].getAttribute("data-div-id"));
  console.log(url_details);
  const clickID = details[0].getAttribute("data-div-id");
//  window.location.replace(..)
//  var url_new = "{% url 'edit_post' %}";

  document.location.replace("../../" + "postData/" +"edit/" + clickID);

}
)

function newFunction()
{

let logoutBox = document.getElementById("logout-confirm-btn");
console.log(logoutBox)

//console.log(logoutBox);
logoutBox.classList.remove("not-visible");
logoutBox.innerHTML += `
<div class="modal-body">
  <h5>Popover in a modal</h5>
  <p>This <a href="#" role="button" class="btn btn-secondary popover-test" title="Popover title" data-bs-content="Popover body content is set in this attribute.">button</a> triggers a popover on click.</p>
  <hr>
  <h5>Tooltips in a modal</h5>
  <p><a href="#" class="tooltip-test" title="Tooltip">This link</a> and <a href="#" class="tooltip-test" title="Tooltip">that link</a> have tooltips on hover.</p>
</div>
`
}

const replyPosts = ()=>
{
const replyPost = [...document.getElementsByClassName("ml-1")]
replyPost.forEach(reply=>reply.addEventListener("click", e=>
{
           e.preventDefault();
           console.log(e);
           const x = e.target.nextElementSibling
           console.log(x.outerHTML);
           const csrf = document.getElementsByName("csrfmiddlewaretoken");
           console.log(csrf);
           const tickID = e.target.getAttribute('data-id');
           const newtickID = e.target.getAttribute('button');
           console.log(tickID);
           const form_1 = document.getElementById(`replyForm-${tickID}`);
           console.log(form_1);
           var formText = document.getElementById(`id_reply_body-${tickID}`);
           const fd = new FormData()
           console.log(fd);
           form_1.classList.remove("not-visible");
           form_1.addEventListener("submit", (e)=>{
           console.log("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
           e.preventDefault();

          $.ajax(
{
type: 'POST',
url: `${tickID}/comments/`,
enctype: "multipart/form-data",
dataType: 'json',
data: fd,
beforeSend: function(){
     form_1.classList.remove("not-visible");
     fd.append('csrfmiddlewaretoken', csrftoken);
     fd.append('comment_body', formText.value);
     fd.append('comment_id', `${tickID}`);

},
success: function(response)
       {
//         const y = JSON.stringfy(response);
//         console.log(y);
         const s1 = JSON.parse(JSON.stringify(response.data[0]))
         console.log(s1);
         console.log(`${tickID}`);

//         fd.append('csrfmiddlewaretoken', csrftoken);
////           fd.append('comment_id', `${tickID}`);
//         fd.append('comment_body', formText.value);
//         fd.append('comment_id', `${tickID}`);
//         console.log(formText);
////           fd.append('reply_body', formText.value);
         const reply_new1_comment = document.getElementById(`load-reply-${tickID}`);
         reply_new1_comment.classList.remove("not-visible");
         console.log(reply_new1_comment);
         reply_new1_comment.innerHTML += `<div class="card">
                                            <div class="card-body">
                                               <h7>  ${s1.comment_body} </h7>
                                               <br>
                                                  ${s1.commented_user} <img src=${ s1.pic }
                                                        width="30" class="user-img rounded-circle mr-2">
                                            </div>

                                            <div class="card-footer">
                                                      <div class="row">
                                                        <div class="col-2">
                                      <div class="reply-n2-forms">
                                      <button type="button" class="btn btn-primary btn-sm" data-newform-id="comment-reply-${s1.id}"
                                      onclick="replytoReply(${s1.id})">reply</button>
                                      <div id="comment-replyForm-${s1.id}" class='not-visible'></div>
                                      </div>
                                </div>
                                                     </div>
                                                   </div>
                                          </div>`

                                form_1.classList.add("not-visible");
},
error: function(error){

      console.log(error);
},
async: true,
cache: false,
contentType:false,
processData: false
})
})
/*
*/
}))
}

const loadComments = ()=>
{
console.log("Hanhuman JI");

const loadComment = [...document.getElementsByClassName("ml-3")]
console.log("Hanhuman JI");

loadComment.forEach(reply=>reply.addEventListener("click", e=>
{

console.log("Hanhuman JI");

           e.preventDefault();
           console.log(e);
           const t1 = e.target.nextElementSibling
           console.log(t1.outerHTML);
           const replyID = e.target.getAttribute('data-id');
           console.log(replyID)
           const reply_per_comment = document.getElementById(`load-reply-${ replyID }`);
           if (replyID != null)
             {
//           e.preventDefault();

$.ajax({
type: 'GET',
url: `${ replyID }/load-comments/`,
dataType: 'json',
success: function(response){
        const y2 = JSON.parse(JSON.stringify(response.data))
        console.log(y2);
        e.preventDefault();
        reply_per_comment.classList.remove("not-visible");
        reply_per_comment.innerHTML = ''
        y2.forEach(y1 =>{
        reply_per_comment.innerHTML += `<div class="card">
                                            <div class="card-body">
                                               <h7>  ${y1.comment_body} </h7>
                                               <br>
                                                  ${y1.commented_user} <img src=${ y1.pic }
                                                        width="30" class="user-img rounded-circle mr-2">
                                            </div>

                                            <div class="card-footer">
                                                      <div class="row">
                                                        <div class="col-2">
                                      <div class="reply-n2-forms">
                                      <button type="submit" class="btn btn-primary btn-sm" data-newform-id="comment-reply-${y1.id}"
                                      onclick="replytoReply(${y1.id})">reply</button>
                                      <div id="comment-replyForm-${y1.id}" class='not-visible'></div>
                                      </div>
                                </div>
                                                     </div>
                                                   </div>
                                          </div>`


                                          })

},
error: function(error){
       console.log(error);

},
async: true,
cache: false,
contentType:false,
processData: false

})
}
}))
}

loadComments();

const replytoReply = (t)=>
{
console.log("987766666666666666666644444444")
console.log(t);
const t1 = document.getElementById(`comment-replyForm-${t}`);
console.log(t1)
$.ajax({
type: 'GET',
url: "",
beforeSend: function(){
         console.log("ppppp")
         t1.classList.remove("not-visible");
         const fd = new FormData()
         fd.append('csrfmiddlewaretoken', csrftoken);

},
xhr: function(){
            t1.insertAdjacentHTML('afterbegin',`<form id="ReplyForm-${t}" onsubmit="replyTonew(${t})" action="" method="post" enctype="multipart/form-data">
            <input type="text" id="reply-${t}" name="reply" onchange="replyTonew(${t})">
            <button type="button" class="btn btn-primary btn-sm">reply</button>
             </form>`)

},
success: function(response){
             console.log(response);
             loadComments();

},
error: function(error){
      console.log(error)

},
async: true,
cache: false,
contentType:false,
processData: false
})
}



const replyTonew = (f)=>
{
console.log("90988888888888888888888")
console.log(f);
const f1 = document.getElementById(`reply-${f}`);
const f2 = document.getElementById(`ReplyForm-${f}`);
const fd = new FormData()
fd.append('csrfmiddlewaretoken', csrftoken);
fd.append('reply', f1.value);
console.log(fd);
$.ajax({
                    type: 'POST',
                    url: `${f}/reply/`,
                    enctype: "multipart/form-data",
                    data: fd,
                    dataType: 'json',
                    beforeSend: function(){
                              loadComments();

                    },
                    success: function(response)
                               {
                                  console.log(response.data);
                                  const m1 = JSON.parse(JSON.stringify(response.data));
                                  console.log(m1['id']);
                                  console.log(m1['comment_body']);

//                                   f2.addEventListener("click", (e)=>{

                                   console.log("ooo8863eedddddgg")
                                   const reply_new_comment = document.getElementById(`load-reply-${ m1.parent_id }`);
                                   reply_new_comment.classList.remove("not-visible");
                                   console.log(reply_new_comment);
                                   f2.classList.add("not-visible");

                                   reply_new_comment.innerHTML += `<div class="card">
                                            <div class="card-body">
                                               <h7>  ${m1.comment_body} </h7>
                                               <br>
                                                  ${m1.commented_user} <img src=${ m1.pic }
                                                        width="30" class="user-img rounded-circle mr-2">
                                            </div>

                                            <div class="card-footer">
                                                      <div class="row">
                                                        <div class="col-2">
                                      <div class="reply-n2-forms">
                                      <button type="button" class="btn btn-primary btn-sm" data-newform-id="comment-reply-${m1.id}"
                                      onclick="replytoReply(${m1.id})">reply</button>
                                      <div id="comment-replyForm-${m1.id}" class='not-visible'></div>
                                      </div>
                                </div>
                                                     </div>
                                                   </div>
                                          </div>`
                               console.log(response.message);


  //                                 })
},
error: function(error){
                             console.log(error);
                    },
                    async: true,
                    cache: true,
                    contentType:false,
                    processData: false
                    })

}