import requests
from bs4 import BeautifulSoup
URL = "https://zhuanlan.zhihu.com/p/21377121?refer=xmucpp"
r = requests.get(URL)
html = r.content
soup = BeartifulSoup(html, 'html.parser')
# div_people_list = soup.find('div', attrs={'class': 'people_list'})
commentList = soup.find('div', attrs={'class': 'PostCommentList'})
# a_s = div_people_list.find_all('a', attrs={'target': '_blank'})
CommentItems = commentList.find_all('div', attrs={'class': 'CommentItem'})
for info in CommentItem:
    name = info.find()
    theComment = 
