import openpyxl
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

wb = openpyxl.load_workbook(r'C:\DataCrawlingProjects\StartCoding\Chapter04\파이썬 엑셀 다루기\참가자_data.xlsx')
ws = wb.active  #현재 활성화된 시트 선택

company_codes = [
    '207940',   #삼바
    '035720',   #카카오
    '035420',   #네이버
    '000120'    #cj대한통운
]

for com_code in company_codes:
    url = f"https://finance.naver.com/item/sise.naver?code={com_code}"

    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    price = soup.select_one('#_nowVal').text.replace(',', '')

    print(price)