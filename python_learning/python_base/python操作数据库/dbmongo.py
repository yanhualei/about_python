from pymongo import MongoClient

conn = MongoClient(host="127.0.0.1",port=27017)
collection = conn['dytv']['dy_hpjy']  # 相当于[数据库名][表名]
collection.insert({"name":"oldeleven"})
result = collection.find_one()
print(result)