# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Article
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title', 'summary', 'body', 'photo')
    template_name = 'article_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Article
    template_name = 'article_create.html'
    fields = ('title', 'summary', 'body', 'photo')

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        # Avtomatik ravishda hozirgi foydalanuvchini author sifatida qo'shish
        form.instance.author = self.request.user
        return super().form_valid(form)