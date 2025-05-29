import pymysql  
# 连接数据库并创建spider数据库
db = pymysql.connect(host='localhost',user='root', password='123456', port=3306, database='spiders')  
cursor = db.cursor()  
# cursor.execute('SELECT VERSION()')  
# data = cursor.fetchone()  
# print('Database version:', data)  
# cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")  
# db.close()
# 创建学生表
# cursor = db.cursor()
# sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
# cursor.execute(sql)
# db.close()
# 插入数据
# db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
# cursor = db.cursor()
# data = {
#     'id': '20120001',
#     'name': 'Bob',
#     'age': 20
# }
# table = 'students'
# keys = ', '.join(data.keys())
# values = ', '.join(['% s'] * len(data))
# sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
# try:
#    if cursor.execute(sql, tuple(data.values())):
#        print('Successful')
#        db.commit()
# except:
#     print('Failed')
#     db.rollback()
# db.close()
# 更新数据
# sql = 'UPDATE students SET age = % s WHERE name = % s'
# try:
#    cursor.execute(sql, (25, 'Bob'))
#    db.commit()
# except:
#    db.rollback()
# db.close()
# 删除数据
# table = 'students'
# condition = 'age > 20'

# sql = 'DELETE FROM  {table} WHERE {condition}'.format(table=table, condition=condition)
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()

# db.close()
# 查询数据
sql = 'SELECT * FROM students WHERE age >= 20'

try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    one = cursor.fetchone()
    print('One:', one)
    results = cursor.fetchall()
    print('Results:', results)
    print('Results Type:', type(results))
    for row in results:
        print(row)
except:
    print('Error')