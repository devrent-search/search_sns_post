from django.shortcuts import render

from . import fetch_blog
# Create your views here.


def index(request):
    return render(request, 'search/index.html')


def search(request):
    search_contain = request.POST.get('search_contain')
    search_exclude = request.POST.get('search_exclude')
    search_author = request.POST.get('search_author')
    search_query = request.POST.get('search_query')
    
    # 위 4개의 변수들을 이용하여 결과물을 "article_data"에 넣으시면 됩니다.
    # 하실 일의 대부분은 예외처리와 받아온 데이터 가공입니다.
    
    if (not search_query):
        pass  # 검색어가 존재하지 않을 경우 예외처리

    blogdata = fetch_blog.BlogData(search_query, 100)
    if (blogdata.get()['status_code'] != 0):
        print("Error: " + blogdata.get()['status_message'])
        #  정상적으로 데이터를 받아오지 못했을 경우 예외처리
    else:
        articles = blogdata.get()['data']['items']
        processed_articles = []
        for article in articles:
            processed_articles.append("")  # 저희에게 필요한 형식에 맞게 데이터를 가공한 후 processed_articles에 append
            """
            데이터를 가공한다는 것은
            1. 포함/제외 단어, 작성자 필터에 맞는 article만 고르는 작업
            2. 템플릿에 직접적으로 들어가기 때문에 문자열을 다듬는 과정 (예를 들어 20220528 -> 2022-05-28 이런 식으로 변환)
            등의 작업을 말합니다.
            """
    context = {
        "search_contain": search_contain,
        "search_exclude": search_exclude,
        "search_author": search_author,
        "search_query": search_query,
        "article_data": [  # 여기에 processed_articles가 들어가면 됩니다. 우선 형식을 찾는 데 도움을 드리기 위해 그대로 놔두겠습니다.
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
    return render(request, 'search/search.html', context=context)
