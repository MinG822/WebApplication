from django.shortcuts import render, redirect, HttpResponse
from .models import Answer, Question

# Create your views here.

def index(request):
    questions = Question.objects.all()
    context = {
        questions: "questions",
    }
    return render('eithers/index.html', context)
def new(request):
    if request.method == 'POST':
        Question.objects.create(
            title = request.POST.get('title'),
            issue_a = request.POST.get('issue_a'),
            issue_b = request.POST.get('issue_b'),
            image_a = request.FILE.get('image_a'),
            image_b = request.FILE.get('image_b')
        )
        return redirect('index')
    else:
        return render(request, 'eithers/new.html')

def detail(request, pk):
    picked_question = Question.objects.get(pk=pk)
    context = {
        picked_question: "picked_question",
    }
    return render('either/detail.html', context)

def answers_create(request):
    if HttpResponse == "POST":
        comment

def answers_delete(request):
    pass
