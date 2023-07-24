from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import CreateView, DeleteView
from article_app.models import Article
from comment_app.models import Comment
from comment_app.forms import CommentCreationForm
from django.urls import reverse
from django.utils.decorators import method_decorator
from comment_app.decorators import comment_ownership_required

class CommentCreateView(CreateView) :
    model = Comment
    form_class = CommentCreationForm
    template_name = 'comment_app/create.html'

    def form_valid(self, form) :
        temp_comment = form.save(commit=False)
        temp_comment.article = Article.objects.get(pk=self.request.POST['article_pk'])
        temp_comment.writer = self.request.user
        temp_comment.save()

        return super().form_valid(form)

    def get_success_url(self) :
        return reverse('article_app:detail', kwargs={'pk': self.object.article.pk})

@method_decorator(comment_ownership_required, 'get')
@method_decorator(comment_ownership_required, 'post')    
class CommentDeleteView(DeleteView) :
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'comment_app/delete.html'

    def get_success_url(self):
        return reverse('article_app:detail', kwargs={'pk': self.object.article.pk})