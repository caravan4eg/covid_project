import scrapy
from scraper.items import PostItem


class GoogleCovidPostSpider(scrapy.Spider):
    name = "google_covid_post_spider"
    start_urls = [
        "https://news.google.com/covid19/map?hl=ru&gl=RU&ceid=RU:ru"]

    # this is what start_urls does
    # def start_requests(self):
    #     urls = ['https://www.theodo.co.uk/team',]
    #     for url in urls:
    #       yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data = response.css("div.st-about-employee-pop-up")

        for line in data:
            item = PostItem()
            item["name"] = line.css("div.h3 h3::text").extract_first()
            item["image"] = line.css(
                "img.img-team-popup::attr(src)").extract_first()
            item["fun_fact"] = line.css(
                "div.p-small p::text").extract().pop()
            yield item
