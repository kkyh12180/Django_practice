from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from comment_app.forms import CommentCreationForm
from article_app.decorators import article_ownership_required
from article_app.models import Article
from article_app.forms import ArticleCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import FormMixin

# Create your views here.

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView) :
    model = Article
    form_class = ArticleCreationForm
    template_name = 'article_app/create.html'

    def form_valid(self, form) :
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self) :
        return reverse('article_app:detail', kwargs={'pk': self.object.pk})
    
class ArticleDetailView(DetailView, FormMixin) :
    model = Article
    form_class = CommentCreationForm
    context_object_name = 'target_article'
    template_name = 'article_app/detail.html'

@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleUpdateView(UpdateView) :
    model = Article
    form_class = ArticleCreationForm
    context_object_name = 'target_article'
    template_name = 'article_app/update.html'

    def get_success_url(self) :
        return reverse('article_app:detail', kwargs={'pk': self.object.pk})
    
@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleDeleteView(DeleteView) :
    model = Article
    context_object_name = 'target_article'
    template_name = 'article_app/delete.html'

    def get_success_url(self) :
        return reverse_lazy('article_app:list')
    
class ArticleListView(ListView) :
    model = Article
    context_object_name = 'article_list'
    template_name = 'article_app/list.html'
    paginate_by = 5