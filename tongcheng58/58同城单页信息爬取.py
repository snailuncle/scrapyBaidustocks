import requests
from lxml import etree
import os
import time
import sys



def get_page(url):
    page_info=requests.get(url)
    page_info.raise_for_status()
    page_info_etree=etree.HTML(page_info.text)
    write_text(page_info.text)
    sys.exit()
    title=page_info_etree.xpath("/html/body/div[@id='content']/div[@class='person_add_top  no_ident_top']/div[@class='per_ad_left']/div[@class='col_sub mainTitle']/h1")
    price=page_info_etree.xpath("/html/body/div[@id='content']/div[@class='person_add_top  no_ident_top']/div[@class='per_ad_left']/div[@class='col_sub sumary']/ul[@class='suUl']/li[1]/div[@class='su_con']/span[@class='price c_f50']")
#    seller=page_info_etree.xpath("/html/body/div[@id='content']/div[@class='person_add_top  no_ident_top']/div[@class='per_ad_left']/div[@class='col_sub sumary']/ul[@class='suUl']/li[3]/div[@id='divContacter']/ul[@class='userinfo']/ul[@class='vcard']/li/a")
    seller=page_info_etree.xpath("//div[@id='divContacter']/ul[@class='userinfo']/ul[@class='vcard']/li/a")
    phone=page_info_etree.xpath("/html/body/div[@id='content']/div[@class='person_add_top  no_ident_top']/div[@class='per_ad_left']/div[@class='col_sub sumary']/ul[@class='suUl']/li[@class='wupin_b']/div[@class='su_con']/span[@id='t_phone']")
#    print(type(title), title[0].text.strip())

    print(seller, type(seller))
    data={
        'title':title[0].text.strip() if len(title) != 0 else "------", 
        'price':price[0].text.strip() if len(price) != 0 else "------", 
        'seller':seller[0].text.strip() if len(seller) != 0 else "------", 
        'phone':phone[0].text.strip() if len(phone) != 0 else "------", 
    }
    print(data)

def write_text(page_info):
    path=r"D:\scrapyProject\tongcheng58"
    if not os.path.exists(path):
        os.makedirs(path) 
        print('create_success')
        time.sleep(1)
    if page_info:

        pic_path=os.path.join(path, "58同城单页信息---查找联系人姓名.txt")

        print(pic_path)
#        if not os.path.exists(pic_path):
        with open(pic_path, 'w') as f:
            f.write(page_info)
            print("write_complete")
#        else:
#            print('contacter_file is exists')

def main():
    url='http://bj.58.com/shouji/32002131438529x.shtml'
    get_page(url)

if __name__=='__main__':
    main()



