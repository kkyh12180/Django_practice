from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from account_app.forms import AccountUpdateForm
from account_app.models import HelloWorld
from django.views.generic import CreateView, DetailView, UpdateView

# Create your views here.

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

class AccountDetailView(DetailView) :
    model = User
    context_object_name = 'target_user'
    template_name = 'account_app/detail.html'

class AccountUpdateView(UpdateView) :
    model = User
    form_class = AccountUpdateForm
    success_url = reverse_lazy('account_app:hello_world')
    template_name = 'account_app/update.html'