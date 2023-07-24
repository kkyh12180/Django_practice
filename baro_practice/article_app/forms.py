from django.forms import ModelForm
from article_app.models import Article

class ArticleCreationForm(ModelForm) :
    class Meta :
        model = Article
        fields = ['title', 'image', 'content']

        