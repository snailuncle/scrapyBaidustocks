from lxml import etree


# 定义一个函数，给他一个html，返回xml结构
def getxpath(html):
    return etree.HTML(html)


sample2 = """
<html>
  <body>
    <ul>
      <li>Quote 1</li>
      <li>Quote 2 with <a href="...">link</a></li>
      <li>Quote 3 with <a href="...">another link</a></li>
      <li><h2>Quote 4 title</h2> ...</li>
    </ul>
  </body>
</html>
"""
s2 = getxpath(sample2)

li = s2.xpath('//li/text()')  # 相对路径// 标签名 + / + text方法
print(li)
# 获取第一个li
li1 = s2.xpath('//li/text()')[0]  # 返回列表中的一个条目
print(li1)
li2 = s2.xpath('//li[position() = 1]/text()')  # 返回列表
print(li2)
li3 = s2.xpath('//li[position()=3]/text()')  # 标签li li列表的位置方法的值 text()方法
print(li3)
li4 = s2.xpath('//li[position() mod2 = 1]/text()')
print(li4)
li5 = s2.xpath('//li[position() mod2 = 0]/text()')  # li标签 position()方法(可以使用mod函数) text()方法
print(li5)
liLast = s2.xpath('//li[last()]/text()')
print(liLast)
liA = s2.xpath('//li[a]/text()')
print('liA', liA)
liAH2 = s2.xpath('//li[a or h2]/text()')  # li标签后的中括号  是位置方法position() 或者 字符匹配
print(liAH2)
aAndH2 = s2.xpath('//a/text()|//h2/text()')  # 两种选择器放在同一对引号中
print(aAndH2)
