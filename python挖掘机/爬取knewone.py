import requests
import sys
from lxml import etree
import time
import os  
import re

class T(object):
    n=0
    def add(self, x):
        T.n=T.n+x
        return T.n
        
    @staticmethod
    def add_staticmethod(x):
        T.n=T.n+x
        return T.n

def get_page(url, data=None):
#    try: 
    r=requests.get(url)
    r.raise_for_status()

    html=etree.HTML(r.text)
    
    titles=html.xpath("//article/header[@class='cover']/a[@class='cover-inner']/img/@alt")
    links=html.xpath("//article/header[@class='cover']/a[@class='cover-inner']/img/@src")
    for title, link in zip(titles, links):
        data={
            'title':title, 
            'link':link
        }
        print(data)
        write_pic(data)
        count=T().add(1)
        print('正在爬第%d张'%count)
            
#    except Exception as e:
#        print(e)
#        pass
#        sys.exit()

def get_more_pages(url, start, end):
    for i in range(start, end):
        get_page(url+str(i))
        time.sleep(2)

        
def write_pic(data):
    path=r"D:\test\pic2\knewone"
    if not os.path.exists(path):
        os.makedirs(path) 
        print('创建成功')
        time.sleep(1)
    if data:
        pic_title=data['title']
        pic_title = re.sub(r'/|\\', '--', pic_title)
        pic_link=data['link']

        pic_path=os.path.join(path, pic_title+'.jpg')

        print(pic_path)
        if not os.path.exists(pic_path):
            with open(pic_path, 'wb') as f:
                r=requests.get(pic_link)
                f.write(r.content)
                print("写入完成")
        
def generate_counter():
    CNT=[0]
    def add_one():
        CNT[0]=CNT[0]+1
        return CNT[0]
    return add_one

if __name__=='__main__':
    start, end=1, 200
    print(start)
    print(end)
    url='https://knewone.com/discover?page='
    get_more_pages(url, start, end)
    os.system('start '+r"D:\test\pic2\knewone")



















