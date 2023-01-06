from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('인덱스페이지.')


def search(request):
    return HttpResponse('서치페이지.')


