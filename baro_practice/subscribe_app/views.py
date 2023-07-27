from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView
from django.urls import reverse, reverse_lazy
from project_app.models import Project
from article_app.models import Article
from subscribe_app.models import Subscription

# Create your views here.

@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView) :
    def get_redirect_url(self, *args, **kwargs) :
        return reverse('project_app:detail', kwargs={'pk': self.request.GET.get('project_pk')})
    
    def get(self, request, *args, **kwargs) :
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user
        subscription = Subscription.objects.filter(user=user, project=project)

        if subscription.exists() :
            subscription.delete()
        else :
            Subscription(user=user, project=project).save()
        return super(SubscriptionView, self).get(request, *args, **kwargs)

@method_decorator(login_required, 'get')
class SubscriptionListView(ListView) :
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribe_app/list.html'
    paginate_by = 5

    def get_queryset(self) :
        projects = Subscription.objects.filter(user=self.request.user).values_list('project')
        article_list = Article.objects.filter(project__in=projects)
        return article_list