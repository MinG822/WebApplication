from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Post, Comment

# Create your views here.

def index(request):
    articles = Post.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'posts/index.html', context)

def detail(request, pk):
    # pk라는 id를 가진 글을 찾아와 보여줌
    article = Post.objects.get(pk=pk)
    aticles = Post.objects
    # 해당 글에 달려있는 모든 댓글을 보여줌
    comments = article.comment_set.all()
    context = {
        "article":article,
        "comments":comments,
        "article":article,
    }
    return render(request, 'posts/detail.html', context)

def create(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        content = request.POST.get("content")
        Post.objects.create(title=title, content=content)
        return redirect('posts:index')
    else:
        return render(request, 'posts/create.html')

def delete(request, pk):
    article = get_object_or_404(Post, pk=pk)
    article.delete()
    return redirect('posts:index')

def update(request, pk):
    article = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        article.title = request.POST.get("title")
        article.content = request.POST.get("content")
        article.save()
        return redirect('posts:index')
    else:
        context = {
            "article":article,
        }
        return render(request, 'posts/update.html', context)

def create_comment(request, pk):
    # 댓글 작성 후, 디테일 페이지로 리다이렉트
    Comment.objects.create(
        content=request.GET.get('content'),
        post=Post.objects.get(pk=pk),
    )
    return redirect('posts:detail', pk)