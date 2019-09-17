from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Todo
from decouple import config
from bs4 import BeautifulSoup
import requests
from django.views.decorators.csrf import csrf_exempt
import json
from pprint import pprint


# Create your views here.

def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todos/index.html', context)

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due-date')
        Todo.objects.create(title=title, due_date=due_date)

        token = config("TELTEGRAM")
        base = "https://api.telegram.org/bot"
        method1 = "getUpdates"
        method2 = "sendMessage"
        url1 = f"{base}{token}/{method1}"
        text = f"{due_date}까지 해야할 일정 {title}이 등록되었습니다."
        response = requests.get(url1).json()
        chatgroup = []
        for i in range(len(response["result"])):
            chatid = response["result"][i]["message"]["from"]["id"]
            print(i)
            if chatid not in chatgroup:
                chatgroup.append(chatid)
                url2 = f"{base}{token}/{method2}?chat_id={chatid}&text={text}"
                requests.get(url2)
        return redirect('todos:index')
    else:
        return render(request, 'todos/create.html')
        

def update(request, pk):
    todo = get_object_or_404(Todo, id=pk)

    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due-date')
        todo.title = title
        todo.due_date = due_date
        token = config("TELEGRAM")
        base = "https://api.telegram.org/bot"
        method1 = "getUpdates"
        method2 = "sendMessage"
        url1 = f"{base}{token}/{method1}"
        text = f"{due_date}까지 해야할 일정 {title}이 수정되었습니다."
        response = requests.get(url1).json()
        chatgroup = []
        for i in range(len(response["result"])):
            chatid = response["result"][i]["message"]["from"]["id"]
            print(i)
            if chatid not in chatgroup:
                chatgroup.append(chatid)
                url2 = f"{base}{token}/{method2}?chat_id={chatid}&text={text}"
                requests.get(url2)
        todo.save()
        return redirect('todos:index')
    else:
        context = {
            'todo': todo
        }
        return render(request, 'todos/update.html', context)

def delete(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    todo.delete()
    return redirect('todos:index')

@csrf_exempt
def telegram(request):
    print(request.method)
    res = json.loads(request.body)
    token = config("TELEGRAM")
    base = "https://api.telegram.org/bot"
    method2 = "sendMessage"
    text = res.get('message').get('text')
    chat_id = res.get('message').get('chat').get('id')
    url2 = f"{base}{token}/{method2}?chat_id={chat_id}&text={text}"
    requests.get(url2)
    return HttpResponse('메시지')