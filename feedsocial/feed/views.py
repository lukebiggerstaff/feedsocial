from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import UserContent
from .forms import UserContentForm

class FeedView(CreateView):
    template_name = 'feed/home.html'
    form_class = UserContentForm
    success_url = reverse_lazy('feed')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        qs = UserContent.objects.all()
        kwargs['object_list'] = qs
        return super().get_context_data(**kwargs)
