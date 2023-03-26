"""project2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views
from django.contrib.staticfiles.urls import static

urlpatterns = [
     path('', views.home, name='home'),
#     path('postData/', views.get_post_data, name='get_post_data'),
     path('like_post/', views.like_post, name='like_post'),
     path('unlike_post/', views.unlike_post, name='unlike_post'),
     path('details/<int:id>/', views.detail_post, name='detail_post'),
     path('details/<int:id>/<int:comment_id>/load-comments/', views.replies_post, name='replies_post'),
     path('details/<int:id>/<int:comment_id>/comments/', views.create_comment, name='create_comment'),
     path('details/<int:id>/<int:comment_id>/reply/', views.comment_reply, name='comment_reply'),
     path('postData/<int:num_posts>/', views.load_post_data, name='load_post_data'),
     path('postData/edit/<int:pk>', views.edit_post_data, name='edit_post_data'),
#     path('postData/edit/<int:pk>', views.edit_post, name='edit_post'),

]
#1/19/load-comments/
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

