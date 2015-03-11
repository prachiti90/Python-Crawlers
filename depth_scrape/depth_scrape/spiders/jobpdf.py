# -*- coding: utf-8 -*-
import scrapy
import math
import time

from urlparse import urljoin, urlparse

from scrapy.spider import BaseSpider

from scrapy.contrib.spiders.init import InitSpider
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


from scrapy.http import Request, FormRequest
from scrapy.selector import Selector
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request, FormRequest


from times_job.items import TimesJobItem
class TimesSpiderSpider(InitSpider):
    name = "times_spider"
    allowed_domains = ['hire.timesjobs.com']
    login_page = 'http://hire.timesjobs.com/employer/login.html'
    start_urls = (
        'http://hire.timesjobs.com/employer/login.html',
    )
    

    def init_request(self):
        """This function is called before crawling starts."""

        #LOGGING IN WITH SELENIUM
        self.driver = webdriver.Firefox()
        
        return Request(url=self.login_page, callback=self.login)

    def login(self, response):
        """Generate a login request."""
        print("\n\n \t\tGENERATE A LOGIN REQUEST.\n\n")

        print("\n\n \t\tLOGGING IN WITH SELENIUM.\n\n")

        self.driver.get(response.url)
        #USERNAME
        self.driver.find_element_by_xpath("/html/body/div[1]/aside/div[1]/div[1]/form/input[1]").clear()
        self.driver.find_element_by_xpath("/html/body/div[1]/aside/div[1]/div[1]/form/input[1]").send_keys("my_username")
        #PASSWORD
        self.driver.find_element_by_xpath("/html/body/div[1]/aside/div[1]/div[1]/form/input[2]").clear()
        self.driver.find_element_by_xpath("/html/body/div[1]/aside/div[1]/div[1]/form/input[2]").send_keys("my_password")
        #CLICK ON LOGIN
        self.driver.find_element_by_xpath("/html/body/div[1]/aside/div[1]/div[1]/form/div[1]/div/input").click()

        print("\n\n\t\tPASSING SESSION COOKIES FROM SELENIUM TO SCRAPY\n\n\t\t")
        my_cookies = self.driver.get_cookies()
        #print my_cookies

        return Request(url="http://hire.timesjobs.com/employer/activejobs.html?verticalId=0",
                cookies=self.driver.get_cookies(),
                callback=self.parse_item)

    def parse_item(self, response):
        

        print("\n\n \t\tSCRAPING LINK 1!\n\n \t\t")
        self.driver.get(response.url)
        job_type = response.xpath('/html/body/div/div[1]/div[2]/div[3]/div/div[3]/form/table/tbody/tr[3]/td/ul/li[1]/p[2]/a/@href').extract()
        times_url = 'http://hire.timesjobs.com/employer/'
        if (len(job_type) > 0):
            job_type_string = str(job_type[0])
            job_url = urljoin(times_url, job_type_string)
            yield Request(url=job_url, cookies=self.driver.get_cookies(), callback=self.parse_page)
        

        # Yield a new request for link we found
            
        

    def parse_page(self, response):

        print("\n\n \t\tSCRAPING LINK 2!\n\n \t\t")
        self.driver.get(response.url)
        #from scrapy.shell import inspect_response
        #inspect_response(response) 

        #applications = response.xpath('/html/body/div/div/div[2]/div[1]/div[4]/div[2]/div[1]/div[1]/a/text()').extract()
        #applications = str(applications)
        #no_applications = applications.split(' Applications')
        #total_applications = (no_applications[0])
        #total_applications = (total_applications)
        total_applications = 4373
        #pages = int(4373/20)
        no_of_pages = math.ceil(4373/20) #PAGINATION : per page 20 results.
        pages = int(no_of_pages) 
	total_pages = pages + 1
        print no_of_pages
        next_page = 1
        sel = Selector(response)
        counter = 1

        for next_page in range (1, total_pages):
            
            script = 'return vPagerBottom.showPage(%d)' %next_page
            self.driver.execute_script(script)
		# SELENIUM EXECUTES THE ALREADY PRESENT JAVASCRIPT FUNCTION FOR NEXT PAGE.
		# I DIDN'T USE ONCLICK() AS THE BUTTON FOR NEXT WAS NOT VISIBLE IN THE HTML CODE AND WAS DYNAMICALLY GENERATED.
            time.sleep(4) # TIME DELAY
            print("\n\n \t\tRESULTS FROM PAGE %d\n\n \t\t") %next_page
            # SCRAPING DATA WITH SELENIUM AS THE JAVASCRIPT FUNCTION RESPONSE IS SEEN IN SELENIUM AND NOT BY SCRAPY
            candidates = self.driver.find_elements_by_xpath('//a[contains(@href,"resumeDetailView")]')
            for candidate in candidates:
                candidate_profile_url = str(candidate.get_attribute('href'))
                print "Candidate URL: " + candidate_profile_url
                times_url = "http://hire.timesjobs.com/employer/"
		# THE COUNTER IS USED HERE AS THE FIRST ELEMENT WAS A BLANK LINK.
                if (counter > 1):
                    candidate_string = candidate_profile_url

                    job_candidate_url = urljoin(times_url, candidate_string)
                    time.sleep(3)
                    pdf_file_url = yield Request(url=job_candidate_url, cookies=self.driver.get_cookies(), callback=self.parse_pdf)
                    time.sleep(3)
                counter = counter + 1
        self.driver.close()


    def parse_pdf(self, response):

        #from scrapy.shell import inspect_response
        #inspect_response(response) 
        print("\n\n \t\tSCRAPING LINK 3!\n\n \t\t")
       
        pdf_file = response.xpath('/html/body/div[4]/div[1]/div[2]/a[1]/@href').extract()
        times_url = "http://hire.timesjobs.com/employer/"
        if (len(pdf_file) > 0):
            pdf_file_string = str(pdf_file[0])
            pdf_file_url = urljoin(times_url, pdf_file_string)
            # GENERATING FILE NAME 
            first = pdf_file_url.split("&name=")
            name = first[1].split("&linkFrom=")
            candidate_name = name[0]

            second = first[0].split("cwrId=")
            second_int = second[1].split("==&")
            file_id = second_int[0]

            resume_name = candidate_name+file_id

            yield TimesJobItem(pdf_urls=[{"file_url": pdf_file_url, "file_name": resume_name+"_data.doc"}])
        

    



