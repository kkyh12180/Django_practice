from django.contrib import admin
from django.urls import path, include

from profile_app.views import ProfileCreateView, ProfileUpdateView

# app_name 명시
# 추후 accountapp:hello_world 로 접근이 가능해지기 때문
app_name = 'profile_app'

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create'),
    path('update/<int:pk>', ProfileUpdateView.as_view(), name='update')
]
