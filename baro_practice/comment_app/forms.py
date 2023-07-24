from django.forms import ModelForm
from comment_app.models import Comment

class CommentCreationForm(ModelForm) :
    class Meta :
        model = Comment
        fields = ['content']