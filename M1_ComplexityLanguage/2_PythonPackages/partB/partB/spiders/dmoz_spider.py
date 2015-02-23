############################################
# dmoz_spider.py
#
# Written by:
#   Erika Burdon
#   eburdonGIT@gmail.com
#
# This is a Scrapy web crawler to parse the Python Package Index for package names, descriptions, Source upload date and size of download.
# This was written for SEng 371 - Software Evolution at the University of Victoria, Spring 2014, as part of my research project into the evolution
#   of the Python language. It was written/modified from the original scrapy tutorial files because I'm a lazy cheater and didn't want to set up 
#   new/original work from scratch. Sorry.
#
# Compile:   ---
# Run:  scrapy crawl PyPiIndex -o items.json        *** All output yieled into formatted JSON file; remove '-o items.json' to display on cmd line
############################################

import scrapy

from scrapy.selector    import Selector
from scrapy.http        import HtmlResponse

class MyItem(scrapy.Item):
    url     = scrapy.Field()
    descr   = scrapy.Field()
    type    = scrapy.Field()
    # These may be lists! (E.g., several package uploads/updates)
    upload  = scrapy.Field()
    size    = scrapy.Field()


class DmozSpider(scrapy.Spider):
    name            = "PyPiIndex"      # Executable name of scraper
    allowed_domains = ["pypi.python.org"]
    start_urls      = ["https://pypi.python.org/pypi?%3Aaction=index"] 
    
    # Starting parsing function; Parse index table and create a list (to iterate through) of every package currently available.
    # Collect intial data: Package name and description. Follow included URL link (parsePackPage)
    def parse(self, response):
        packageList = []
        
        # Rows are split into even/odd; Ignore and parse ALL
        rows = response.xpath('//table[@class="list"]/tr')
        
        for row in rows:
            # Constructor; set some initializers
            my_item = MyItem()
            my_item['upload']   = "yyyy-mm-dd"
            my_item['size']     = "0KB"
            my_item['type']     = "Undefined"
            
            # Get package description from table
            my_item['descr'] = row.select('.//td/text()').extract()
            
            # Get package URL (Not unicode, string!); following addrs later (table)
            tempURL = row.select('.//a/@href').extract()
            lenTMP = len(tempURL)
            
            if lenTMP == 0:
                # Add for completeness
                my_item['url'] = "NO URL GIVEN"
                continue
            else:
                # Add string part ONLY of unicode
                my_item['url'] = tempURL[0]
            packageList.append(my_item)
        
        
        # Now I need to follow every [valid] URL and collect stats about the package
        for PACKAGE in packageList:
            if PACKAGE['url'] != "NO URL GIVEN":
                tail_url = PACKAGE['url']
                full_url = "http://pypi.python.org" + tail_url

                # Request creates a response object that executes callback function
                request = scrapy.Request(full_url, callback=self.parsePackPage)
                request.meta['item'] = PACKAGE
                yield request
            # If no URL found, do nothing
    
    
    ## Parse the URL links of packages (their index information pages; all same format!)
    def parsePackPage(self, response):
        item    = response.meta['item']
        rows    = response.xpath('//table[@class="list"]/tr')
        dates   = []
        sizes   = []
        types   = []
        
        # Will always have that top (zero) and last (nth) rows to skip
        rowCount = len(rows)
        
        for rowiter in range(1, rowCount-1):
            tempFormat = rows[rowiter].select('.//td[2]/text()').extract()
            tempType = str(tempFormat[0]).strip()
            tempDate = rows[rowiter].select('.//td[4]/text()').extract()
            tempSize = rows[rowiter].select('.//td[5]/text()').extract()
            # Parsed as Unicode; append ONLY the string part!
            types.append(tempType)
            dates.append(tempDate[0])
            sizes.append(tempSize[0])
        item['type']    = types
        item['upload']  = dates
        item['size']    = sizes
        
        return item