'''
chapter16_crawling 패키지 생성

main.py 파일 생성

pip : 파이썬 패키지 관리자, 파이썬 패키지를 설치하는 데 사용

requests 라이브러리는 파이썬에서 HTTP 요청을 보내기 위해 가장 널리 사용되는
    라이브러리 중 하나로, 사용하기 쉽고 직관적인 API를 제공하여
    HTTP 요청과 응답을 쉽게 처리할 수 있다.
    requests 라이브러리를 사용하면 GET, POST, PUT, DELETE 등 다양한
    HTTP  메서드를 간편하게 사용 가능.

1. 웹크롤링의 이해
    웹 크롤링(Web Crawling)이란 완성된 웹 페이지에서 필요한 정보를 수집하고
        선별하여 추출하는 과정으로, Web scraping이라고 하기도 함.

    1) HTML의 개념
        Hyper Text Markup Language의 약자로 '웹 페이지를 만드는 문법을 갖춘 언어'
        각자의 역할이 정해진 태그들로 구성된 언어로, 페이지를 만드는데
        각각의 태그를 붙여가며 사용.

    2) HTML의 구조
        <html>
            head
                meta
                title
            body
                h1
                div
        </html>
    3) URL : Uniform Resource Locator의 약자로 어떤 자원의 위치를 표기하는 방법을 의미함.
    https://google.com 과 같은 인터넷 주소를 입력하는데, 이때 입력한 주소가 URL에 해당.
'''
import requests

# url = "https://www.naver.com"       #naver 메인 페이지 주소를 url 변수에 저장
# response = requests.get(url)        # requests 모듈의 get() 메서드를 호출하여 그 결과(response)를
#                                     # response라는 변수에 담았습니다.
# print(f"응답 코드 : {response.status_code}")
# print(response.text)
'''
        2. 검색 결과 웹 페이지 정보 가져오기
            네이버에서 "파이썬"을 검색했을 때 나오는 결과 화면을 가져오는 방법
            
https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=파이썬 

검색하는 것이 함수라면 -> 그 결과값이 return이 될건데요. -> 검색어는 argument가 되겠죠

def searchResult(query):
    pass
    
result = searchResult("파이썬")
           
입력한 검색어 "파이썬"은 query라는 매개변수로 전달됩니다.
검색어와 관련된 부분은 query 매개변수이기 때문에 나머지는 지워도 무방합니다.
https://search.naver.com/search.naver?query=파이썬
'''
# url = "https://search.naver.com/search.naver"
# searching_word = input("검색어를 입력하세요 >>> ")
# param = {
#     "query": searching_word,
#     "ie": "utf8",
# }
# response = requests.get(url, params=param)
# # 일부만 keyword argument를 사용 / print(어쩌고, end="")
#
# print(response.text)


'''
무직백수 계백순의 소개 페이지를 가져오는 프로그램을 작성하시오.
'''
url = "https://comic.naver.com/webtoon/list"

