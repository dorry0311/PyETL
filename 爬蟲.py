import requests
from bs4 import BeautifulSoup
import os
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
headers = {'User-Agent':user_agent}
path = r'./res'
if not os.path.exists(path):
    os.mkdir(path)


    # temp = soup.findAll('div' , {'id': 'topbar'})
    # print(temp[0].a.text)
    # print('https://www.ptt.cc' + temp[0].a['href'])
    # tmp = soup.findAll('div',id = 'topbar')
    # print(tmp[0].a)
    # title = soup.findAll('a', class_ = 'board')
    # print()
    # for tmp_title in title:
    #     print(tmp_title.div.text)
    #     print('https://www.ptt.cc' + tmp_title['href'])
page_number = 10
while page_number > 0:
    try:
        url = 'https://www.ptt.cc/bbs/movie/index%s.html' % (page_number)
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        title1 = soup.select('div[class="title"]')
        for n, tmp_title1 in enumerate(title1):
            print(tmp_title1.a.text)
            article_url = 'https://www.ptt.cc' + tmp_title1.a['href']
            print(article_url)

            res_article = requests.get(article_url,headers=headers)
            soup_article = BeautifulSoup(res_article.text,'html.parser')
            article_content = soup_article.select('div[id="main-content"]')
            article_str = article_content[0].text.split('--')[0]

            push_up = 0
            push_down = 0
            score = 0
            push_tag = soup_article.select('div[class="push"] span')
            for p in push_tag:
                if '噓' in p.text:
                    push_down += 1
                if '推' in p.text:
                    push_up += 1
            score = push_up - push_down
            article_str += '\n--split--\n'
            article_str += '推:' + str(push_up) + '\n'
            article_str += '噓:' + str(push_down) + '\n'
            article_str += '分數:' + str(score) + '\n'

            try:
                with open('%s/%s.txt'%(path,tmp_title1.a.text.replace('/','-')),'w',encoding='utf-8') as f:
                    f.write(article_str)
            except OSError as e:
                with open('%sarticle%s.txt'%(path,n),'w', encoding='utf-8') as f:
                    f.write(article_str)
            print(article_str)
    except AttributeError as e :
        print('===============')
        print(e.args)
        print('===============')
    page_number -=1
    # url_last = 'https://www.ptt.cc' + soup.select('a[class="btn wide"]')[1]['href']
    # print(url_last)
    # url = url_last