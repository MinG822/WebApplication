from django.shortcuts import render, redirect
from datetime import datetime
from .models import Article

# Create your views here.

# class Article:
#     def __init__(self, title, content, created_at):
#         self.title = title
#         self.content = content
#         self.created_at = created_at
    
#     def __str__(self):
#         return f'제목: {self.title}, 내용: {self.content}, 작성시간: {self.created_at}'

blogs = []

def index(request):
    articles = Article.objects.all()
    
    context = {
        'articles': reversed(articles),
    }

    return render(request, 'index.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get('articleTitle')
    content = request.GET.get('articleContent')
    img_url = request.GET.get('img_url')

    article = Article()
    article.title = title
    article.content = content
    article.img_url = img_url
    article.save()

    context = {
        'title' : title,
        'content' : content,
        'img_url' : img_url,
        'created_at' : article.created_at
    }
    
    return redirect('index')