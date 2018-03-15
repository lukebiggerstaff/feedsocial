from django.forms import ModelForm
from django import forms
from .models import UserContent, ContentComment

class UserContentForm(ModelForm):
    class Meta:
        model = UserContent
        fields = ['content',]
        widgets = {
            'content' : forms.Textarea(attrs={
                'class' : 'form-control text-muted',
                'placeholder' : 'Add your message here',
                'autocomplete' : 'off',
            })
        }


class CommentForm(ModelForm):
    class Meta:
        model = ContentComment
        fields = ['message']
        widgets = {
            'message' : forms.TextInput(attrs={
                'class' : 'form-control text-muted',
                'placeholder' : 'what do you want to say?',
                'autocomplete' : 'off',
            }),
        }
