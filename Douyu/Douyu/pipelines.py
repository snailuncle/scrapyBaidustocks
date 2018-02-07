# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
import os
from Douyu.settings import IMAGES_STORE as images_store
# from Tencent.items import TencentItem

# class DouyuPipeline(object):
#     def process_item(self, item, spider):
#         return
class DouyuPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        image_link = item['imagelink']
        yield scrapy.Request(image_link)

    def item_completed(self, results, item, info):
        # print(results)
        # print("*" * 30)
        # [(True, {'url': 'https://rpic.douyucdn.cn/live-cover/appCovers/2018/02/01/4228501_20180201040102_big.jpg', 'path': 'full
        # /026d54538ca1827e7633dca0b2a99d0e9697144f.jpg', 'checksum': 'a37dba7d5b005b90a845cd0478e4e9da'})]
        # 取出results图片信息中的  图片路径 值
        image_path = [x["path"] for ok, x in results if ok]

        os.rename(images_store + image_path[0], images_store + item["nickname"] + ".jpg")
