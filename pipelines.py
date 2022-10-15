# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv

from lico.spiders.myLico import MylicoSpider


class LicoPipeline(object):
    def __init__(self) -> None:
        self.f = open("lico.csv", "a", encoding='utf-8-sig', newline='')
        self.writer = csv.writer(self.f)
        self.writer.writerow(['price', 'words'])

    @staticmethod
    def process_item(self, item):
        print('==' * 20,'\n',item) #为什么这里接收的item和parse()里面的不一样
        self.writer.writerow([item['price'], item['words']])
        print("shfiuefhrg:\n", item['price'])
        return item

    def close_spider(self, spider):
        self.f.close()
