import scrapy

from urlparse import urljoin

from scrapy.spider import Spider
from scrapy.selector import Selector
from multi_page.items import Itemtype
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request



class DmozSpider(CrawlSpider):
    name = "linkbooks"
    allowed_domains = ["it-ebooks.info"]
    start_urls = [
        "http://it-ebooks.info/book/",
    ]
    rules = (
            Rule(SgmlLinkExtractor(allow=(r'/book/\d+/')), callback='parse_start_url', follow=True),
        )

    def parse_start_url(self, response):
        
        sel = Selector(response)
        

        item = Itemtype()
        item['book_title'] = sel.xpath('//h1/text()').extract()
        item['book_subtitle'] = sel.xpath('//h3/text()').extract()
        item['book_desc'] = sel.xpath('//td[@class="justify link"]/span/text()').extract()
        item['publisher'] = sel.xpath('//td[@class="justify link"]/table/tr[2]/td[2]/b/a/text()').extract()
        item['author'] = sel.xpath('//td[@class="justify link"]/table/tr[3]/td[2]/b[2]/a/text()').extract()
        item['ebook_link'] = sel.xpath('//td[@class="justify link"]/table/tr[11]/td[2]/a/@href').extract()

        yield item
       
