from django.urls import path, include
from django.views.generic import TemplateView

from comment_app.views import CommentCreateView, CommentDeleteView

# app_name 명시
app_name = 'comment_app'

urlpatterns = [
    path('create/', CommentCreateView.as_view(), name='create'),
    path('delete/<int:pk>', CommentDeleteView.as_view(), name='delete'),
]
