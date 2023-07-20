from django.forms import ModelForm
from profile_app.models import Profile

class ProfileCreationForm(ModelForm) :
    class Meta :
        model = Profile
        fields = ['image', 'nickname', 'message']