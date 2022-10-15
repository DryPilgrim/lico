from urllib.parse import urljoin
from lico.send_email import sendEmail
import scrapy
import re
from lico.items import LicoItem
import lico.variables as VAR

# VAR._init()

cookie = "PHPSESSID=3pjpq3o2vtijv4fmu5o68emkdv; uid=35557; email=dry782413632%40163.com; " \
         "key=906bf66d1dab797b209f4f5058ee66e8098ac55a696a2; ip=07baa5cc4c3411846bda96f4b8e801b4; " \
         "expire_in=1637238498; mtauth=2867c842941428cdf7d33e01cc286c31 "


class MylicoSpider(scrapy.Spider):
    name = 'myLico'
    allowed_domains = ['https://www.lico.club']
    start_urls = ['https://www.lico.club/user/shop', 'https://www.lico.club/user']

    def start_requests(self):  # 重写了spider的start_requests方法
        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookie.split("; ")}
        yield scrapy.Request(
            self.start_urls[0],
            # callback=self.parse,#这个应该可以省略，因为start_requests()默认将结果返回给parse进行解析
            cookies=cookies
        )
        # print('cookies:', cookies)

    def parse(self, response):
        node = response.xpath("//div[@class='col-xs-6 col-sm-6 col-md-6 col-lg-4 col-xl-4 col-xxl-3']")
        print('jfidsdef:', node, len(node))
        item = LicoItem()
        for node_i in node:
            item['price'] = \
                node_i.xpath("//div[@class='display-3 text-primary font-weight-bolder'][1]/strong[1]/text()").extract()[
                    0]
            item['words'] = \
                node_i.xpath("//div[@class='d-flex flex-column w-100 pl-2 pt-3']/span/span/text()").extract()[0]
            # print('=', item['words'])
            break
        print('------' * 5)
        print('--:', item, item['price'], item['words'])
        yield item
        # res = re.findall("此商品限购剩余", response.body.decode())
        # print(res, len(res))

        # if item['price'] == '2.99' and item['words'] == '此商品已售空, 可尝试购买其它时长':
        #     sendEmail()
