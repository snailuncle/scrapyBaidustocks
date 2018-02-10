import requests
from requests.exceptions import RequestException

def main():
    url = 'https://www.toutiao.com/a6520762859721327111/'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print('图集展示页面', response.text)
            return response.text
        return None
    except RequestException:
        print('请求详情页出错',url)
        return None
        
        
if __name__=='__main__':
    main()