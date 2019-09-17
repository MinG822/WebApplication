from django.shortcuts import render
from django.http import HttpResponse
#pip 에 들어가 있는 django.http pip 에 Lib sitepackages에 들어가면 임포트한 친구들이 들어가 있음
import random

# Create your views here.
def index(request):
    # return render_template('index.html')
    # request 는 사용자가 input한 내용을 받을 때
    return render(request, 'index.html')

def home(request):
    data = ['a', 'b']
    empty_data = []
    number = 10
    context = {
        'name': 'name',
        'data': data,
        'empty_data': empty_data,
        'number': number,
    }
    return render(request, 'home.html', context)

def lotto(request):
    lotto = random.sample(range(1,46),6)
    number = 10
    return render(request, 'lotto.html', {'lotto':lotto})

def cube(request, num):
    result = num ** 3
    context = {
        'result': result,
    }
    return render(request, 'cube.html', context)

def match(request):
    goonghap = random.randint(50, 101)
    # you = request.GET.get('you')
    # counterpart = request.GET.get('counterpart')
    test = request.path
    # 우리대신에 파싱해주는 친구. 쉽게 해준다. 
    context = {
        'you':request.POST.get('you'),
        'counterpart': request.POST.get('counterpart'),
        'goonghap': goonghap,
        'test': test,
    }
    return render(request, 'match.html', context)