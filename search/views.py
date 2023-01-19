from django.shortcuts import render
from django.http import HttpResponse
from fetch_blog import BlogData

import json

# Create your views here.

def index(request):
    context = {
        'd': None,

    }
    return render(request, 'search/index.html', context)

def search(request):
    context = {
        'test': "12345",
        'debug': True,
        
        'search_contain':" ", #포함단어
        'search_exclude':" ", #제외 단어
        'search_author' :" ", #작성자
        'search_query' :" ", #검색어
        'article_data' :[], #블로그 게시물 검색결과
    }

    return render(request, 'search/sample.html', context)


if __name__ == '__main__':
    blogData = BlogData("맛집",3)
    a = blogData.get()
    print(a['data'])


"""
def index(request):
    # 여기다가 코드 입력하시면 됩니다.
    return render(request, 'search/index.html')


def search(request):
    # 여기다가 코드 입력하시면 됩니다.
    return render(request, 'search/search.html')
"""