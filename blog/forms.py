from django import forms
from django.contrib.auth.models import User
from .models import blog, Comment

class blogCreationForm(forms.ModelForm):
      class Meta:
          model = blog
          fields = ('title', 'body')
          widgets = { 'title': forms.TextInput(attrs={'class': 'form_control', 'id': 'id_title_body'}),
                      'body': forms.Textarea(attrs={'class': 'form_control', 'id': 'id_blog_body'})

                     }

      def __init__(self, *args, **kwargs):
          super(blogCreationForm, self).__init__(*args, **kwargs)
          for field in self.fields:
              self.fields[field].widget.attrs.update({
                  'class': 'form-control'})


class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_body',)
        widgets = {'comment_body': forms.TextInput(attrs={'class': 'form_control'})
                   }

    def __init__(self, *args, **kwargs):
        super(commentForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'})
#
# class replyForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('comment_body',)
#         widgets = {'comment_body': forms.TextInput(attrs=
#                                                    {'class': 'form_control'})
#                    }
    # def __init__(self, *args, **kwargs):
    #     super(replyForm, self).__init__(*args, **kwargs)
    #     for field in self.fields:
    #         self.fields[field].widget.attrs.update({
    #             'class': 'form_control'})


class replyForm(forms.Form):
      reply_body = forms.CharField(max_length=500)
