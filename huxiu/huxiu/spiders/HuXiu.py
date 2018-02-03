# -*- coding: utf-8 -*-
import scrapy
from huxiu.items import HuxiuItem
# 新闻xpath //*[@id="index"]/div[1]/div[2]/div[2]/div[3]/h2/a
# introduction
class HuxiuSpider(scrapy.Spider):
    name = 'HuXiu'
    allowed_domains = ['huxiu.com']
    start_urls = ['http://huxiu.com/']

    def parse(self, response):
        for s in response.xpath('//div[@class="mod-info-flow"]/div/div[@class="mob-ctt"]'):
            print(s)
            item = HuxiuItem()
            item['title'] = s.xpath('h2/a/text()')[0].extract()
            item['link'] = s.xpath('h2/a/@href')[0].extract()
            url = response.urljoin(item['link'])
            item['author'] = s.xpath('div/a/span/text()')[0].extract()
            item['introduction'] = s.xpath('div[2]/text()')[0].extract()
            item['time'] = s.xpath('div/span/text()')[0].extract()
            print(item)
