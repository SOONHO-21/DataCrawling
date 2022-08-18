# import requests
# from bs4 import BeautifulSoup

# date = str(datetime.now()) 
# date = date[:date.rfind(':')].replace(' ', '_') 
# date = date.replace(':','시') + '분'

# query = input('검색 키워드를 입력하세요 : ') 
# query = query.replace(' ', '+') 

# news_num = int(input('총 필요한 뉴스기사 수를 입력해주세요(숫자만 입력) : '))

# news_url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={}'

# req = requests.get(news_url.format(query))
# soup = BeautifulSoup(req.text, 'html.parser')

# print(soup)

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
        content = soup.select_one("#dic_area")
        print(content.text)
        time.sleep(0.3)