# _*_ coding:UTF-8 _*_
import requests
from bs4 import BeautifulSoup

'''
镇魂女孩爬取镇魂小说（python爬虫小白，代码后续会继续优化）
'''
if __name__ == '__main__':
    url = 'http://www.luoxia.com/zhenhun/'
    results = requests.get(url=url)
    results.encoding = 'utf-8'
    html = results.text
    bf = BeautifulSoup(html)
    texts = bf.find_all('div', class_='book-list')
    a_href = BeautifulSoup(str(texts[0]))
    a = a_href.find_all('a')
    for each in a:
        novel = requests.get(url=each.get('href'))
        novel.encoding = 'utf-8'
        bf_novel = BeautifulSoup(novel.text)
        novel_text = bf_novel.find_all('div', id='nr1')
        novel_text = novel_text[0].text
        with open('E:/test/' + each.string + '.txt', 'a', encoding='utf-8') as f:
            f.write(novel_text)