import pymysql as sql
db = sql.connect(host="localhost",port=3306,user="root",password="pwd",database="banking")
c = db.cursor()
