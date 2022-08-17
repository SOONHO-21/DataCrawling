from turtle import title
from urllib import response
import requests
import pyautogui
from bs4 import BeautifulSoup


# response = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query="
# "%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90") #%EC%82%BC%...부분 : 삼성전자
keyWord = pyautogui.prompt("검색어를 입력하시오>>>")
#f String 사용
response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyWord}")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.select(".news_tit") #결과는 list

for link in links:
    title = link.text  #태그 안에 텍스토 요소를 가져온다
    url = link.attrs['href']    #속성값 중 'href' 값 출력
    print(title, url)