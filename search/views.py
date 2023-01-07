from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

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