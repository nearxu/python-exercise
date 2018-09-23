import pymongo

client = pymongo.MongoClient(host='localhost', port=20717)
db = client.test_mongo_py
print('数据库链街成功')
collection = db.students

student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

result = collection.insert(student)

print(result)
