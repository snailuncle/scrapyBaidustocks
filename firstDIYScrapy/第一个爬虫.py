import requests
from bs4 import BeautifulSoup
URL = "http://www.wise.xmu.edu.cn/people/staff"
r = requests.get(URL)
html = r.content
soup = BeautifulSoup(html, 'html.parser')
# print(soup)
div_people_list = soup.find('div', attrs={'class': 'module paged_list faculty_paged_list'})
print(div_people_list)
# commentList = soup.find('div', attrs={'class': 'PostCommentList'})
# print(commentList)
# a_s = div_people_list.find_all('a', attrs={'target': '_blank'})
# CommentItems = commentList.find_all('div', attrs={'class': 'CommentItem'})
# print(CommentItems)
# for info in CommentItem:
#     name = info.find()
#     theComment = 
# get_text(strip=True)
# method 1
# tags = soup.find('div').find_all('p')
# for i in tags:
#     # do something here
#     print i.text

# # method 2
# print soup.find('div').find('p').text
# print soup.find('div').find('p').find_next('p').text
# a.table.tr.td.string
