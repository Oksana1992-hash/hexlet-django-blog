from django.views import View
from django.shortcuts import render

class IndexView(View):
    template_name = "articles/index.html"

    def get(self, request, *args, **kwargs):
        tags = kwargs.get('tags', 'python')
        article_id = kwargs.get('article_id', 42)

        message = f'Статья номер {article_id}. Тег {tags}'
        context = {
            "app_name": "Статьи",
            "message": message,
        }
        return render(request, self.template_name, context)

