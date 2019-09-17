from django.shortcuts import render, redirect
from .models import Crud

# Create your views here.

def index(request):
    article = Crud.objects.all()
    context = {
        'article': article,
    }
    return render(request, 'crud/index.html', context)

def detail(request, pk):
    article = Crud.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'crud/detail.html', context)

def new(request):
    return render(request, 'crud/new.html')

def create(request):
    Crud.objects.create(
        title = request.GET.get("title"),
        content = request.GET.get("content"),
        image_url = request.GET.get("image_url"),
    )
    return redirect('home')

def delete(request, pk):
    article = Crud.objects.get(pk=pk)
    article.delete()
    return redirect('home')

def edit(request, pk):
    article = Crud.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'crud/edit.html', context)

def update(request, pk):
    article = Crud.objects.get(pk=pk)
    article.title = request.GET.get("title")
    article.content = request.GET.get("content")
    article.image_url = request.GET.get("image_url")
    article.save()

    return redirect(f'/crud/{pk}/')