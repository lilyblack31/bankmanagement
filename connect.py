import pymysql as sql
db = sql.connect(host="localhost",port=3306,user="root",password="candus76",database="banking")
c = db.cursor()
