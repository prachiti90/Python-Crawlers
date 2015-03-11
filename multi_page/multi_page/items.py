
import scrapy
from scrapy.item import Item, Field
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import TakeFirst


class Itemtype(scrapy.Item):
	book_title = Field()
	book_subtitle = Field()
	book_desc = Field()
	publisher = Field()
	author = Field()
	ebook_link = Field()
	subpage = Field()

class ItembookLoader(XPathItemLoader):
    default_item_class = Itemtype
    default_output_processor = TakeFirst()
	
