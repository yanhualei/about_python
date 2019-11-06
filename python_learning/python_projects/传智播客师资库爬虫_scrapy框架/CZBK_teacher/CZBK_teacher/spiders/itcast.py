# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'  # 爬虫名字,启动爬虫时使用
    allowed_domains = ['itcast.cn']  # 目标域名
    start_urls = ['http://itcast.cn/']  # 初始爬取的url

    def parse(self, response):  # 爬虫解析函数:编辑爬取过程
        name = response.xpath('//div[@class="tea_con"]//li/div/h3/text()')
        print(name)
