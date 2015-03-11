# Depth Scraping
Recursively  scraping to a depth of 4, with FilesPipline to download files and Selenium for javascript.
 - In this crawler I get links from within the website and redirect scrapy to these links.
 - At the last link the '.doc' files are scraped using the FilePipeline.
 - The biggest challenge was AJAX PAGINATION.
 - The AJAX code generates no links for the next page, viz the HTML href was '#' for all next_page_link and previos_page_link.
 - Also the Next button and Previous button generated were not detected in the HTML code of response.body().
 - Using Selenium I login to the page and pass the session cookies to Scrapy for Scraping the redirection links.
 - At the last page the links to the '.doc' files are scraped using Selenium.
 - The Javascript Function defined within the source code of the webpage is then used to Generate the Next Page.


## Step by Step Demo.


 


  
