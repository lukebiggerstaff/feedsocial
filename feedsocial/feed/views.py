from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils.datastructures import MultiValueDictKeyError
from accounts.models import FeedSocialUser
from .models import UserContent
from .forms import UserContentForm

class FeedView(ListView):
    template_name = 'feed.html'
    model = UserContent

    def get_queryset(self):
        try:
            query = self.request.GET['query']
        except MultiValueDictKeyError:
            qs = UserContent.objects.all()
            return qs
        else:
            if query:
                qs = UserContent.objects.filter(content__icontains=query)
                return qs
            qs = UserContent.objects.all()
            return qs

class PFeedView(ListView):
    template_name = 'feed.html'

    def get_queryset(self):
        user = get_object_or_404(FeedSocialUser, username=self.kwargs['user'])
        qs = UserContent.objects.filter(creator=user)
        return qs

class ContentCreateView(CreateView):
    model = UserContent
    template_name = 'create.html'
    form_class = UserContentForm
    success_url = reverse_lazy('feed')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
