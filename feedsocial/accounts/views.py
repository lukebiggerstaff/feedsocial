from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import FeedSocialUserCreationForm


class SignupView(FormView):
    form_class = FeedSocialUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('feed')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
