from cgitb import html
from urllib import response

import requests

response = requests.get("https://www.naver.com") #변수 response에 NAVER로부터의
                                                #원격 api호출
html = response.text
print(html)