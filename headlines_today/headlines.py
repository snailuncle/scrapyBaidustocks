# 今日头条爬虫 更新日期  2018 02 11
# coding=utf-8 ##以utf-8编码储存中文字符
import requests
import json
import re
import os
from hashlib import md5
# import time
from requests.exceptions import RequestException
from urllib.parse import urlencode
from bs4 import BeautifulSoup


# 清空某文件,用来写入图集链接信息
with open('索引页.txt', 'w') as f:
    f.truncate()


# https://www.toutiao.com/search_content/?offset=80&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&cur_tab=1&from=search_tab
# 得到索引页的内容
def get_page_index():
    print('get_page_index', '*' * 50)
    data = {
        'offset': '20',
        'format': 'json',
        'keyword': '福',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab'
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    print('索引页', url)
    try:
        response = requests.get(url)
        print('get_page_index状态码', response.status_code)
        if response.status_code == 200:
            content = response.text
            # print('索引页的内容是:', content)
            # with open('索引页.txt', 'w', encoding='utf-8') as f:
            #     f.write(json.dumps(content, ensure_ascii=False))
            # with open('索引页.txt', 'w') as f:
            #     f.write(content)
            return content
        return None
    except RequestException:
        print('请求索引页面出错')
        return None


# 开始解析索引页  格式化为json对象  用json.get()方法,提取data,再提取article_utl
# article_url就是图集的链接地址
def parse_page_index(html):
    print('parse_page_index', '*' * 50)
    try:
        print('开始json化')
        data = json.loads(html)
        print('完成json化')
        # data = html
        if data and 'data' in data.keys():
            for item in data.get('data'):
                # print('parse_page_index    item', item)
                item_content = item.get('article_url')
                if item_content:
                    # with open('索引页.txt', 'a') as f:
                    #     f.write('\n' + '*' * 50 + '\n' + '\n' + '\n' + item_content + '\n' + '\n' + '\n' + '*' * 50)
                    yield item_content
                else:
                    print("if item_content:")
            else:
                print("for item in data.get('data'):")
        else:
            print("if data and 'data' in data.keys():")
    except Exception as e:
        print(e)
        pass


# 得到详情页的内容
def get_page_detail(url):
    print('get_page_detail', '*' * 50)
# ----------------------------------------------------------------------
    # url = 'https://www.toutiao.com/a6441465438442127617/'
    try:
        # ---------------------请求响应返回空----------------------------------------------------------------------------------------
        # ---------------------添加请求头----------------------------------------------------------------------------------------
        user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.32 Safari/537.36'
        # referer='http://maoyan.com/board'
        # # headers是一个字典dict
        headers = {"user-agent": user_agent}
        response = requests.get(url, headers=headers)
        print('get_page_detail状态码',  str(response.status_code))
        if response.status_code == 200:
            print('get_page_detail', 'url', response.url)
            content = response.text
            # print('get_page_detail', 'content', content)
            # with open('索引页.txt', 'a', encoding='utf-8') as f:
            #         f.write('\n' + content)
            return content
        return None
    except RequestException:
        print('请求详情页面出错', url)
        pass


# 得到详情页的title和data(json字符串)
def parse_page_detail(html):
    print('parse_page_detail', '*' * 50)
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select('title')[0].get_text()
    print(title)
    #                           gallery: JSON\.parse\("(.*?})"\),
    image_pattern = re.compile('gallery: JSON\.parse\("(.*?})"\),', re.S)
    result = re.search(image_pattern, html)
    print('\n' + '*' * 50 + '\n' + '\n' + '\n' + 'help' + '\n')
    # help(result)
    if result:
        print('\n' + '*' * 50 + '\n' + '\n' + '\n' + 'image_pattern_result' + '\n')
        data = result.group(1)
        print(type(data), 'data')
        if data:
            data = re.sub(r'\\', '', data)
            pictures_dict = json.loads(data)
            print(type(pictures_dict), 'pictures_dict')
            if pictures_dict:
                print('pictures_dict', 'right')
                # print(pictures_dict)
                if 'sub_images' in pictures_dict.keys():
                    sub_images = pictures_dict.get('sub_images')
                    images = [item.get('url') for item in sub_images]
                    print('images', type(images))
                    return images
                    # help(sub_images)
                    # images = [item.get('url') for item in sub_images]
                # help(dict)
                # if 'sub_images' in data.keys():
                #     sub_images = data.get('sub_images')
                #     images = [item.get('url') for item in sub_images]
                #     return {
                #         'title': title,
                #         'images': images
                #     }
            else:
                print('pictures_dict = json.loads(data)', 'wrong')
        else:
            print('pictures_dict', 'wrong')

    # if result:
    # *********************loads方法,把字符串转换为  dict   或者   list   ,   外面必须是单引号,里面必须是双引号
    #     data = json.loads(result.group(1))
    #     if data and 'sub_images' in data.keys():
    #         sub_images = data.get('sub_images')
    #         images = [item.get('url') for item in sub_images]
    #         return {
    #             'title': title,
    #             'images': images
    #         }
    else:
        print('\n' + '*' * 50 + '\n' + '\n' + '\n' + 'image_pattern_result', 'wrong')


def download_image(url):
    print('正在下载', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            save_image(response.content)
    except Exception as e:
        print('请求图片出错', url)
        return None


def save_image(content):
    file_path = '{0}/{1}.{2}'.format(os.getcwd() + '/pic',
                                     md5(content).hexdigest(), 'jpg')
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(content)
            f.close()


def main():
    k = 1
    print('main', '*' * 50)
    html = get_page_index()
    for url in parse_page_index(html):
        print('单个图集的链接地址:', url)
        html = get_page_detail(url)
    #     time.sleep(3)
        if html:
            result = parse_page_detail(html)
            print(result)
            if result:
                with open('索引页.txt', 'a', encoding='utf-8') as f:
                    f.write(json.dumps(result, ensure_ascii=False) + '\n')
                # 遍历result类型  list   保存该列表中,所有链接的图片到文件夹
                for picture_url in result:
                    download_image(picture_url)
                    print("保存数量：%s   图片链接：%s" % (k, picture_url))
                    k = k + 1


if __name__ == '__main__':
    main()
