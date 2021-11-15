from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.core.paginator import Paginator  
from .models import *
from .filters import PostFilter
from .forms import PostForm
from datetime import datetime

from django.views import View


class NewsList(ListView):
    model = Post
    template_name = 'list.html'
    context_object_name = 'news'
    ordering = ['-dateCreation']
    paginate_by = 10
    form_class = PostForm

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            'filter': self.get_filter(),
            'form': self.form_class,
            'all_post': Post.objects.all(),
            'time_now': datetime.utcnow(),
        }

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return super().get(request, *args, **kwargs)


class NewsDetailView(DetailView):
    template_name = 'detail.html'
    queryset = Post.objects.all()
    context_object_name = 'new'


class NewsCreateView(CreateView):
    template_name = 'create.html'
    form_class = PostForm
    context_object_name = 'new'


class NewsSearchView(NewsList):
    template_name = 'search.html'


class NewsUpdateView(UpdateView):
    template_name = 'update.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class NewsDeleteView(DeleteView):
    template_name = 'delete.html'
    queryset = Post.objects.all()
    context_object_name = 'new'
    success_url = '/news/'