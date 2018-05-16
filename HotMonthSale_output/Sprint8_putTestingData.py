import mysql.connector as mariadb
import pandas as pd
import csv
#from sqlalchemy import create_engine


mariadb_connection = mariadb.connect(user='toy9986619', \
									password='86471333',\
									database='mroongatest')

cursor = mariadb_connection.cursor()



#engine = create_engine("mysql://toy9986619:86471333@localhost/mroongatest")
#con = engine.connect()

'''
df = pd.read_csv('2018-05-14_itemHotMonthSaleChart.csv')
for row in df.iterrows():
    value = row[1].values
    try{
    	cursor.execute("INSERT INTO hotsale(id, item_id, category_name, 最大月銷量, 最小月銷量, 熱銷程度, update_time) VALUES('%d', '%d', '%s', '%d', '%d', '%s', '%s')" % tuple(value))
    }    
'''

df = pd.read_csv('2018-05-14_AllItemChart.csv')
for row in df.iterrows():
    value = row[1].values
    try:
    	cursor.execute("INSERT INTO item(item_id, shop_id, shop_name, category_name, name, price, sale, content, update_time) VALUES('%d', '%d', '%s', '%s', '%s', '%d', '%d', '%s', '%s')" % tuple(value))
    except:
    	print(value)

cursor.close()
mariadb_connection.commit()
mariadb_connection.close()