# -*- coding: utf-8 -*-
import scrapy


class MydomainSpider(scrapy.Spider):
    name = 'mydomain'
    # allowed_domains = ['mydomain.com']
    # start_urls = ['http://mydomain.com/']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
