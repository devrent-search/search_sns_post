from django.shortcuts import render

# Create your views here.


def index(request):
    # 여기다가 코드 입력하시면 됩니다.
    return render(request, 'search/index.html')


def search(request):
    # 여기다가 코드 입력하시면 됩니다.
    return render(request, 'search/search.html')
