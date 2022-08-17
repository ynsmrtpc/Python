from pyexpat import model
from turtle import title
from django.db import models

class Article(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE) # ,verbose_name='Yazar' -> Türkçeleştirmek için
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__ (self):
        return self.title