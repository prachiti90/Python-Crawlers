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

### 1. Here we have logged in with Selenium and scraping the first link with scrapy. The link is of the button "175 Applications Recieved"

![Scraping Link 1](https://cloud.githubusercontent.com/assets/8667031/6603580/1233ac84-c849-11e4-981d-72cea4c81564.png)
 
### 2. Redirecting to the link obtained Above, we now scrape the second link for the text "MBA-Marketing 7yrs exp in marketing [Pharmaceutical, Insurance]"

![Scraping Link 2](https://cloud.githubusercontent.com/assets/8667031/6603595/1f5f71e0-c849-11e4-9d3a-7abc141d6a8e.png)

### 3. Redirecting to the second link obtained Above, we now scrape the third link for the '.doc' file from "Download Resume"

![Scraping Link 3](https://cloud.githubusercontent.com/assets/8667031/6603598/256efdda-c849-11e4-83f7-287c725de765.png)

### 4. The Javascript Function for showPage from the web-page source is called by selenium to get the Next Page.
The Javascript Function can be seen for the 'onclick' attribute.

![Next Page Link](https://cloud.githubusercontent.com/assets/8667031/6603605/2af2cc82-c849-11e4-82a2-63188e170a7e.png)



## If you have a better Solution, please let me know. Happy Crawling...! 

  
