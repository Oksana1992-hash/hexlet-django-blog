from django.views import View
from django.shortcuts import render

class IndexView(View):
    template_name = "articles/index.html"

    def get(self, request, *args, **kwargs):
        context = {
            "app_name": "Статьи",
        }
        return render(request, self.template_name, context)

