from typing import Any, Dict
from django.views.generic import CreateView , DetailView, ListView
from django.urls import reverse, reverse_lazy
from project_app.forms import ProjectCreationForm
from project_app.models import Project
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.list import MultipleObjectMixin
from article_app.models import Article
from subscribe_app.models import Subscription

# Create your views here.
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView) :
    model = Project
    form_class = ProjectCreationForm
    template_name = 'project_app/create.html'
    
    def get_success_url(self) :
        return reverse('project_app:detail', kwargs={'pk': self.object.pk}) 
    
class ProjectDetailView(DetailView, MultipleObjectMixin) :
    model = Project
    context_object_name = 'target_project'
    template_name = 'project_app/detail.html'
    paginate_by = 25

    def get_context_data(self, **kwargs: Any) :
        project = self.object
        user = self.request.user

        if user.is_authenticated :
            subscription = Subscription.objects.filter(user=user, project=project)

        object_list = Article.objects.filter(project=self.get_object())
        return super(ProjectDetailView, self).get_context_data(object_list=object_list, subscription=subscription , **kwargs)

class ProjectListView(ListView) :
    model = Project
    context_object_name = 'project_list'
    template_name = 'project_app/list.html' 
    paginate_by = 25