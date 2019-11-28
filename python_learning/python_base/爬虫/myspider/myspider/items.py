# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Dy_hpjySpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    room_type = scrapy.Field()
    room_id = scrapy.Field()
    anchor_name = scrapy.Field()
    room_link = scrapy.Field()
    hoot = scrapy.Field()
