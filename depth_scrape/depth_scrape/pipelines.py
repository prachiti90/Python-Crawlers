# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.contrib.pipeline.files import FilesPipeline
from scrapy.http import Request


class MyFilesPipeline(FilesPipeline):
	def get_media_requests(self, item, info):
		for file_spec in item['pdf_urls']:
			#wrong_url = file_spec["file_url"]
			#first_split = wrong_url.split("<")
			#second_split = first_split[1].split(">")
			#third_split = second_split[0].split("GET ")
			#final_url = third_split[1]
			yield Request(url=file_spec["file_url"], meta={"file_spec": file_spec})

	def file_path(self, request, response=None, info=None):
		return request.meta["file_spec"]["file_name"]

class TimesJobPipeline(object):
    def process_item(self, item, spider):
        return item
