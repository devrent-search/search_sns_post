from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

<<<<<<< HEAD
def index(request): #이것만....
    return HttpResponse('인덱스페이지.')
    #return render(request,'index.html')


def search(request): #이건 말고
    return HttpResponse('서치페이지.')


=======

def index(request):
    # 여기다가 코드 입력하시면 됩니다.
    return render(request, 'search/index.html')


def search(request):
    # 여기다가 코드 입력하시면 됩니다.
    return render(request, 'search/search.html')
>>>>>>> main
