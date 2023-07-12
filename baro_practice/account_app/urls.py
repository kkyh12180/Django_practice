from django.contrib import admin
from django.urls import path, include
from account_app.views import hello_world

# app_name 명시
# 추후 accountapp:hello_world 로 접근이 가능해지기 때문
app_name = 'account_app'

urlpatterns = [
    # views.py의 hello_world 불러옴
    path('hello_world/', hello_world, name='hello_world'),
]
