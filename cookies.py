import requests
from bs4 import BeautifulSoup
import os
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
headers = {'User-Agent':user_agent}
url = 'https://www.ptt.cc/bbs/movie/index.html'
#res = requests.get(url, headers=headers,cookies = {'over18':'1'})
ss = requests.session()
ss.cookies['over18'] = '1'
res = ss.get(url,headers=headers)

soup = BeautifulSoup(res.text,'html.parser')
print(soup.prettify())