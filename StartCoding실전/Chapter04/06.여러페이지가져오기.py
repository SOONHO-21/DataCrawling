# from turtle import title
# from urllib import response
# import requests
# import pyautogui
# from bs4 import BeautifulSoup
# import time

# # response = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query="
# # "%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90") #%EC%82%BC%...부분 : 삼성전자
# keyWord = pyautogui.prompt("검색어를 입력하시오>>>")
# lastPage = pyautogui.prompt("검색어를 입력하시오>>>")
# pageNum = 1

# #int(lastPage*10)로 하면 문자열*10이 되기 때문에 결론적으로 한도를 인식을 못해
# #무한루프에 빠짐. 1부터 시작해서 10씩 더함. 1, 11, 21...
# for i in range(1, int(lastPage)*10, 10):   
#     print(f"============{pageNum}페이지 입니다.============")
#     response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyWord}&start={i}")
#     html = response.text
#     soup = BeautifulSoup(html, 'html.parser')
#     links = soup.select(".news_tit") #결과는 list

#     for link in links:
#         title = link.text  #태그 안에 텍스토 요소를 가져온다
#         url = link.attrs['href']    #속성값 중 'href' 값 출력
#         print(title, url)
#     pageNum = pageNum + 1
#     articles = soup.select("div.info_group") #뉴스기사 10개 추출
# for article in articles:
#     links = article.select("a.info")    # a태그인데 info class인 애들
#     if len(links) >= 2: #링크가 2개 이상이면
#         url = links[1].attrs['href']    #두 번째 링크의 URL 추출
#         response = requests.get(url, headers={'User-agent' : 'Mozila/5.0'})
#         html = response.text
#         soup = BeautifulSoup(html, 'html.parser')
#         print(url)
#         #만약 스포츠뉴스 기사면
#         if "sports" in response.url:
#             title = soup.select_one("title")
#             content = soup.select_one("#newsEndContents")
#             divs = content.select("div")
#             for div in divs:
#                 div.decompose()
#             paragraphs = content.select("p")
#             for p in paragraphs:
#                 p.decompose()
#         #만약 연예뉴스 기사면
#         elif "entertain" in response.url:
#             title = soup.select_one("h4.title")
#             content = soup.select_one("#articeBody")
#         else:
#             title = soup.select_one(".media_end_head_headline")
#             content = soup.select_one("#dic_area")
#         print(title)
#         print(content.text)
#         time.sleep(0.3)
from turtle import title
import pyautogui
import requests
from bs4 import BeautifulSoup
import time

keyWord = pyautogui.prompt("검색어를 입력하시오>>>")
lastPage = int(pyautogui.prompt("몇 페이지까지 크롤링 할까요?"))

pageNum = 1
for i in range(1, int(lastPage)*10, 10):
    print(f"{pageNum}페이지 크롤링 중입니다.=================")
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyWord}&start={i}")
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    articles = soup.select("div.info_group") #뉴스기사 10개 추출
    for article in articles:
        links = article.select("a.info")    # a태그인데 info class인 애들
        if len(links) >= 2: #링크가 2개 이상이면
            url = links[1].attrs['href']    #두 번째 링크의 URL 추출
            response = requests.get(url, headers={'User-agent' : 'Mozila/5.0'})
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            print(url)
            #만약 스포츠뉴스 기사면
            if "sports" in response.url:
                title = soup.select_one("title")
                content = soup.select_one("#newsEndContents")
                divs = content.select("div")
                for div in divs:
                    div.decompose()
                paragraphs = content.select("p")
                for p in paragraphs:
                    p.decompose()
            #만약 연예뉴스 기사면
            elif "entertain" in response.url:
                title = soup.select_one(".end_tit")
                content = soup.select_one("#articeBody")
            else:
                title = soup.select_one(".media_end_head_headline")
                content = soup.select_one("#dic_area")
            print(url)
            print(title)
            print(content.text.strip())
            time.sleep(0.3)
    pageNum = pageNum + 1