import requests
from bs4 import BeautifulSoup
import os
import json
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
headers = {'User-Agent':user_agent}
url ='https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90&order=14&asc=0&page=2&mode=s&jobsource=2018indexpoc'
res = requests.get(url,headers = headers)
soup = BeautifulSoup(res.text,'html.parser')
data = soup.select('h2[class="b-tit"]')
for i in data:
    try:
        print(i.a.text)
        print('http:' + i.a['href'])
        article_url = 'https://www.104.com.tw/job/4gj93?jobsource=hotjob_chr'
        article_res = requests.get(article_url,headers = headers)
        article_soup = BeautifulSoup(article_res.text,'html.parser')
        article_data = soup.select('script[type="application/ld+json"]')
        print(article_data)
    except AttributeError as e:
        print("--------")
