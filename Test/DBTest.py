'''
@author: siyao
'''


import pymongo

conn = pymongo.Connection("127.0.0.1",27017)

db = conn.IndustryNameList

content = db.user.find()

for i in content:
    print i['url']
    print i['name']
