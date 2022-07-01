import requests
from bs4 import BeautifulSoup


response = requests.get("https://www.naver.com/")

#네이버에서 html 줌
html = response.text
#html번역 선생님으로 수프 만듦
soup = BeautifulSoup(html, 'html.parser')
#id 값이 NM_set_home_btn인 놈 한 개를 찾아냄
word = soup.select_one('#NM_set_home_btn')
#텍스트 요소만 출력
print(word.text)