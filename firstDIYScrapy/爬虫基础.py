import requests
import re
r= requests.get('https://book.douban.com')
content = r.text
print(r.)
print(content)
# pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>', re.S)
# results = re.findall(pattern, content)
# for result in results:
#     url, name, author, date = result
#     author = re.sub('\s', '', author)
#     date = re.sub('\s', '', date)
#     print(url, name, author, date)
# 打开一个文件
fo = open("foo.txt", "w")
fo.write(icontent)
 
# 关闭打开的文件
fo.close()
