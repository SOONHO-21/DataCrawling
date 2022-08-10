from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import warnings

chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 셀레니움 로그 무시
warnings.filterwarnings("ignore", category=DeprecationWarning) # Deprecated warning 무시 

browser = webdriver.Chrome("c:/chromedriver.exe", options = chrome_options)
browser.get('https://www.naver.com')
browser.implicitly_wait(2) #로딩이 끝날동안 2초 기다린다

browser.find_element(By.CSS_SELECTOR, 'a.nav.shop').click() #쇼핑메뉴 클릭
time.sleep(2)

#검색창 클릭
search = browser.find_element(By.CSS_SELECTOR, 'input._searchInput_search_input_QXUFf')
search.click()

#검색어 입력
search.send_keys('아이폰 13')
search.send_keys(Keys.ENTER)

#무한 스크롤
before_h = browser.execute_script("return window.scrollY")
while True:
    browser.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.END) #맨 아래로 스크롤 내림
    time.sleep(2) #스크롤 사이 페이지 로딩 시간
    after_h = browser.execute_script("return window.scrollY")
    if after_h == before_h:
        break
    before_h = after_h

#상품 정보 div
items = browser.find_elements(By.CSS_SELECTOR, '.basicList_info_area__17Xyo')
#find_elements:리스트 반환
for item in items:
    name = item.find_element(By.CSS_SELECTOR, '.basicList_title__3P9Q7').text
    try:
        price = item.find_element(By.CSS_SELECTOR, '.price_num__2WUXn').text
    except:
        price = "판매중단"
    link = item.find_element(By.CSS_SELECTOR, '.basicList_title__3P9Q7 > a').get_attribute('href')
    print(name, price, link)