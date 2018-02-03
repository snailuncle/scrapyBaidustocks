from lxml import etree


# 定义一个函数，给他一个html，返回xml结构
def getxpath(html):
    return etree.HTML(html)


sample3 = """<html>
  <body>
    <ul>
      <li id="begin"><a href="https://scrapy.org">Scrapy</a>begin</li>
      <li><a href="https://scrapinghub.com">Scrapinghub</a></li>
      <li><a href="https://blog.scrapinghub.com">Scrapinghub Blog</a></li>
      <li id="end"><a href="http://quotes.toscrape.com">Quotes To Scrape</a>end</li>
      <li data-xxxx="end" abc="abc"><a href="http://quotes.toscrape.com">Quotes To Scrape</a>end</li>
    </ul>
  </body>
</html>
"""
# s3 = getxpath(sample3)
# s = s3.xpath('//li/a[@href="https://scrapinghub.com"]/text()')  # 返回列表,a标签后跟特性,特性放在中括号内,且用@前缀
# print(s)
# s = s3.xpath('//li[@id="begin"]/text()')
# print(s)
# s = s3.xpath('//li/a[text()="Scrapinghub"]/text()')
# print(s)
# s = s3.xpath('//li[@data-xxxx="end"]/text()')
# print(s)


sample4 = u"""
<html>
  <head>
    <title>My page</title>
  </head>
  <body>
    <h2>Welcome to my <a href="#" src="x">page</a></h2>
    <p>This is the first paragraph.</p>
    <p class="test">
    编程语言<a href="#">python</a>
    <img src="#" alt="test"/>javascript
    <a href="#"><strong>C#</strong>JAVA</a>
    </p>
    <p class="content-a">a</p>
    <p class="content-b">b</p>
    <p class="content-c">c</p>
    <p class="content-d">d</p>
    <p class="econtent-e">e</p>
    <p class="heh">f</p>
    <!-- this is the end -->
  </body>
</html>
"""
s4 = etree.HTML(sample4)

s = s4.xpath('//p[@class="test"]/text()')
print(s)
print("开始", ''.join(s))
s = s4.xpath('//p[@class="test"]/text()')
print(s)
s = s4.xpath('string(//p[@class="test"])')  # string括住  选择器  p标签 class特性  相对目录
print(s)
# p标签 标签特征[] 标签特征可以使用的方法starts-with() 该方法有两个参数,标签特性的名字,和特性的值的描述性字符串
s = s4.xpath('//p[starts-with(@class,"content")]/text()')
print(s)
s = s4.xpath('//p[contains(@class,"content")]/text()')
print(s)
