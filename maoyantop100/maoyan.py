# coding=utf-8 ##以utf-8编码储存中文字符

import requests
import re
from multiprocessing import Pool
from requests.exceptions import RequestException
import json

# 清空某文件,用来写入电影信息
with open('result.txt','w') as f:
    f.truncate()    
    
# 常量放最前
# http://maoyan.com/board/4?offset=10
url = 'http://maoyan.com/board/4'
user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
referer='http://maoyan.com/board'
# headers是一个字典dict
headers={"User-Agent":user_agent,'Referer':referer}

# 得到一张网页的内容
def get_one_page(url):
    try:
        response = requests.get(url,headers=headers)
        print('状态吗' + str(response.status_code))
        print('网页编码类型' + str(response.apparent_encoding))
        if response.status_code == 200:
            return response.text
        return 'response_error'
    except Exception as e:
        return 'get_one_page_except_error'

# 解析一个网页
def parse_page(page):
    pattern = re.compile('<dd.*?class="board-index.*?>(\d+)</i>.*?movieId:\d+}">.*?data-act="boarditem-click" data-val="{movieId:\d+}">(.+?)</a></p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i><i class="fraction">(.*?)</i></p>', re.S)
    items = re.findall(pattern,page)
    # print('*' * 50 + 'items')
    # print(items)
    for item in items:
        yield{
        'board-index':item[0],
        'name':item[1],
        'releasetime':item[2],
        'score':item[3] + item[4]
        }

        
# ensure_ascii=False在json.dumps中设置,
# encoding='utf-8'在with open中设置
# 写入文件
def write_content(content):
    with open('result.txt', 'a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False) + '\n')
        
    

# 主流程 
def main(offset):
    html = get_one_page(url + '?offset=' + str(offset))
    # print(html)
    # items = parse_page(html)
    print('*' * 50 + 'main_item')
    for item in parse_page(html):
        print(item)
        write_content(item)
    
 # 启动脚本   
if  __name__ == '__main__':
    for i in range(10):
        main(i*10)
    #多进程用法
    # pool = Pool()
    # pool.map(main, [i*10 for i in range(10)])
    
    
    
    
    
    
    
    
    
    
    
    
    