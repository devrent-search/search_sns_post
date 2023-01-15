from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

<<<<<<< HEAD
def index(request):
    context = {
        'd': None,
    }
    return render(request, 'index.html', context)


def search(request):
    context = {
        'test': "12345",
        'debug': True,
    }
    return render(request, 'search/sample.html', context)
=======

def index(request):
    # 여기다가 코드 입력하시면 됩니다.
    return render(request, 'search/index.html')


def search(request):
    # 여기다가 코드 입력하시면 됩니다.
    return render(request, 'search/search.html')
>>>>>>> oshmos
