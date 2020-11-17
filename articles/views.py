from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Comment

class ArticleListView(ListView):
    model = models.Article
    template_name = 'article_list.html'

class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = models.Article
    template_name = 'article_detail.html'

class ArticleUpdateView(LoginRequiredMixin,UpdateView): 
    model = models.Article
    fields = ['title', 'body', ]
    template_name = 'article_edit.html'

class ArticleDeleteView(LoginRequiredMixin,DeleteView): 
    model = models.Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = models.Article
    template_name = 'article_new.html'
    fields = ['title', 'body', 'author',]
    login_url = 'login'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

