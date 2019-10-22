import os
import jieba
source_path = r'./res_gossiping'
file_list = os.listdir(source_path)
article_str = ''
for article in file_list:
    with open(source_path + '/' + article, 'r', encoding='utf-8') as f:
        article_str += f.read().split('---split---')[0]
    new_str = article_str.replace('\n', ' ')
    s = jieba.cut(new_str)

    word_count = {}
    for w in '|'.join(s).split('|'):
        if w in word_count:
            word_count[w] += 1
        else:
            word_count[w] = 1
    print(word_count)