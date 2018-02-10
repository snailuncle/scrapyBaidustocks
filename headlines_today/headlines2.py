# coding=utf-8
import os
import requests
import json
import re
import pymongo
from urllib.parse import urlencode
from bs4 import BeautifulSoup
from hashlib import md5
from multiprocessing import Pool
from json.decoder import JSONDecodeError
from requests.exceptions import RequestException
# from config import *

#from .config import *

MONGO_URL = '10.163.46.92 '
MONGO_DB = 'toutiao'
MONGO_TABLE = 'toutiao'
GROUP_START = 1
GROUP_END = 3
KEYWARD = '街拍'

client = pymongo.MongoClient(MONGO_URL, connect=False)
db = client[MONGO_DB]


def get_page_index(offset, keyword):
    data = {
        "offset": offset,
        "format": "json",
        "keyword": keyword,
        "autoload": "true",
        "count": "20",
        "cur_tab": "1",
    }

    url = 'http://www.toutiao.com/search_content/?' + urlencode(data)
    print(url)
    response = requests.get(url)
    try:
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求索引出错', url)
        return None


def parse_page_index(html):
    try:
        data = json.loads(html)
        if data and 'data' in data.keys():
            for item in data.get('data'):
                yield item.get('article_url')
    except Exception as e:
        pass


def get_page_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # print(response.text)
            return response.text
        return None
    except Exception as e:
        print('请求详情页出错', url)
        print(e)
        return None


def parse_page_detail(html, url):
    try:
        title_pattern = re.compile("title: '(.*)',")
        title = re.search(title_pattern, html)
        print(title.group(1))
        title = title.group(1)
        content_pattern = re.compile("//(.*?)&quot;")
        content_urls = re.finditer(content_pattern, html)
        for url in content_urls:
            print("http://" + url.group(1))
            image = "http://" + url.group(1)
            download_image(image)
            return {'title': title, 'images': image}
    except Exception as e:
        print(e)

    # title = soup.select('title')[0].get_text()
    # print(title)
    # image_pattern = re.compile('gallery: (.*?)]},', re.S)
    # result = re.search(image_pattern, html)
    # if result:
    #     data = json.loads(result.group(1) + ']}')
    #     if data and 'sub_images' in data.keys():
    #         sub_images = data.get('sub_images')
    #         images = [item.get('url') for item in sub_images]
    #         for image in images:
    #             download_image(image)
    #         return {
    #             'title': title,
    #             'url': url,
    #             'images': images,
    #         }


def save_to_mongo(result):
    if db[MONGO_TABLE].insert(result):
        print('存储到mongodb成功', result)
        return True
    return False


def download_image(url):
    print('正在下载', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            save_image(response.content)
        return None
    except Exception as e:
        print('请求图片出错', url)
        return None


def save_image(content):
    file_path = '{0}/{1}.{2}'.format(os.getcwd(),
                                     md5(content).hexdigest(), 'jpg')
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(content)
            f.close()


def main(offset):
    html = get_page_index(offset, KEYWARD)
    for url in parse_page_index(html):
        html = get_page_detail(url)
        if html:
            result = parse_page_detail(html, url)
            if result:
                save_to_mongo(result)


if __name__ == '__main__':
    groups = [x * 20 for x in range(GROUP_START, GROUP_END)]
    pool = Pool()
    pool.map(main, groups)
    # get_page_index(3,KEYWARD)
    # main(0)
