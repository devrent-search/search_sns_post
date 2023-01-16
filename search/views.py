from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request): #이것만....
    return HttpResponse('인덱스페이지.')
    #return render(request,'index.html')


def search(request): #이건 말고
    return HttpResponse('서치페이지.')


