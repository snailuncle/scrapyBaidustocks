# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import simplejson as json


class TencentPipeline(object):
    def __init__(self):
        # self.f = open("tencent.json", "w")
        self.f = open("tencent.json", "w", encoding='utf-8')


    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        # content = json.dumps(dict(item)) + ",\n"
        self.f.write(content)
        return item

    def close_spider(self, spider):
        self.f.close()
