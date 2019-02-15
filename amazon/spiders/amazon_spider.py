import scrapy
from scrapy.selector import Selector
from amazon.items import AmazonItem

class AmazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["www.amazon.cn"]
    start_urls = [
        "https://www.amazon.cn/s/ref=lp_813272051_pg_2?rh=n%3A813108051%2Cn%3A813272051&page=2&ie=UTF8&qid=1550196173"
    ]

    def parse(self, response):
        items = []
        lists = response.xpath('//*[re:test(@id, "result_\d\d$")]').extract()
        for li in lists:
            Amazon = AmazonItem()
            Amazon['ymx_goods_name'] = Selector(text=li).xpath('//div/div[3]/div[1]/a/h2/text()').extract()
            Amazon['ymx_goods_price'] = Selector(text=li).xpath('//div/div[5]/div/a/span[2]/text()').extract()
            Amazon['ymx_goods_brand'] = Selector(text=li).xpath('//div/div[3]/div[2]/span[2]/text()').extract()
            items.append(Amazon)
        return items