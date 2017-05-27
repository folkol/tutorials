# -*- coding: utf-8 -*-
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ElectronicsSpider(CrawlSpider):
    name = 'electronics'
    allowed_domains = ["www.olx.com.pk"]
    start_urls = [
        'https://www.olx.com.pk/computers-accessories/',
        'https://www.olx.com.pk/tv-video-audio/',
        'https://www.olx.com.pk/games-entertainment/'
    ]
    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.pageNextPrev',)),
             # process_links="process_link",
             callback='parse_item',
             follow=True),)

    def process_link(self, url):
        print('Processing..' + url)
        # print(response.text)

    def parse_item(self, response):
        print('Processing..' + response.url)

    # def parse(self, response):
    #     pass


process = CrawlerProcess()
process.crawl(ElectronicsSpider)
process.start()
