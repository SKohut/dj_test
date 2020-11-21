from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    date = models.DateField()
    article_img = models.ImageField(upload_to = 'portfolio/article_img/')
