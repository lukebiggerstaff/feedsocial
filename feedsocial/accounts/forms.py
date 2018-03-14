from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import FeedSocialUser

class FeedSocialUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        # hack per https://stackoverflow.com/questions/21572701/customize-the-way-usercreationform-looks-in-django
        # setting widgets in class Meta was not working for password fields
        # override init method to set class
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control text-muted'
        self.fields['password2'].widget.attrs['class'] = 'form-control text-muted'

    class Meta(UserCreationForm.Meta):
        model = FeedSocialUser
        fields = UserCreationForm.Meta.fields + ('email', )
        widgets = {
            'username'  : forms.TextInput(attrs={
                'class' : 'form-control text-muted',
            }),
            'email'     : forms.EmailInput(attrs={
                'class' : 'form-control text-muted',
            }),
        }

class FeedSocialAuthForm(AuthenticationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={
        'class' : 'form-control text-muted',
    }))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        'class' : 'form-control text-muted',
    }))
