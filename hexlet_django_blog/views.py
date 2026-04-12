from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.urls import reverse
from django.views import View

class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = {
            "who": "World",
        }
        return render(request, self.template_name, context)


def about(request):
    return render(request, "about.html")

def home_redirect(request, tags=None, article_id=None):
    article_id = 42
    tags = 'python'

    return redirect(reverse('article', kwargs={'article_id': article_id, 'tags': tags}))

