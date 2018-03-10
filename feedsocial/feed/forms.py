from django.forms import ModelForm
from .models import UserContent

class UserContentForm(ModelForm):
    class Meta:
        model = UserContent
        fields = ['content',]
