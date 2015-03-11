# -*- coding: utf-8 -*-

# Scrapy settings for times_job project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'times_job'

SPIDER_MODULES = ['times_job.spiders']
NEWSPIDER_MODULE = 'times_job.spiders'

ITEM_PIPELINES = {'times_job.pipelines.MyFilesPipeline': 300}

FSFilesStore = '/home/prachi/python/times_job_pdf_files/'


#ITEM_PIPELINES = [
#    'times_job.files.FilesPipeline',
#]
FILES_STORE = '/home/prachi/python/times_job_pdf_files/'



# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'times_job (+http://www.yourdomain.com)'
