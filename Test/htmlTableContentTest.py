'''
@author: siyao
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

import time

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

driver = webdriver.Chrome(chromedriver)


driver.get("http://vip.stock.finance.sina.com.cn/mkt/#new_zhhy")

tbl_wrap_element = driver.find_element_by_id('tbl_wrap')
ActionChains(driver).drag_and_drop(tbl_wrap_element, tbl_wrap_element).perform()
time.sleep(1)

tbody = tbl_wrap_element.find_element_by_xpath("//div[@id='tbl_wrap']/table/tbody")
tbody_html = tbody.get_attribute("innerHTML")

soup = BeautifulSoup(tbody_html,from_encoding = "gb2312")
filteredContent = soup.findAll("tr", {"style":"display: none;"})
tbody_html = soup.renderContents()

print tbody_html

newSoup = BeautifulSoup(tbody_html,from_encoding = "gb2312") 
stock_urls = newSoup.findAll("th", {"class":"sort_down"})

for url in stock_urls:
    url = url.next
    print url.attrs['href']

driver.quit()
