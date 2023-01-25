from django.shortcuts import render
from django.http import HttpResponse
from .fetch_blog import BlogData

import json

# Create your views here.

def index(request):
    context = {
        'd': None,

    }
    return render(request, 'search/index.html', context)

def search(request):
    context = {
        "search_contain": None,
        "search_exclude": None,
        "search_author": None,
        "search_query": request.POST.get('search_query'),
        "article_data": [
            {
                "title": "노티드 연남 방문일지",
                "author": "주현준",
                "content": "노티드 연남에 가봤습니다. 우유 도넛이 아주 맛있습니다.",
                "link": "https://google.com",
                "author_link": "https://naver.com",
                "postdate": "2023-01-14",
            },
            {
                "title": "가로수길에 있는 모든 파스타집을 가본 제가 직접 엄선한 맛집들을 소개해드리겠습니다. 이 뒤부터는 truncatechars 테스트를 위한 내용 늘리기에 불과하니 읽으실 필요가 없습니다. 아직도 이걸 읽고 계신 당신은 호기심이 가득한 사람입니다.",
                "author": "홍길동",
                "content": "가로수길에 있는 모든 파스타집을 가본 제가 직접 엄선한 맛집들을 소개해드리겠습니다. 이 뒤부터는 truncatechars 테스트를 위한 내용 늘리기에 불과하니 읽으실 필요가 없습니다. 아직도 이걸 읽고 계신 당신은 호기심이 가득한 사람입니다. 가로수길에 있는 모든 파스타집을 가본 제가 직접 엄선한 맛집들을 소개해드리겠습니다.가로수길에 있는 모든 파스타집을 가본 제가 직접 엄선한 맛집들을 소개해드리겠습니다.",
                "link": "https://google.com/maps",
                "author_link": "https://kakaocorp.com",
                "postdate": "2023-01-21",
            },
        ]
    }
    if request.method == 'GET':
        return render(request, 'search/search.html', context=context)

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username, password=password)
            responce = redirect('pages:index')
            
            responce.set_cookie('username', user.username)
            responce.set_cookie('password', user.password)
            responce.set_cookie('is_login', True)

            return responce
        except User.DoesNotExist:  # 회원 정보가 없는 경우
            context['is_valid'] = False
            return render(request, 'users/login.html', context)
    


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