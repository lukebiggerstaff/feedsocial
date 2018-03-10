from django.contrib.auth.forms import UserCreationForm
from .models import FeedSocialUser

class FeedSocialUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = FeedSocialUser
        fields = UserCreationForm.Meta.fields + ('email', )
