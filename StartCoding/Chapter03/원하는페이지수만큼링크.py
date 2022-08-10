from turtle import title
from urllib import response
import requests
import pyautogui
from bs4 import BeautifulSoup

# response = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query="
# "%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90") #%EC%82%BC%...부분 : 삼성전자
keyWord = pyautogui.prompt("검색어를 입력하시오>>>")
lastPage = pyautogui.prompt("검색어를 입력하시오>>>")
pageNum = 1

#int(lastPage*10)로 하면 문자열*10이 되기 때문에 결론적으로 한도를 인식을 못해
#무한루프에 빠짐. 1부터 시작해서 10씩 더함. 1, 11, 21...
for i in range(1, int(lastPage)*10, 10):   
    print(f"============{pageNum}페이지 입니다.============")
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm="
    "tab_jum&query={keyWord}&start={i}")
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select(".news_tit") #결과는 list

    for link in links:
        title = link.text  #태그 안에 텍스토 요소를 가져온다
        url = link.attrs['href']    #속성값 중 'href' 값 출력
        print(title, url)
    pageNum = pageNum + 1