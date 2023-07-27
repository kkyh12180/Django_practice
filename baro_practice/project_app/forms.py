from django.forms import ModelForm
from project_app.models import Project

class ProjectCreationForm(ModelForm) :
    class Meta :
        model = Project
        fields = ['image', 'title', 'description']
        