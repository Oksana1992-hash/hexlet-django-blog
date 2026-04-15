from django.forms import ModelForm # Импортируем формы Django
from .models import Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']