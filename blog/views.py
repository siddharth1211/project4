from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from userprofile.views import settings
from django.contrib.auth.views import auth_login
from django.contrib import messages
from django.contrib.auth.models import User
from .models import blog, blog_like, blog_unlike, Comment
from .forms import blogCreationForm, commentForm, replyForm
from django.core import serializers
import json
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


def home(request):
#    x = blog.objects.all()

    form = blogCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            x = form.save(commit=False)
            x.author = request.user
            x.save()
        else:
            print("form not valid!!")
    else:
        print("not POST")
        form = blogCreationForm()
    return render(request, 'blog/home.html', {'form': form})

def load_post_data(request, num_posts):
    visible = 3
    upper = num_posts
    lower = upper - visible
    size = blog.objects.all().count()
    x = blog.objects.all()
    data = []

    for item in x:
        d1 = {
                'id':  item.id,
                'title': item.title,
                'body': item.body,
                'author': item.author.username,
                'no_of_like': item.no_of_like,
                'no_of_unlike': item.no_of_unlike,
                'created_date': item.created_date,
                'modified_date': item.modified_date,
                'pic': item.author.profile.img.url
        }
        data.append(d1)
        print(data)
    return JsonResponse({'data': data[lower: upper], 'size': size})

def edit_post_data(request, pk):
    obj = get_object_or_404(blog, id=pk)
    print(obj)
    editform = blogCreationForm(request.POST, request.GET or None, instance=obj)
    if  request.method=='POST':
        editform = blogCreationForm(request.POST, instance=obj)
        if editform.is_valid():
           instance = editform.save(commit=False)
           instance.author = obj.author
           print(obj.body)
#            instance.body = form.cleaned_data.get("body")
           instance.save()
           ser_instance = serializers.serialize('json', [instance, ])
            # send to client side.
           return redirect("home")
        else:
            print("errors")
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)
    else:
        print("not post!")
        print(obj.body)
    editform = blogCreationForm(instance=obj)
    return render(request, 'blog/edit.html', {'editform': editform})

#    return JsonResponse({"error": ""}, status=400)



def like_post(request):
    try:
      if request.is_ajax():
        pk = request.POST.get("pk")
        obj = blog.objects.get(pk=pk)
        x = blog_like.objects.create(likes=obj, user_liked=request.user)

        messages.success(request, 'user liked this post!!')
        return JsonResponse({'data': 'you liked this post!!', 'nooflike': obj.no_of_like, 'noofunlike': obj.no_of_unlike})
    except Exception:
        return JsonResponse({'data': 'you alreday liked this post!!'})

def unlike_post(request):
    try:
      if request.is_ajax():
        pk = request.POST.get("pk")
        obj = blog.objects.get(pk=pk)
        x = blog_unlike.objects.create(unlikes=obj, user_unliked=request.user)

        messages.success(request, 'user unliked this post!!')
        return JsonResponse({'data': 'you liked this post!!', 'noofunlike': obj.no_of_unlike, 'nooflike': obj.no_of_like})
    except Exception:
        return JsonResponse({'data': 'you alreday unliked this post!!'})

# Create your views here.

def edit_post(request, pk):
    obj = get_object_or_404(blog, id=pk)
    print(obj)
    if request.is_ajax():
        print(obj)
        editform = blogCreationForm(request.POST, request.GET or None, instance=obj)
        if editform.is_valid():
            instance = editform.save(commit=False)
            instance.author = obj.author
            instance.body = obj.body
            print(editform.cleaned_data.get("body"))
#            instance.save()
            ser_instance = serializers.serialize('json', [instance, ])
            # send to client side.
            return JsonResponse({"instance": "saved successfully",
#                                 "form" : serializers.serialize('json', [editform]),
                                 "django_backend": ser_instance}, status=200)
        else:
            return JsonResponse({"error": "error occurred"}, status=400)

    else:
        print("not post!")
    editform = blogCreationForm(instance=obj)
    return render(request, 'blog/edit.html', {'editform': editform})

def detail_post(request, id):
    obj = get_object_or_404(blog, id=id)
    form = commentForm(request.POST, request.GET or None)

    if form.is_valid():
        form = form.save(commit=False)
        form.commented_user = request.user
        form.commented_post = obj
        form.save()
        return redirect('detail_post', id=id)
    else:
        print(form.errors)

    return render(request, 'blog/details.html', {'x': obj, 'comment_Form': form})


