from lxml import etree


# 定义一个函数，给他一个html，返回xml结构
def getxpath(html):
    return etree.HTML(html)


# 下面是我们实战的第一个html
sample1 = """<html>
  <head>
    <title>My page</title>
  </head>
  <body>
    <h2>Welcome to my <a href="#" src="x">page</a></h2>
    <p>This is the first paragraph.</p>
    <!-- this is the end -->
  </body>
</html>
"""
# 获取xml结构
s1 = getxpath(sample1)

# 获取标题(两种方法都可以)
# 有同学在评论区指出我这边相对路径和绝对路径有问题，我搜索了下
# 发现定义如下图
title1 = s1.xpath('//title/text()')  # 相对路径 两个斜杆 title标签   title标签的text方法
title2 = s1.xpath('/html/head/title/text()')  # 绝对路径 网页跟目录 斜杆 html标签 head标签 title标签 text方法
print('title1 =', title1)  # 返回为列表
print('title2 =', title2)
src = s1.xpath('//@src')  # 两个斜杆 相对路径 属性用符号@索引
print(src)
href = s1.xpath('//@href')
print(href)
text = s1.xpath('//text()')  # 相对路径 方法带括号,不用@符号
print(text)
comment = s1.xpath('//comment()')
print(comment)
