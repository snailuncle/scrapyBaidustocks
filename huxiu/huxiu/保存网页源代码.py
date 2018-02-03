import requests

url = r'https://www.baidu.com/'
res = requests.session().get(url)
# print(res.status())
with open('huxiuHomePage.html','wb') as file:
    file.write(res.text.encode('utf-8'))
