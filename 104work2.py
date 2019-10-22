import requests
from bs4  import BeautifulSoup
import os
import json
from urllib import request

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
headers = {'User-Agent':user_agent}
url ='https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90&order=14&asc=0&page=1&mode=s&jobsource=2018indexpoc'
res = requests.get(url,headers = headers)
soup = BeautifulSoup(res.text,'html.parser')
data = soup.select('h2[class="b-tit"]')
for i in data:
    try:
        print(i.a.text)
        print('http:'+i.a['href'])
        page = i.a['href'][21:26]
        article_url = 'https://www.104.com.tw/job/%s?jobsource=hotjob_chr'%(page)
        article_res = requests.get(article_url,headers = headers)
        article_soup = BeautifulSoup(article_res.text,'html.parser')
        article_data = article_soup.select('script[type="application/ld+json"]')
        js = json.loads(article_data[0].text)
        js1=js[0]['description']
        rm104 = re.findall(r'<[\s\S]*?>',js1)
        for i in rm104:
            js1=js1.replace(i,"")
        print(js1)
        print('=============================================== 分 隔 線 ======================================================')
    except AttributeError as e:
        print("--------")