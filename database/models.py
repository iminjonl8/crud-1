from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    name = models.CharField('Категория название', max_length=255)
    def __str__(self):
        return self.name


class News(models.Model):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
    title = models.CharField('Загаловок', max_length=255)
    content = models.TextField('Текст')
    category = models.ForeignKey(Categories, related_name ='categories', on_delete=models.CASCADE, null=True)
    created_at = models.DateField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField('Текст')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    news = models.ForeignKey(News, related_name='comments', on_delete=models.CASCADE, null=True)


