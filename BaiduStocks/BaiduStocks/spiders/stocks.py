# -*- coding: utf-8 -*-
import scrapy
import re
import sys

# import time


# 东方财富网   http://quote.eastmoney.com/stocklist.html
# 百度股票     http://gupiao.baidu.com/stock/
class StocksSpider(scrapy.Spider):
    # 这只爬虫的名字
    name = 'stocks'
    # 爬虫要爬的网址---起始网址
    start_urls = ['http://quote.eastmoney.com/stocklist.html']

    def parse(self, response):
        # 把所有股票编号写入文件---------------------------------
        with open("stocksTest.txt", 'w') as f:
            # 写入响应内容主体
            f.write('')
        # -------------------------------------------------------------
        count = 0
        # -------------------------------------------------------------

        # response响应对象中的a标签,a标签的属性,href属性的值
        for href in response.css("a::attr(href)").extract():
            # href写入文件
            # with open("stocksTest.txt", 'a') as f:
            #     # 写入响应内容主体
            #     f.write(href + '\n')
            # print('a标签中包含href属性的href条目=', href)
            # time.sleep(2)
            try:
                stock = re.findall(r"[s][hz]\d{6}", href)[0]

                # 把所有股票编号写入文件---------------------------------
                # with open("stocksTest.txt", 'a') as f:
                #     # 写入响应内容主体
                #     f.write(stock + '\n')
                # -------------------------------------------------------------

                url = "https://gupiao.baidu.com/stock/" + stock + ".html"
                # 把所有股票编号百度股票网址写入文件---------------------------------
                with open("stocksTest.txt", 'a') as f:
                    # 写入响应内容主体
                    f.write(url + '\n')
                # -------------------------------------------------------------
                # 此处回调函数---parse_stock
                # -------------------------------------------------------------
                print(count)
                count = count + 1
                if count > 100:
                    sys.exit("Error message")
                # -------------------------------------------------------------

                # yield scrapy.Request(url, callback=self.parse_stock)
            except BaseException:
                continue

    def parse_stock(self, response):
        infoDict = {}
        stockInfo = response.css(".stock-bets")
        name = stockInfo.css(".bets-name").extrack()[0]
        keyList = stockInfo.css("dt").extract()
        valueList = stockInfo.css("dd").extract()
        for i in range(len(keyList)):
            key = re.findall(r">.*</dt>", keyList[i])[0][1:-5]
            try:
                val = re.findall(r"\d+\.?.*</dd>", valueList[i])[0][0:-5]
            except BaseException:
                val = "--"
            infoDict[key] = val

        infoDict.update(
            {"股票名称": re.findall("\s.*\(", name)[0].split()[0] +
             re.findall("\>.*\<", name)[0][1:-1]})

        yield infoDict