def create_comment(request, id, comment_id):
    obj = get_object_or_404(blog, id=id)
    comment = get_object_or_404(Comment, id=comment_id)
    d2 = {}
    t1 = []
    if request.is_ajax():
        print(request.POST.get("comment_id"))
        print(request.POST)
        d1 = {x: request.POST.get(x) for x in request.POST.keys()}
        d1['comment_id'] = int(d1['comment_id'])
        print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiuuuuuuuuuuuuu")
        #            form = form.save(commit=False)
        #            form.commented_post = obj
        x = Comment(commented_user=request.user, comment_body=str(d1['comment_body']),
                    parent=Comment.objects.get(id=d1['comment_id']), commented_post=obj)
        x.save()
        d2['id'] = x.id
        d2['commented_user'] = request.user.username
        d2['comment_body'] = str(d1['comment_body'])
        d2['parent'] = d1['comment_id']
        d2['commented_post'] = obj.id
        d2['pic'] = request.user.profile.img.url
        print(d2)
        t1.append(d2)
        print(t1)
    return JsonResponse({'message': 'comment submitted !!', 'data': t1})

# def reply_post(request, id):
#     print("callll me!!")
#     obj = get_object_or_404(blog, id=id)
# #    comment = get_object_or_404(Comment, id=comment_id)
#     form1 = replyForm(request.POST, request.GET or None, instance=obj)
#     if request.method == 'POST':
#         if form1.is_valid():
#             reply_body = form1.cleaned_data.get('reply_body')
#             form1 = form1.save(commit=False)
#             form1.post = obj
#             form1.reply_user = request.user
#             form1.parent = x.id
#             form1.save()
# #            obj = get_object_or_404(blog, id=id)
# #            comment = get_object_or_404(Comment, id=comment_id)
#             print(obj, comment)
#             print("------------------------------------******")
#             t1 = request.POST.get("reply_body")
#             t2 = request.POST.get("comment.id")
#             x.save()
#             form1.save()
# #            x.chidren()
#             return JsonResponse({'reply_body': t1, 'reply_Form': form1})
#         else:
#             print("form not valid!!")
#             print(form1.errors)
#             print(request.GET.get('comment.id'))
#     else:
#
#         form1 = replyForm()
#         form1.post = obj
#         form1.reply_user = request.user
#         form1 = form1.save(commit=False)
#         form1.parent = form1.id
#         form1.save()
#         print(request.POST.get("reply_body"))
#     return render(request, 'blog/details.html', {'x': obj, 'reply_Form': form1})


def replies_post(request, id, comment_id):
    post = get_object_or_404(blog, id=id)
    comment = get_object_or_404(Comment, id=comment_id)
    reply_post = Comment.objects.filter(commented_post=post, parent=comment).values()
    l1 = []
    d1 = {}
    t1 = []
    for obj in reply_post:
#        obj['commented_post'] = blog.objects.get(id=obj['commented_post_id']).id
        obj['commented_user'] = User.objects.get(id=obj['commented_user_id']).username
        obj['pic'] = User.objects.get(id=obj['commented_user_id']).profile.img.url
        # d1['comment_body'] = obj['comment_body']
        # d1['parent'] = obj['parent_id']
        # d1['date_added'] = obj['date_added']
        print("----------------")
        l1.append(obj)
    return JsonResponse({'data': l1})

#@csrf_exempt
def comment_reply(request, id, comment_id):
    y = get_object_or_404(blog, id=id)
    comment = get_object_or_404(Comment, id=comment_id)
    comment_id = get_object_or_404(Comment, id=comment_id).parent_id
    l1 = []
    d1 = {}
    t1 = []
    if request.is_ajax():
        print(request.POST)
        d1 = {x: request.POST.get(x) for x in request.POST.keys()}
        print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiuuuuuuuuuuuuu")
        #            form = form.save(commit=False)
        #            form.commented_post = obj
        x = Comment(commented_user=request.user, comment_body=str(d1['reply']),
                    parent=Comment.objects.get(id=comment_id), commented_post=y)
        x.save()
    reply_post = Comment.objects.filter(commented_post=y, parent=Comment.objects.get(id=comment_id)).values()
    print(reply_post)
    for obj in reply_post:
        obj['commented_user'] = User.objects.get(id=obj['commented_user_id']).username
        obj['pic'] = User.objects.get(id=obj['commented_user_id']).profile.img.url
        print(obj)
    t1.append(obj)
    print(t1)
    return JsonResponse({'message': 'comment submitted !!', 'data': t1[-1]})