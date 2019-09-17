from django.shortcuts import render
import requests
# Create your views here.

def artii(request):
    return render(request, 'artii/artii.html')

def result(request):
    word = request.GET.get('word')
    fonts = request.GET.get('fonts')
    url = f"http://artii.herokuapp.com/make?text={word}&font={fonts}"
    res = requests.get(url).text
    return render(request, 'artii/result.html', {'res':res})


