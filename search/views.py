from django.shortcuts import render
from django.http import HttpResponse
from .fetch_blog import BlogData
from django.contrib import messages

#BlogData로부터 나온 데이터를 딕셔너리화하기 위한 클래스
class ResultData:
    def __init__(self, title=None, author=None, content=None, link=None, author_link=None, postdate=None):
        def delete_b_tag(string):
            return string.replace('<b>', '').replace('</b>', '')
            
        self.title = delete_b_tag(title)
        self.author = delete_b_tag(author)
        self.content = delete_b_tag(content)
        self.link = delete_b_tag(link)
        self.author_link = delete_b_tag(author_link)
        self.postdate = postdate[:4] + "-" + postdate[4:6] + "-" + postdate[6:]


    def is_valid(self, search_contain: str = "", search_exclude: str = "", search_author: str = ""):
        if search_contain: #search contain이 있을때 검사
            if search_contain not in self.title \
                and search_contain not in self.content: # search contain이 하나도 포함되지 않으면
                return False
        if search_exclude:
            if search_exclude in self.title \
                or search_exclude in self.content: # search exclude이 하나라도 포함되면  
                return False
        if search_author:
            if search_author != self.author: # 작성자가 아니라면
                return False
        return True

#필터링 가능하도록 오버라이드한 클래스
class BlogCroller(BlogData):
    def iter_item(self):
        if self.response['data']:
            for element in self.response['data']:
                result = ResultData(
                    title = element['title'],
                    author = element['bloggername'],
                    content = element['description'],
                    link = element['link'],
                    author_link = element['bloggerlink'],
                    postdate = element['postdate']
                )
                if result.is_valid(self.search_contain,self.search_exclude,self.search_author):
                    # 필터조건 충족시
                    yield result.__dict__ 

        
    def __init__(self, query: str, limit: int, sort: str = "s", search_contain: str = "",search_exclude: str = "",search_author: str = "" ) -> None:
        super().__init__(query, limit, sort)
        self.search_contain = search_contain
        self.search_exclude = search_exclude
        self.search_author = search_author
                

# Create your views here.

def index(request):
    return render(request, 'search/index.html')

from django.views.decorators.http import require_POST

contain_key = 'search_contain'
exclude_key = 'search_exclude'
author_key = 'search_author'
query_key = 'search_query'
article_data_key = 'article_data'

@require_POST
def search(request):
    search_contain = request.POST.get(contain_key)
    search_exclude = request.POST.get(exclude_key)
    search_author = request.POST.get(author_key)
    search_query = request.POST.get(query_key)

    # 검색어가 없을 경우
    if not search_query:
        pass

    context = {
            contain_key: search_contain,
            exclude_key: search_exclude,
            author_key: search_author,
            query_key: search_query,
            article_data_key: []
        }

    try:
        blog_croller = BlogCroller(
            search_query, 100,
            search_contain=search_contain,
            search_exclude=search_exclude, 
            search_author=search_author
            )  # 크롤링
    except: 
        # request.POST에 데이터 없는 경우
        return render(request, 'search/search.html', context=context)
    
    for each_item in blog_croller.iter_item():
        #크롤링 API로부터 얻어온 데이터 추가
        context[article_data_key].append(each_item)

    return render(request, 'search/search.html', context=context)
    