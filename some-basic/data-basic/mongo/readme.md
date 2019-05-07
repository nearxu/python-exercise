### mongo

start : 

mongod --dbpath d:mongodb/data

use:

mongo

### python use mongo

pip3 install pymongo



#### 查看、创建和删除数据库。

show dbs

use admin // add

db.dropDatabase() // delete

db.createCollection('person') // create collect person

show collections  // see all collect

db.person.drop() // delete collect

#### 文档的CRUD操作
// 向students集合插入文档
> db.students.insert({stuid: 1001, name: '骆昊', age: 38})
WriteResult({ "nInserted" : 1 })
> // 向students集合插入文档
> db.students.save({stuid: 1002, name: '王大锤', tel: '13012345678', gender: '男'})
WriteResult({ "nInserted" : 1 })
> // 查看所有文档
> db.students.find()


> // 查询stuid大于1001的文档只显示name和tel字段
> db.students.find({stuid: {'$gt': 1001}}, {_id: 0, name: 1, tel: 1}).pretty()
{ "name" : "王大锤", "tel" : "13012345678" }
{ "name" : "白元芳", "tel" : "13022223333" }
> // 查询name为“骆昊”或者tel为“13022223333”的文档
> db.students.find({'$or': [{name: '骆昊'}, {tel: '13022223333'}]}, {_id: 0, name: 1, tel: 1}).pretty()
{ "name" : "骆昊", "tel" : "13566778899" }
{ "name" : "白元芳", "tel" : "13022223333" }
> // 查询学生文档跳过第1条文档只查1条文档
> db.students.find().skip(1).limit(1).pretty()
{
        "_id" : ObjectId("5b13c790006ad854460ee70c"),
        "stuid" : 1002,
        "name" : "王大锤",
        "tel" : "13012345678",
        "gender" : "男"
}
> // 对查询结果进行排序(1表示升序，-1表示降序)
> db.students.find({}, {_id: 0, stuid: 1, name: 1}).sort({stuid: -1})
{ "stuid" : 1003, "name" : "白元芳" }
{ "stuid" : 1002, "name" : "王大锤" }
{ "stuid" : 1001, "name" : "骆昊" }
