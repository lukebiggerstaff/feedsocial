from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.datastructures import MultiValueDictKeyError
from accounts.models import FeedSocialUser
from .models import UserContent, ContentComment
from .forms import UserContentForm, CommentForm

class FeedView(ListView):
    template_name = 'feed.html'
    model = UserContent

    def get_queryset(self):
        try:
            query = self.request.GET['query']
        except MultiValueDictKeyError:
            qs = UserContent.objects.all()
            return qs[:101]
        else:
            if query:
                qs1 = UserContent.objects.filter(content__icontains=query)
                qs2 = UserContent.objects.filter(creator__username__icontains=query)
                return (qs1 | qs2)[:101]
            qs = UserContent.objects.all()
            return qs[:101]

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


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = ContentComment
    form_class = CommentForm
    template_name = 'commentcreate.html'
    success_url = reverse_lazy('feed')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        obj = get_object_or_404(UserContent, pk=pk)
        context['object'] = obj
        return context

    def form_valid(self, form):
        content_parent = get_object_or_404(UserContent, pk=self.kwargs['pk'])
        form.instance.comment_creator = self.request.user
        form.instance.content_parent = content_parent
        return super().form_valid(form)
