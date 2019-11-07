from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.
class Hashtag(models.Model):
    content = models.TextField(unique=True)

    def __str__(self):
        return self.content

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # M:N 관계 형성, 중계필드를 가져와서 원본필드를 바꾸는게 아니니까 makemigrations해서 상관없다.
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    hashtags = models.ManyToManyField(Hashtag, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-pk',)

    # method 추가 예정
    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'article_pk': self.pk})


class Comment(models.Model):
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # M:N 관계 형성

    def __str__(self):
        return self.content[:10]
    
    class Meta:
        ordering = ('-pk',)

    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'article_pk': article.pk})


# 보충수업
class Comment2(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-pk',)
    
    def __str__(self):
        return self.content



    