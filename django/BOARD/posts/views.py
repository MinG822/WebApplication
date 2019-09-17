from django.shortcuts import render, redirect
from .models import Post

# Create your views here.

def index(request):
    # 게시판 테이블 형태로 보여주기
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'posts/index.html', context)

def new(request):
    return render(request, 'posts/new.html')

def create(request):

    Post.objects.create(
        title = request.GET.get("title"),
        content = request.GET.get("content"),
        image_url = request.GET.get("image_url"),
    )
    # 이 방법은 데이터 유효성 검사를 할 때 SAVE를 기점으로 하는데, CREATE방법을 쓰면 그게 힘들다. 
    # 원라인으로, 대신 칼럼명과 인풋네임이 같아야한다. 또 불순물이 없어야한다.

    # Post.objects.create(**request.GET)

    return redirect('home')

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post
    }
    return render(request, 'posts/detail.html', context)

def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()

    return redirect('home')

def edit(request, pk):
    # pk라는 id를 가진 글을 편집하게 함
    # 1. pk라는 id를 가진 글을 찾음
    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'posts/edit.html', context)

def update(request, pk):
    # pk라는 id를 가진 글을 찾아서
    # /edit/으롭터 날아온 데이터를 적용하여 변경함
    post = Post.objects.get(pk=pk)
    post.title = request.GET.get("title")
    post.content = request.GET.get("content")
    post.image_url = request.GET.get("image_url")
    post.save()

    return redirect(f'/posts/{pk}/')
    