import Database.DAO

myDao = Database.DAO.DAO("test.db")
myDao.format_database()
debug = myDao.get_debug()
for i, message in enumerate(debug):
    print(str(i)+':',end=' ')
    print(message)
res = myDao.query_ingredients()
print(res)
