# -*- coding: utf-8 -*-

# Scrapy settings for multi_page project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'multi_page'

SPIDER_MODULES = ['multi_page.spiders']
NEWSPIDER_MODULE = 'multi_page.spiders'

DEFAULT_ITEM_CLASS = 'multi_page.items.Itemtype'

#ITEM_PIPELINES = {'multi_page.pipelines.JsonWriterPipeline': 1}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'multi_page (+http://www.yourdomain.com)'
