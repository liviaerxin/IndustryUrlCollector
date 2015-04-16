'''
@author: siyao
'''


from FinanceUrlCollector import *

targetUrl = "http://vip.stock.finance.sina.com.cn/mkt/#hangye_ZI11"
fileName = "financeLinks"

urlHandler = FinanceUrlCollector(targetUrl,fileName)
urlHandler.getUrls()
