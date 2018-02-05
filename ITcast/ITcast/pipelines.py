# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import simplejson


class ItcastPipeline(object):
    def __init__(self):
        self.f = open("itcast_pipeline.json", "w", encoding='utf-8')
        # self.f = open("itcast_pipeline.json", "w")

    def process_item(self, item, spider):
        content = simplejson.dumps(dict(item), ensure_ascii=False) + ", \n"
        print('item=======================', item)
        # content = simplejson.dumps(dict(item)) + ", \n"
        print('content长度', len(content), 'content类型', type(content))
        print('content内容==============', content)
        self.f.write(content)
        # self.f.write(content)
        return item

    def close_spider(self, spider):
        self.f.close()


# JSON 相关概念：
# 序列化（Serialization）：将对象的状态信息转换为可以存储或可以通过网络传输的过程，传输的格式可以是JSON，XML等。反序列化就是从存储区域（JSON，XML）读取反序列化对象的状态，重新创建该对象。

# 　　   JSON（Java Script Object Notation）：一种轻量级数据交互格式，相对于XML而言更简单，也易于阅读和编写，机器也方便解析和生成，Json是JavaScript中的一个子集。

# 　　python2.6版本开始加入了JSON模块，python的json模块序列化与反序列化的过程分别是encoding和decoding。

# encoding：把一个python对象编码转换成Json字符串。
# decoding：把json格式字符串编码转换成python对象。
# 具体应用：

# 　　json提供四个功能：dumps, dump, loads, load

# dumps功能 ：将数据通过特殊的形式转换为所有程序语言都认识的字符串
# [html] view plain copy
# >>> import simplejson
# >>> data =['aa','bb','cc']
# >>> j_str = simplejsondumps(data)# Traceback (most recent call last):#   File "<stdin>", line 1, in <module># NameError: name 'simplejsondumps' is not defined
# >>> j_str = simplejson.dumps(data)# >>> j_str# '["aa", "bb", "cc"]'#
# loads功能 ： 将json编码的字符串再转换为python的数据结构
# [html] view plain copy
# >>> mes = simplejson.load(j_str)# Traceback (most recent call last):#   File "<stdin>", line 1, in <module>#   File "D:\Program
# Files\python\lib\site-packages\simplejson\__init__.py", line 455, in load#     return loads(fp.read(),# AttributeError: 'str' object has no
# attribute 'read'# >>> mes = simplejson.loads(j_str)# >>> mes# ['aa', 'bb', 'cc']
# 1 # dump功能
# 2 # 将数据通过特殊的形式转换为所有程序语言都认识的字符串，并写入文件
# 3 with open('D:/tmp.json', 'w') as f:
# 4     simplejson.dump(data, f)
# 1 # load功能
# 2 # 从数据文件中读取数据,并将json编码的字符串转换为python的数据结构
# 3 with open('D:/tmp.json', 'r') as f:
# 4     data = simplejson.load(f)

# 说明：

# 　　json编码支持的基本类型有：None, bool, int, float, string, list, tuple, dict.

# 　　对于字典，json会假设key是字符串（字典中的任何非字符串key都会在编码时转换为字符串），要符合JSON规范，应该只对python列表和字典进行编码。此外，在WEB应用中，把最顶层对象定义为字典是一种标准做法。

# 　　json编码的格式几乎和python语法一致，略有不同的是：True会被映射为true,False会被映射为false,None会被映射为null，元组()会被映射为列表[]，因为其他语言没有元组的概念，只有数组，也就是列表。

# 1 >>> import simplejson
# 2 >>> data = {'a':True, 'b':False, 'c':None, 'd':(1,2), 1:'abc'}
# 3 >>> j_str = simplejson.dumps(data)
# 4 >>> j_str
# 5 '{"a": true, "c": null, "d": [1, 2], "b": false, "1": "abc"}'
