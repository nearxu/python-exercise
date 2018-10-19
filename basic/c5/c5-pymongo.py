from pymongo import MongoClient

try:
    client = MongoClient(host='localhost', port=27017)
    db = client.student
    collection = db.Student
    print('mongo data connect')
    datas = collection.find()[:3]
    for data in datas:
        print(data, 'data')
except Exception as e:
    print(e)
