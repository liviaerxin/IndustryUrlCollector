'''
@author: siyao
'''

from IndustryUrlCollector import *

import pymongo
conn = pymongo.Connection("54.169.18.100",27017)
db = conn.test
IndustryItemList = db.industryCategory.find()

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)

for industryItem in IndustryItemList:
    urlHandler = IndustryUrlCollector(driver, industryItem)
    urlHandler.collectUrls()
    print industryItem

driver.quit()
