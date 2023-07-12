from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from account_app.models import HelloWorld

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