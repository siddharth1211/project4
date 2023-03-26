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
from django.contrib.staticfiles.urls import static
from . import views

app_name = "userprofile"


urlpatterns = [
            path('<int:user_id>/settings', views.settings, name='settings'),
            path('<int:user_id>/logout/', views.user_logout, name='user_logout'),
            path('login/', views.user_login, name='user_login'),
            path('register/', views.register_user, name='register_user')

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)