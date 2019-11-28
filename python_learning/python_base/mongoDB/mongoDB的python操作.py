from pymongo import MongoClient

conn = MongoClient(host="127.0.0.1",port=27017)
collection = conn['dytv']['dy_hpjy']  # 相当于[数据库名][表名]
result = collection.insert({"name":"oldeleven"})
print(result)