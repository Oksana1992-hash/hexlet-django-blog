from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=200) #название статьи
    body = models.TextField() #тело статьи
    created_at = models.DateTimeField(auto_now_add=True) #для хранения даты и времени создания записи
    updated_at = models.DateTimeField(auto_now=True) #для хранения даты и времени последнего изменения записи
