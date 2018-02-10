import requests
import json
import time
from requests.exceptions import RequestException
from urllib.parse import urlencode
from bs4 import BeautifulSoup


# 得到索引页的内容
def get_page_index(offset, keyword):
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'cur_tab': 1,
        'from': 'search_tab'
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    print(url)
    # https://www.toutiao.com/search_content/?offset=0&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&cur_tab=1&from=search_tab
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求索引页面出错')
        return None


# 开始解析索引页
def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('url')


# 得到详情页的内容
def get_page_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求详情页面出错', url)
        return None


# 得到详情页的title和data(json字符串)
def parse_page_detail(html):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select('title')[0].get_text()
    print(title)
    image_pattern = re.compile('', re.S)
    result = re.search(image_pattern, html)
    if result:
        print(result.group(1)


def main():
    html = get_page_index(0, '街拍')
    for url in parse_page_index(html):
        html = get_page_detail(url)
        time.sleep(3)
        if html:
            parse_page_detail(html)

if __name__ == '__main__':
    main()
