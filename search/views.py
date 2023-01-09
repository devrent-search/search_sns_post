from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'search/index.html')  # TODO: 01/06 백엔드

def search():
    pass  # TODO: 01/06 백엔드
