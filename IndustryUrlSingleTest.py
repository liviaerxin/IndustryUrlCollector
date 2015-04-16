'''
@author: siyao
'''


#http://vip.stock.finance.sina.com.cn/mkt/#new_jxhy
#http://vip.stock.finance.sina.com.cn/mkt/#new_ysjs
#http://vip.stock.finance.sina.com.cn/mkt/#new_qtxy

from IndustryUrlCollector import *

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)

targetUrl = "http://vip.stock.finance.sina.com.cn/mkt/#new_zhhy"
item = {u'url': u'http://vip.stock.finance.sina.com.cn/mkt/#new_zhhy', u'id': 1, u'name': u'\u751f\u7269\u5236\u836f'}

urlHandler = IndustryUrlCollector(driver,item)
print urlHandler.collectUrls()

driver.quit()
