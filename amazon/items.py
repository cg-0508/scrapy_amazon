# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ymx_goods_name = scrapy.Field()
    ymx_goods_id = scrapy.Field()
    ymx_goods_sort_desc = scrapy.Field()
    ymx_goods_desc = scrapy.Field()
    ymx_goods_options = scrapy.Field()
    ymx_goods_price = scrapy.Field()
    ymx_goods_category = scrapy.Field()
    ymx_goods_format = scrapy.Field()
    ymx_goods_url = scrapy.Field()
    ymx_goods_keyword = scrapy.Field()
    ymx_goods_brand = scrapy.Field()
    # ymx_goods_shop_url = scrapy.Field()
    # ymx_goods_shop_name = scrapy.Field()
    
