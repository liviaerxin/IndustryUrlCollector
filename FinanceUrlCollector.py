'''
@author: siyao
'''

from selenium import webdriver

import pymongo
import time
import codecs

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
mongodb_ip = "54.169.18.100"
class FinanceUrlCollector(object):
    
    
    
    def __init__(self, url, fileName):
        self.url = url
        self.fileName = fileName
        self.driver = webdriver.Chrome(chromedriver)
        
        
    def getUrls(self):
        self.driver.get(self.url)
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@id='treeContainer']/ul[1]/li[1]/a").click()

        time.sleep(1)
        
        links  = self.driver.find_element_by_xpath("//div[@id='treeContainer']/ul[1]/li[1]/div/dl").find_elements_by_tag_name("dd")
        
        
        conn = pymongo.Connection(mongodb_ip,27017)
        #database name test
        db = conn.test
        #collection name 
        db.industryCategory.drop()

        
        f = codecs.open(self.fileName, "w", "GB2312")
        id = 1
        for link in links:
            link.click()
            time.sleep(2)
            #industry name
            industryName = link.text
            url = self.driver.current_url
            print industryName
            print url
            #write to file
            f.write(industryName + ' ' + url + '\n')
            #write to db
            db.industryCategory.insert({'id':id,'name':industryName,'url':url})
            id = id + 1
        f.close()
        self.driver.quit()
