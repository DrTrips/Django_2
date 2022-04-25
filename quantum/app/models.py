from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Student(models.Model):
    """
    Класс со студентами
    """
    user_surname = models.CharField(max_length=50, verbose_name='Surname')
    user_name = models.CharField(max_length=25, verbose_name='Name')
    user_age = models.IntegerField(verbose_name='Age')

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return str(f'{self.user_name} {self.user_surname} {self.user_age}')


class Article(models.Model):
    article_title = models.CharField('название статьи', max_length=250)
    article_text = models.TextField('текст статьи')
    pub_date = models.DateTimeField('дата публикации')


    def __str__(self):
        return self.article_title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('имя автора', max_length=50)
    comment_text=models.CharField('текст комментария', max_length=500)
    comment_pub_date = models.DateTimeField('дата публикации')


    def __str__(self):
        return self.author_name
