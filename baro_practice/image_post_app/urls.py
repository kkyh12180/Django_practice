from django.contrib import admin
from django.urls import path, include
from image_post_app.views import show_image_posts, show_image_content

# app_name 명시
# 추후 accountapp:hello_world 로 접근이 가능해지기 때문
app_name = 'image_post_app'

urlpatterns = [
    path('', show_image_posts, name='image_post_list'),
    path('image/<str:IPID>', show_image_content, name='image_post_content'),
]
