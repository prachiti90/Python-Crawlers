import scrapy
from scrapy.spider import Spider
from scrapy.selector import Selector
from it_books.items import Books


class DmozSpider(Spider):
    name = "itbooks"
    allowed_domains = ["it-ebooks.info"]
    start_urls = ["http://it-ebooks.info/tag/programming"]

    def parse(self, response):
        
        sel = Selector(response)
        sites = sel.xpath('/html/body/table/tr[2]/td/table/tr/td')
        #items = []

        for site in sites:
            item = Books()          
            item['title'] = site.xpath('a/text()').extract()         
            item['desc'] = site.xpath('text()').extract()
            yield item
  
