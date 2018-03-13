from django.forms import ModelForm
from django import forms
from .models import UserContent

class UserContentForm(ModelForm):
    class Meta:
        model = UserContent
        fields = ['content',]
        widgets = {
            'content' : forms.Textarea(attrs={
                'class' : 'form-control text-muted',
            })
        }
