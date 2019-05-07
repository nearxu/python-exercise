import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

# create db

mydb = myclient['rundb']

# create collect

mycol = mydb['sites']

# insert collect

mydict = { "name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com" }

x = mycol.insert_one(mydict)

print(x)

print(x.inserted_id)

# insert list
mylist = [
  { "name": "Taobao", "alexa": "100", "url": "https://www.taobao.com" },
  { "name": "QQ", "alexa": "101", "url": "https://www.qq.com" },
  { "name": "Facebook", "alexa": "10", "url": "https://www.facebook.com" },
  { "name": "知乎", "alexa": "103", "url": "https://www.zhihu.com" },
  { "name": "Github", "alexa": "109", "url": "https://www.github.com" }
]


x = mycol.insert_many(mylist)

print(x.inserted_ids)

# find all one

for y in mycol.find():
  print(y)

# find id ,$gt =>大于条件修饰符

myquery = {"alexa":{"$gt":"103"}}
mydoc = mycol.find(myquery).limit(3)

for z in mydoc:
  print(z)


# update_value

myupdate = {"alexa":"10000"}
newvalues = {"$set":{"alexa":"123456"}}

mycol.update_one(myupdate,newvalues)

# sort -1降序
mysort = mycol.find().sort("alexa",-1)

for x in mysort:
  print(x)

# delete_one