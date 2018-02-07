# -*- coding: utf-8 -*-
import scrapy
from huxiu.items import HuxiuItem
import sys
# 新闻xpath //*[@id="index"]/div[1]/div[2]/div[2]/div[3]/h2/a
# introduction

# --------------------------初代爬虫,打印作者,时间,标题等小条目-------------------------------------------------------------------------
# class HuxiuSpider(scrapy.Spider):
#     name = 'HuXiu'
#     allowed_domains = ['huxiu.com']
#     start_urls = ['http://huxiu.com/']

#     def parse(self, response):
#         # div标签中 class特性=mod-info-flow , 符合该div标签下的下级div标签,的下级div标签的class特性是mob-ctt的element列表
#         for s in response.xpath('//div[@class="mod-info-flow"]/div/div[@class="mob-ctt"]'):
#             print(s)
#             item = HuxiuItem()
#             item['title'] = s.xpath('h2/a/text()')[0].extract()
#             item['link'] = s.xpath('h2/a/@href')[0].extract()
#             # url = response.urljoin(item['link'])
#             item['author'] = s.xpath('div/a/span/text()')[0].extract()
#             item['introduction'] = s.xpath('div[2]/text()')[0].extract()
#             item['time'] = s.xpath('div/span/text()')[0].extract()
#             print(item)
# ------------------------------------------------------------------------------------------------------


class HuxiuSpider(scrapy.Spider):
    name = 'HuXiu'
    allowed_domains = ['huxiu.com']
    start_urls = ['http://huxiu.com/']

    def parse(self, response):
        for s in response.xpath('//div[@class="mod-info-flow"]/div/div[@class="mob-ctt"]'):
            item = HuxiuItem()
            item['title'] = s.xpath('h2/a/text()')[0].extract()
            item['link'] = s.xpath('h2/a/@href')[0].extract()
            url = response.urljoin(item['link'])
            item['author'] = s.xpath('div/a/span/text()')[0].extract()
            item['introduction'] = s.xpath('div[2]/text()')[0].extract()
            item['time'] = s.xpath('div/span/text()')[0].extract()
            print(item)
            # 把url抛给parse_article处理  翻译为解析条款--解析规则
            yield scrapy.Request(url, callback=self.parse_article)

    def parse_article(self, response):
        # print('parse_farticle响应', response)
        # print('response类型   ', response)
        # sys.exit("Error message")
        item = HuxiuItem()
        # detail细节  wrap围巾,包  article文章,签订协议
        detail = response.xpath('//div[@class="article-wrap"]')
        item['title'] = detail.xpath('h1/text()')[0].extract().strip()
        item['link'] = response.url
        item['author'] = detail.xpath('div[@class="article-author"]/span/a/text()')[0].extract()
        item['time'] = detail.xpath('div[@class="article-author"]/div[@class="column-link-box"]/span/text()')[0].extract()
        print(item)
        word = detail.xpath('div[5]')
        print(word[0].xpath('string(.)').extract()[0])
        yield item
