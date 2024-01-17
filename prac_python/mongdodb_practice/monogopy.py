from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.jungle

# 데이터 추가
def insert_user(name, age):
    db.users.insert_one(
       {
            "name": name,
            "age": age,
        }
    )


# insert_user('bobby',21)
# insert_user('kay',27)
# insert_user('john',30)

# 모든 사용자 조회
# all_users = list(db.users.find({}))

# for user in all_users:
#     print(user)

# 특정 조건을 만족하는 사용자 조회
# same_ages = list(db.users.find({'age':21}))

#  특정 결과값을 뽑아보기
# user = db.users.find_one({'name':'bobby'})


# 특정 결과값에서 특정한 키를 제외하고 뽑아보기
# user = db.users.find_one({'name':'bobby'},{'_id':False})

# 특정 값을 기준으로 데이터 업데이트 하기
# db.users.update_one({'name':'bobby'},{'$set':{'age':19}})
# user = db.users.find_one({'name':'bobby'},{'_id':False})

# 특정 값을 삭제하기
# db.users.delete_many({'name':'bobby'})
# users = list(db.users.find({},{'_id':False}))

# for user in users:
#     # user = db.users.find_one({},{'_id':False})
#     print(user)

# db.users.delete_many({})


# 파이몽고 연습
# 1. 자료 저장하기
# doc = {
#     'name':'kim',
#     'age':31
#     }
# db.users.insert_one(doc)

# 2. 한개 찾기
# print(db.users.find_one({'name':'kim'}))

# 여러개 찾기
# db.users.update_one({'name':'kim'},{'$set':{'age':31}})
# users = list(db.users.find({},{'_id':False}))
# print(users)

# 수정하기
# db.users.update_one({'name':'kim'},{'$set':{'age':25}})
# users = list(db.users.find({},{'_id':False}))
# print(users)

# 지우기
# db.users.delete_one({'name':'john'})
# users = list(db.users.find({},{'_id':False}))
# print(users)
