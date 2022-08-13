from ast import keyword
import requests
from bs4 import BeautifulSoup
import time

keyword = input()
response = requests.get("https://search.naver.com/search.naver?ie=UTF-8&sm=whl_sug&query=" + keyword)
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
        #print(soup)
        content = soup.select_one("#articeBody")
        print(content.text)
        time.sleep(0.3)