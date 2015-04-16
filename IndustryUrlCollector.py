'''
@author: siyao
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

import time
import logging


class IndustryUrlCollector:

    
    def __init__(self, driver, industryItem):
        self.driver = driver
        self.industryItem = industryItem
        self.driver.get(self.industryItem['url'])
        logging.warning('[CSST-IndustryUrlCollector-Url] : '+self.industryItem['url'])
    
    def collectUrls(self):
        self.totalUrls = self.getUrls()
        self.hasNextPage()
        self.writeToFile()
        
    def getUrls(self):
        #find element need to parse
        tbl_wrap_element = self.driver.find_element_by_id('tbl_wrap')
        #move mouse on this element to generate html
#       ActionChains(self.driver).drag_and_drop(tbl_wrap_element, tbl_wrap_element).perform()
        time.sleep(1)
        
        #get table body for all stock
        tbody = tbl_wrap_element.find_element_by_xpath("//div[@id='tbl_wrap']/table/tbody")
        tbody_html = tbody.get_attribute("innerHTML")
        soup = BeautifulSoup(tbody_html,from_encoding = "gb2312")
        #print tbody_html
        #parse element
        stocklist = soup.findAll("th", {"class":"sort_down"})
        #print stocklist
        stock_code = []
        for stock in stocklist:
            if stock.find('a'):
                stock_code.append(stock.find('a').text)
        print stock_code
        return stock_code
    
    def hasNextPage(self):
        nextPage = self.driver.find_element_by_id('list_page_btn_2')
        
        nextLinks = nextPage.find_elements_by_tag_name('a')
        #if there's a next page
        if(nextLinks):
            print "next page"
            self.driver.find_element_by_xpath("//div[@id='list_page_btn_2']/a").click()
            #using plus here, because append will add the entire list as one element
            self.totalUrls = self.totalUrls + self.getUrls()
            #recursive called
            self.hasNextPage()
        else:
            return None
    
    def writeToFile(self):
        filename = self.industryItem['name']
        fileName = "urls/"+filename
        file = open(fileName, 'wb')
        '''
        !!! Using set to get rid of repeated value, 
        because at the last page, some element from previous page still exist.
        But the style is display:none, so some repeated value will be get from last page parsing  
        '''
        finalList = list(set(self.totalUrls))
        finalList.sort(key = self.totalUrls.index)
        #write urls to file
        if(finalList):
            for stock in finalList:
                #url = url.next
                #stock code
                file.write(stock + '\n')
#               self.writeUrl(file, url)
        file.close()
    #deprecated    
    def writeStockCode(self, fileHandler, url):
        stockCode = url.text
        if(stockCode):
            print stockCode
            fileHandler.write(stockCode+'\n')
        
    #deprecated
    def writeUrl(self, fileHandler, url):
        #html element might doesn't have a href. eg: style="display: none;
        if(len(url.attrs) > 0):
            link = url.attrs['href']
            print link
            fileHandler.write(link+'\n')
        
        
