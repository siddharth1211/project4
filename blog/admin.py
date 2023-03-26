from django.contrib import admin
from .models import blog, blog_like, blog_unlike, Comment

admin.site.register(blog)
admin.site.register(blog_like)
admin.site.register(blog_unlike)
admin.site.register(Comment)


# Register your models here.
