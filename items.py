# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LicoItem(scrapy.Item):
    # def __init__(self):
    #     # 如果实现了子类的构造，则必须声明父类构造，
    #     # 否则无法执行ItemProcess的process_item方法
    #     super().__init__()
    #     print('<INFO> LicoItem is instancing.')

    # define the fields for your item here like:
    price = scrapy.Field()
    words = scrapy.Field()
    # pass
