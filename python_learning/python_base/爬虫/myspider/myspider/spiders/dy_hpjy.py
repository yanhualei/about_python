# -*- coding: utf-8 -*-
import scrapy


class Dy_hpjySpider(scrapy.Spider):
    name = "dy_hpjy"  # 爬虫的名字:斗鱼和平精英分区爬虫
    allowed_domains = ["douyu.com"]  # 爬取目标域名，也是爬虫爬取的范围，防止爬虫爬到了其他网站
    start_urls = ('https://www.douyu.com/g_hpjy',)  # 开始爬取的url

    def parse(self, response):  # 提取数据的方法，response是爬虫中间件传过来的数据
        li_list = response.xpath("//ul[@class='layout-Cover-list']/li")
        print(type(li_list))
        for li in li_list:
            item = {}
            item["room_type"] = li.xpath('.//span[@class="DyListCover-zone"]/text()').extract_first()
            item['room_id'] = li.xpath('.//a[@class="DyListCover-wrap"]/@href').extract_first()
            item['anchor_name'] = li.xpath('.//div[@class="DyListCover-info"]/h2/text()').extract_first()
            item['room_link'] = "https://www.douyu.com" + li.xpath('.//a[@class="DyListCover-wrap"]/@href').extract_first()
            item['hot'] = li.xpath('.//div[@class="DyListCover-content"]/div[2]/span/text()').extract_first()
            yield item
