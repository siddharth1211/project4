from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

class NewuserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1')
        widgets = {'username': forms.TextInput(attrs={'class': 'form_control', 'id':'id_username'}),
                   'email': forms.EmailInput(attrs={'class': 'form_control', 'id': 'id_email'}),
                   'password': forms.PasswordInput(attrs={'class': 'form_control', 'id': 'id_password'})
                   }
    def save(self, commit=True):
        user = super(NewuserForm, self).save(commit=False)
        if commit is True:
            user = user.save()
        return user
    def __init__(self, *args, **kwargs):
        super(NewuserForm, self).__init__(*args, **kwargs)
        self.fields["password1"].help_text = None
        self.fields["username"].help_text = None

#        del self.fields["password2"]

class ProfileUserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'dob', 'img' )
        widgets = {'bio': forms.TextInput(attrs={'class': 'form_control', 'id': 'id_bio'}),
                   'dob': forms.DateInput(attrs={'class': 'form_control', 'id': 'id_dob'}),
                   'img': forms.FileInput(attrs={'class': 'form_control', 'id': 'id_user_image',
                                                 'style': 'length 100px ; width 100px'})
                   }