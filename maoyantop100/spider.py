import requests
import re
from multiprocessing import pool
from requestsexceptions import RequestException
import json

# 常量放最前
url = 'http://maoyan.com/board/4'
user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
referer='http://maoyan.com/board'
# headers是一个字典dict
headers={"User-Agent":user_agent,'Referer':referer}

def get_one_page(url):
    try:
        response = requests.get(url)
        print('状态吗' + response.status_code)
        if response.status_code == 200:
            return response.text
        return 'response_error'
    except:
        return 'get_one_page_except_error'


def parse_page(page):
    pattern = re.cpmpile('<dd.*?movieId:\d+}">.*?data-act="boarditem-click" data-val="{movieId:\d+}">(.+?)</a></p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i><i class="fraction">(.*?)</i></p>', re.S)
    items = re.compile(pattern,page)
    for item in items:
        print('*' * 50)
        print(item)

def write_content(content):
    pass

    
def main():
    html = get_one_page(url)
    # print(html)
    parse_page(html)
    
    
if  __name__ == '__main__':
    main()