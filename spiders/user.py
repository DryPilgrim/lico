import scrapy
import lico.variables as VAR

cookie = "PHPSESSID=3pjpq3o2vtijv4fmu5o68emkdv; uid=35557; email=dry782413632%40163.com; " \
         "key=906bf66d1dab797b209f4f5058ee66e8098ac55a696a2; ip=07baa5cc4c3411846bda96f4b8e801b4; " \
         "expire_in=1637238498; mtauth=2867c842941428cdf7d33e01cc286c31 "

class UserSpider(scrapy.Spider):
    name = 'user'
    allowed_domains = ['https://www.lico.club']
    start_urls = ['https://www.lico.club/user']
    reDayIn=0

    def start_requests(self):
        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookie.split("; ")}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
        )
        print('cookies:', cookies)

    def parse(self, response):
        # nonlocal reDay
        node_0 = response.xpath("//div[@class='font-size-h4 text-dark mb-2']")
        print("sdhfiubfhrb:\n", node_0)
        for node_0i in node_0:
            VAR.set_value('remainDay', node_0i.xpath("//span[@class='counter']/text()").extract()[0])
            break
        reDayIn = VAR.get_value('remainDay')
        print("sdhfiuab:", reDayIn, VAR.get_value('remainDay'))


# def set_():
#     tmp=UserSpider()
#     print("shfiuehfiu:",UserSpider.reDayIn)
#     VAR.set_value('remainDay', UserSpider.reDayIn)
