from typing import Union
import json
import urllib.request
import urllib.parse
import urllib.error
import unicodedata


class BlogData:
    """사용 방법:
    BlogData 객체 생성,
    get() 혹은 get_item() 메소드를 통하여 데이터 반환
    
    <예시 코드>
    b = BlogData("맛집", 3)  # "맛집"을 검색하여 검색 결과 3개만 가져옴
    print(b.get())  # 검색 결과 전체 출력
    print(b.get_item(0))  # 검색 결과 중 첫(0)번째 게시물 데이터 출력
    
    !!주의사항!!
    비로그인 API는 일일할당량이 25000회 이므로, loop을 통하여 API를 호출하시면 안됩니다.
    25000회가 초과되면 더 이상 호출할 수 가 없습니다.

    Returns:
        _type_: _description_
    """
    CLIENT_ID = "2AJi5H0MWsa5Ng1wU9vM"
    CLIENT_SECRET = "RBwpJGfIPq"

    def __init__(self, query: str, limit: int, sort: str = "s") -> None:
        """네이버 블로그 API에 요청을 보냄

        Args:
            query (str): 검색어
            limit (int): 검색할 결과 개수 (1 ~ 100)
            sort (str, optional): 정렬 방법 (s: 정확도, d: 날짜 내림차순) (default: s)
        """
        self.response: dict = {"data": None}
        self.query = query
        self.limit = limit
        if (limit < 1 or limit > 100):
            self.response['status_code'] = 4
            self.response['status_msg'] = "Invalid limit parameter"
            return
        self.sort = sort
        if (sort not in ("s", "d")):
            self.response['status_code'] = 3
            self.response['status_msg'] = "Invalid sort parameter"
            return
        self._fetch()

    def _fetch(self) -> None:
        _query = urllib.parse.quote(self.query)
        _limit = self.limit
        _sort = "sim" if (self.sort == "s") else "date"
        _headers = {
            'X-Naver-Client-Id': self.CLIENT_ID,
            'X-Naver-Client-Secret': self.CLIENT_SECRET,
        }
        _req = urllib.request.Request(
            url="https://openapi.naver.com/v1/search/blog.json?"
                f"query={_query}&display={_limit}&sort={_sort}",
            headers=_headers,
        )
        try:
            with urllib.request.urlopen(_req) as response:
                self.response['status_code'] = 0
                self.response['status_msg'] = "Success"
                self.response['data'] = json.loads(
                    unicodedata.normalize("NFKC", response.read().decode("utf-8")))
                return
        except urllib.error.URLError as err:
            self.response['status_code'] = 2
            self.response['status_msg'] = err
            return

    def get(self) -> dict:
        """Response 객체를 dict 형태로 반환

        Returns:
            dict: {
                status_code    (int): 상태 코드 (0: 정상),
                status_msg     (str): 상태 메시지,
                data          (dict): 블로그 API 응답 객체 (default: None)
            }
        """
        return self.response

    def get_item(self, item_no: int) -> Union[dict, None]:
        """검색된 게시물 중 (item_no) 번째 게시물 정보를 반환
        
        만약 IndexError 혹은 Data가 없을 경우 None 반환
        
        Args:
            item_no (int): 검색결과 중 선택할 게시물의 index

        Returns:
            dict: 게시물 정보
        """
        if (not self.response['data']):
            return
        elif (len(self.response['data']['items'] <= item_no)):
            return
        else:
            return self.response['data']['items'][item_no]

