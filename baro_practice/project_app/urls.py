from django.urls import path, include
from project_app.views import ProjectListView, ProjectCreateView, ProjectDetailView

# app_name 명시
app_name = 'project_app'

urlpatterns = [
    path('list/', ProjectListView.as_view(), name='list'),
    path('create/', ProjectCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ProjectDetailView.as_view(), name='detail'),
]