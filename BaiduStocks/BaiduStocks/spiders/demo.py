# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    # allowed_domains = ['python123.io']
    start_urls = ['http://python123.io/ws/demo.html']

    def parse(self, response):
        # 响应网址的以"/"分隔的最后一个元素
        fname = response.url.split('/')[-1]
        # 创建一个文件,文件名是fname
        with open(fname, 'wb') as f:
            # 写入响应内容主体
            f.write(response.body)
        # 打印文件已保存
        self.log('Saved file %s.' % fname)
