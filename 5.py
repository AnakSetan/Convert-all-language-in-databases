# import mysql.connector
# import json
# import csv
# # import requests
# #mysql ke CSV======================================
# dbku = mysql.connector.connect(
#     host = 'localhost',
#     port = 3306,
#     user = 'root',
#     passwd= 'akulasubmarine10',
#     database = 'doraemon'
# )
# kursor = dbku.cursor()
# querydb = 'select*from huhu'
# kursor.execute(querydb)

# row = kursor.fetchall()
# head = ['id','nama','usia']
# with open ('anggota.csv','w',newline ='') as x :
#     writer = csv.writer(x)
#     writer.writerow(head)
#     writer.writerows(row)


#==========mysql ke json=============
# newData =[]
# for item in range(len(row)):
#     newData.append({'id':row[item][0],'nama':row[item][1],'usia':row[item][2]})

# with open ('mysql.json','w') as x :
#     json.dump(newData,x) 


#CSV ke Mysql
#===================================
# data = []
# with open ('anggota.csv','r',newline='') as x :
#     reader = csv.reader(x)
#     for i in reader :
#         data.append(i)
# print(data[:10])
# kursor.execute('''create table keluarga(
#     id int not null auto_increment,
#     nama varchar(30),
#     usia smallint,
#     primary key(id)
#     )'''
# )
# querydb = '''insert into keluarga (id,nama,usia) values (%s,%s,%s)'''
# kursor.executemany(querydb,data[:10])
# dbku.commit()


#json to mysql
#=====================================================
# import json
# import mysql.connector

# dbku = mysql.connector.connect(
#     host = 'localhost',
#     port = 3306,
#     user = 'root',
#     passwd= 'akulasubmarine10',
#     database = 'doraemon'
# )
# kursor = dbku.cursor()
# kursor.execute ('''create database kartun''')
# kursor.execute ('''use kartun''')
# querydb = '''create table table_1(
#     id int not null auto_increment,
#     nama varchar (30),
#     usia smallint,
#     primary key (id)
# )'''
# kursor.execute(querydb)

# with open ('mysql.json','r') as x :
#     reader = json.load(x)
# print(reader)

# datajson = []
# for i in range (0,len(reader)):
#     data = []
#     for k in reader[i].keys():
#         data.append(reader[i][k])
#     datajson.append(tuple(data))
# print(datajson)

# querydb = '''insert into table_1 (id,nama,usia) values (%s,%s,%s)'''
# kursor.executemany(querydb, datajson)
# dbku.commit()


#mongo to json
#=====================================================
# import pymongo
# import json

# #get all data
# connect = pymongo.MongoClient('mongodb://localhost:27017')
# db = connect['marvel']
# col = db['avengers']

# list_1 = list(col.find())
# for i in range (0,len(list_1)):
#     list_1[i].pop('_id')
# with open ('superhero.json','w') as x :
#     json.dump(list_1,x)


#mongo to csv
#=====================================================
# import csv
# import pymongo

# connect = pymongo.MongoClient('mongodb://localhost:27017')
# db = connect['marvel_2']
# col = db['avengers']

# list_1 = list(col.find())

# for i in range(0,len(list_1)):
#     list_1[i].pop('_id')
# #Write CSv============
# with open ('avengerbaru.csv','w',newline='') as x :
#     kolom = list(list_1[1].keys())
#     tulis=csv.DictWriter(x,fieldnames=kolom)
#     tulis.writeheader()
#     tulis.writerows(list_1)


#mongo to mysql
#=====================================================
# import mysql.connector
# import pymongo

# dbku = mysql.connector.connect(
#     host = 'localhost',
#     port = 3306,
#     user = 'root',
#     passwd= 'akulasubmarine10',
#     database = 'doraemon'
# )

# connect = pymongo.MongoClient('mongodb://localhost:27017')
# db = connect['marvel']
# col = db ['avengers']

# kursor =dbku.cursor()
# kursor.execute ('''create database db_superhero''')
# kursor.execute ('''use db_superhero''')
# kursor.execute('''create table superhero(
#     id int not null auto_increment,
#     title varchar(30),
#     usia smallint,
#     primary key(id)
#     )'''
# )
# kursor.executemany(querydb)
# list_1 = list(col.find())

# for j in range (0,len(list_1)):
#     list_1[j].pop('_id')

# datamysql_baru = []
# for j in range (0,len(list_1)):
#     data = []
#     for key in list_1[j].keys():
#         data.append(list_1[j][key])
#     datamysql_baru.append(tuple(data))
# print(datamysql_baru)
# querydb = '''insert into superhero (title,usia) values (%s,%s)'''
# kursor.executemany(querydb, datamysql_baru)
# dbku.commit()


#mysql to mongo
#=====================================================
# import mysql.connector
# import pymongo

# dbku = mysql.connector.connect(
#     host = 'localhost',
#     port = 3306,
#     user = 'root',
#     passwd= 'akulasubmarine10',
#     # database = 'doraemon'
# )
# connect = pymongo.MongoClient('mongodb://localhost:27017')
# db = connect['marvel_2']
# col = db ['avengers']

# kursor = dbku.cursor()
# data_input = []
# kolom = []

# query_db = '''use doraemon'''
# kursor.execute(query_db)
# query_idx = '''describe keluarga'''
# kursor.execute(query_idx)
# key = kursor.fetchall()

# for i in range(0,len(key)):
#     kolom.append(key[i][0])
# querydb_val = '''select * from keluarga'''
# kursor.execute(querydb_val)
# val=kursor.fetchall()
# for i in range(0,len(val)):
#     data = {}
#     for j in range(0,len(kolom)):
#         data.update({kolom[j]:val[i][j]})
#     data_input.append(data)
# print(data_input)
# for item in data_input :
#     add = col.insert_one(item)


#csv to mongo
#=====================================================
# x= pymongo.MongoClient('mongodb://localhost:27017')
# db = x['kartundoraemon']
# col = db['anggota.csv']
# listkosong=[]
# with open ('anggota.csv','r') as x :
#     reader = csv.DictReader(x)
#     for i in reader :
#         listkosong.append(dict(i))
#         print(listkosong)
# for item in listkosong :
#     add = col.insert_one(item)


#json to mongo
#======================================================
# import json
# import pymongo

# connect = pymongo.MongoClient('mongodb://localhost:27017')
# db = connect['marvel_1']
# col = db['avengers']
# data = []

# with open ('superhero.json','r') as x :
#     data =json.load(x)
# print(data) 

# for i in data :
#     add = col.insert_one(i)