#/usr/bin/Python
# Python download size parser

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by   import By
from itertools import izip

import string

DRIVER = None

#################################################

def parse_raw_text(DRIVER):
    print "RAW TEXT FILE, YO"
    ## merp = DRIVER.getPageSource().contains("text to search");
    
def parse_web_page(DRIVER):
    print "FANCY WEB PAGE, YO"
    ## merp = DRIVER.find_element_by_xpath("//div[contains(., 'Release date:')]")
    # print merp.text

def main():
    global DRIVER

    # Open firefox
    DRIVER = webdriver.Firefox()
    
    # Open close
    DRIVER.get("https://www.python.org/downloads/")
    assert 'Python.org' in DRIVER.title
    
    # Find number of releases (to date)
    # listDownloads = DRIVER.find_elements(By.LINK_TEXT,"Release Notes")
    listDownloads = DRIVER.find_elements(By.LINK_TEXT,"Download")
    linksCount = len(listDownloads)
    print linksCount
    
    for item in listDownloads:
        # Get actual url links for each item found in above list
        merp = item.get_attribute("href")
        if "raw-file" in merp:
            print merp
            parse_raw_text(DRIVER)
            print ""
        else:
            print merp
            parse_web_page(DRIVER)
            print ""

    # Open & process each in order
    # listDownloads[0].click()  # Raw text file
    # listDownloads[1].click()    # Fancy web page sample
        
if __name__ == "__main__":
    main()