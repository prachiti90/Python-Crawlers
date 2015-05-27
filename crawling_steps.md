
#Crawling Steps

I follow these steps for all my crawlers. 

Step 1 to 5 are only done once to isolate all resources and install scrapy for first time.

*Assuming you have PIP installed in python if not please Refer : https://pip.pypa.io/en/latest/installing.html*

1.Create folder my_crawlers. 
  >   Create document.txt file. I just write the design of the logic of the crawler here for myself.
  
2.Create virtual enviorment to isolate python resources. This is done in the parent directory. I use the same virtualenv for all my crawlers. So you have to create it only once.
	> 	virtualenv -p /usr/bin/python2.7 crawlerX
	
*Reference for virtualenv Installation : http://docs.python-guide.org/en/latest/dev/virtualenvs/*

3.Activate virtual env
	> 	prachi@Energy:~/python$ source crawlerX/bin/activate
		  OUTPUT : (crawlerX)prachi@Energy:~/python$ 

4.Now install lxml
	> 	(crawlerX)prachi@Energy:~/python$ pip install lxml

*Reference for lxml Installation : http://lxml.de/installation.html*

5.Install Scrapy
  >   (crawlerX)prachi@Energy:~/python$ pip install Scrapy

6.Start Scrapy Project
  >   (crawlerX)prachi@Energy:~/python$ scrapy startproject new_crawler_name
    OUTPUT:   You can start your first spider with:
                cd new_crawler_name
                scrapy genspider example example.com
              (crawlerX)prachi@Energy:~/python$ 

7.Create Item Class
  - Do cd new_crawler_name.
  - Now edit items.py according to your needs.
  
8.Create Spider
  - Do scrapy genspider my_spider_name www.scraping.site.name.com
  - Here my_spider_name is the name of the spider, The www.scraping.site.name.com will be put under allowed domains and genspider is the spider class/type that you are using.
  - Spider types that i have used are : Spider, InitSpider, CrawlSpider.
  
9.Create Pipeline
  - This is Optional. 
  - To create a pipline just edit the pipline.py file present next to items.py in your scrapy project folder.
  - However remember to edit the settings.py to activate your pipeline.
  
10.Run Crawler
  - Run your crawler as :
  >   scrapy crawl my_spider 
  - The name of the spider must be specified in the my_spider_name.py file.
  - To collect the output as json file, run crawler as:
  >   scrapy crawl my_spider -o crawler_output.json

