import mysql.connector as mariadb
import pandas as pd
import numpy as np

mariadb_connection = mariadb.connect(user='toy9986619', \
									password='86471333',\
									database='mroongatest')

cursor = mariadb_connection.cursor()

keyword = "+保護殼"

query = ("SELECT item.item_id, item.category_name, item.name, item.content, item.price, hotsale.最大月銷量, hotsale.熱銷程度, hotsale.update_time "
		 "FROM hotsale, item "
		 "WHERE hotsale.item_id = item.item_id "
		 "AND MATCH(item.name) AGAINST(%s IN BOOLEAN MODE)")

cursor.execute(query, (keyword, ))

#回傳資料
allData = cursor.fetchall()

#資料筆數
dataN = len(allData)
print("搜尋出 " +str(dataN)+" 筆資料" )

#分類投票
category=[]
categoryCount={}
for data in allData:
	if data[1] not in category:
		category.append(data[1])
		categoryCount[data[1]]=1
	else:
		categoryCount[data[1]]+=1


for x in category:
	print(x + " : " + str(categoryCount[x])+" 筆")

allData = sorted(allData, key=lambda x: x[5], reverse=True)

#熱銷區間
#dataHotsale = ['超級熱銷', '熱銷', '普通', '滯銷']
#dataHotsaleCount = {'超級熱銷':0, '熱銷':0, '普通':0, '滯銷':0}

'''
for tag in dataHotsale:
	Qdata = list(filter(lambda x: x[6]==tag, allData))
	QdataArray = np.array(Qdata)
	QMaxPrice = np.amax(QdataArray[:, 4], axis=0)
	QMinPrice = np.amin(QdataArray[:, 4], axis=0)
	print(tag + "價格帶: "+str(QMinPrice) + " ~ " + str(QMaxPrice))
'''




cursor.close()
mariadb_connection.close()