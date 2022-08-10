#네이버 금융 삼성전자 데이터 수집
import requests
from bs4 import BeautifulSoup

#함수형태 변환
#페이지의 HTML 코드를 변환
def get_bs_obj(com_code):
    url = "https://finance.naver.com/item/main.naver?code=" + com_code
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser") #html.parser 로 파이썬에서 쓸 수 있는 형태로 변환
    return bs_obj
    
def get_price(com_code):
    #호출
    bs_obj = get_bs_obj(com_code)
    #현재가 추출 #no_today 클래스명으로
    no_today = bs_obj.find("p", {"class":"no_today"})
    #가격만 추출
    blind_now = no_today.find("span", {"class":"blind"})
    return blind_now.text

print("네이버 주식 현재가 출력")
i=0
for i in range(3):
    #삼성전자 005930
    print("삼성전자 현재가")
    print(get_price("005930"))
    print()
    #셀트리온 068270
    print("셀트리온 현재가")
    print(get_price("068270"))
    print()
    #카카오 035720
    print("카카오 현재가")
    print(get_price("035720"))
    print()