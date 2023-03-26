from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch.dispatcher import receiver
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone


class blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=1800, default=None)
    body = models.TextField(blank=True)
    no_of_like = models.IntegerField(default=0, blank=True)
    no_of_unlike = models.IntegerField(default=0, blank=True)
    created_date = models.DateTimeField(auto_created=True, default=timezone.now)
    modified_date = models.DateTimeField(auto_created=True, default=None, null=True, blank=True)


class blog_like(models.Model):
    likes = models.ForeignKey(blog, on_delete=models.CASCADE)
    user_liked = models.ForeignKey(User, on_delete=models.CASCADE)

class blog_unlike(models.Model):
    unlikes = models.ForeignKey(blog, on_delete=models.CASCADE)
    user_unliked = models.ForeignKey(User, on_delete=models.CASCADE)

@receiver(pre_save, sender=blog_like)
def before_like_blog1(sender, instance, *args, **kwargs):
    try:
        print(blog_like.objects.get(likes=instance.likes, user_liked=instance.user_liked))

        blog_like.objects.get(likes=instance.likes, user_liked=instance.user_liked)
        raise Exception("you already liked the blog")
    except ObjectDoesNotExist:
        print("you can like the blog")

@receiver(post_save, sender=blog_like)
def after_like_blog1(sender, instance, created, **kwargs):
    print(kwargs)
    # if created:
    #     instance.likes.no_of_like = blog_like.objects.filter(likes=instance.likes.id).count()
    #     instance.likes.save()

    try:
        t1 = blog_unlike.objects.get(unlikes=instance.likes, user_unliked=instance.user_liked)
        t1.delete()
        instance.likes.no_of_unlike = blog_unlike.objects.filter(unlikes=instance.likes.id).count()
        instance.likes.no_of_like = blog_like.objects.filter(likes=instance.likes.id).count()
        instance.likes.save()
        # if instance.likes.no_of_unlike > 0:
        #    instance.likes.no_of_unlike -= 1
        #    instance.likes.no_of_like += 1
        #    instance.likes.save()

          #    t1 = blog_like.objects.create(likes=instance.likes, user_liked=instance.user_liked)
          #    t1.likes.no_of_like += 1
          #    t1.likes.save()
          #    t1.save()
          #
    except ObjectDoesNotExist:
        if created:
            instance.likes.no_of_like = blog_like.objects.filter(likes=instance.likes.id).count()
#            instance.save()
            instance.likes.save()


@receiver(pre_save, sender=blog_unlike)
def before_unlike_blog1(sender, instance, *args, **kwargs):
    try:
        print(blog_unlike.objects.get(unlikes=instance.unlikes, user_unliked=instance.user_unliked))

        blog_unlike.objects.get(unlikes=instance.unlikes, user_unliked=instance.user_unliked)
        raise Exception("you already unliked the blog")
    except ObjectDoesNotExist:
        print("you can like the blog")

@receiver(post_save, sender=blog_unlike)
def after_unlike_blog1(sender, instance, created, **kwargs):
    print(kwargs)
    try:
        t1 = blog_like.objects.get(likes=instance.unlikes, user_liked=instance.user_unliked)
        t1.delete()
        instance.unlikes.no_of_like = blog_like.objects.filter(likes=instance.unlikes.id).count()
        instance.unlikes.no_of_unlike = blog_unlike.objects.filter(unlikes=instance.unlikes.id).count()
#        instance.save()
        instance.unlikes.no_of_unlike
        instance.unlikes.save()
        # if instance.unlikes.no_of_like > 0:
        #    instance.unlikes.no_of_like -= 1
        #    instance.unlikes.no_of_unlike += 1
        #    instance.unlikes.save()

          #    t1 = blog_like.objects.create(likes=instance.likes, user_liked=instance.user_liked)
          #    t1.likes.no_of_like += 1
          #    t1.likes.save()
          #    t1.save()
          #
    except ObjectDoesNotExist:
        if created:
            instance.unlikes.no_of_unlike = blog_unlike.objects.filter(unlikes=instance.unlikes.id).count()
#            instance.save()
            instance.unlikes.save()

# @receiver(pre_save, sender=blog_unlike)
# def before_unlike_blog1(sender, instance, *args, **kwargs):
#     try:
#        x = blog_like.objects.get(likes=instance.unlikes, user_liked=instance.user_unliked)
#        x.likes.no_of_like -= 1
#        x.save()
#        x.delete()
#        # if blog_like.likes.no_of_like > 0:
#        #     blog_like.likes.no_of_like -= 1
#        #     blog_like.save()
#     except ObjectDoesNotExist as e:
#        try:
#            t1 = blog_unlike.objects.get(likes=instance.unlikes, user_liked=instance.user_unliked)
#            raise Exception("you already unliked the blog")
#        except ObjectDoesNotExist as e:
#            t1 = blog_unlike.objects.create(unlikes=instance.unlikes, user_liked=instance.user_unliked)
#            t1.likes.no_of_unlike += 1
#            t1.save()
#
# # @receiver(pre_save, sender=blog_like)
# # def before_like_blog2(sender, instance, *args, **kwargs):
# #     try:
# #        x = blog_like.objects.get(likes=instance.likes, user_liked=instance.user_liked)
# #        raise Exception("you already liked the blog")
# #        # if blog_like.likes.no_of_like > 0:
# #        #     blog_like.likes.no_of_like -= 1
# #        #     blog_like.save()
# #     except ObjectDoesNotExist as e:
# #        print("you can like the blog")
# #
# # @receiver(pre_save, sender=blog_unlike)
# # def before_unlike_blog2(sender, instance, *args, **kwargs):
# #     try:
# #        x = blog_unlike.objects.get(unlikes=instance.unlikes, user_unliked=instance.user_unliked)
# #        raise Exception("you already unliked the blog")
# #     except ObjectDoesNotExist as e:
# #        print("you can unlike the blog")
#
#
# Create your models here.


class Comment(models.Model):
    commented_post = models.ForeignKey(blog, related_name="comments", on_delete=models.CASCADE)
    commented_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_body = models.TextField()
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def children(self):
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True