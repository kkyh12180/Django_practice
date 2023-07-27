from typing import Any, Dict
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from account_app.decorators import account_ownership_required
from account_app.forms import AccountUpdateForm
from account_app.models import HelloWorld
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin
from article_app.models import Article

# Create your views here.

has_ownership = [account_ownership_required, login_required]

@login_required
def hello_world(request) :
    if request.method == 'POST' :
        # post 에서 데이터를 가져옴
        temp = request.POST.get('hello_world_input')   
            
        # model DB 내부에 저장
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        hello_world_list = HelloWorld.objects.all()

        return HttpResponseRedirect(reverse('account_app:hello_world'))
    else :
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'account_app/hello_world.html', context={'hello_world_list': hello_world_list})
    
class AccountCreateView(CreateView) :
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('account_app:hello_world')
    template_name = 'account_app/create.html'

class AccountDetailView(DetailView, MultipleObjectMixin) :
    model = User
    context_object_name = 'target_user'
    template_name = 'account_app/detail.html'

    paginate_by = 25
    def get_context_data(self, **kwargs: Any) :
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView) :
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('account_app:hello_world')
    template_name = 'account_app/update.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView) :
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('account_app:hello_world')
    template_name = 'account_app/delete.html'
