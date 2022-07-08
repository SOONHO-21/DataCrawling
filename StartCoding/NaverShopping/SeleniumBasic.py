from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import warnings
import time
from selenium.webdriver.common.by import By

chrome_options = Options()
# 셀레니움 로그 무시
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
# Deprecated warning 무시 
warnings.filterwarnings("ignore", category=DeprecationWarning)
# 브라우저 생성
browser = webdriver.Chrome("c:/chromedriver.exe", options=chrome_options)

#웹사이트 열기
browser.get('https://www.naver.com/')
browser.implicitly_wait(10)
browser.find_element(By.LINK_TEXT,'쇼핑').click()
time.sleep(2)

#검색창 클릭
#클래스 이름으로 찾기
#browser.find_element(By.CLASS_NAME,'_searchInput_search_input_QXUFf').click()
search = browser.find_element(By.CLASS_NAME,'_searchInput_search_input_QXUFf')
search.click()

#검색어 입력 자동화
search.send_keys('갤럭시 S22')
search.send_keys(Keys.ENTER)