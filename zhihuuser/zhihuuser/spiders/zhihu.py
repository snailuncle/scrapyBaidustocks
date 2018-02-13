# -*- coding: utf-8 -*-
import scrapy

# 轮子哥  关注列表
# https://www.zhihu.com/people/excited-vczh/following

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    def parse(self, response):
        pass
