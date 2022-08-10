# import pymysql

# conn = pymysql.connect(host="localhost", user='root', password="12345678",
# db="madang", charset="utf8")
# curs = conn.cursor(pymysql.cursors.DictCursor)
# publisher = '대한미디어'
# sql = "select * from book where publisher = " + publisher     
# curs.execute(sql)
# rows = curs.fetchall()
# for row in rows:
#     print(row)

# conn.close

# import pymysql

# conn = pymysql.connect(host="localhost", user='root', password="madang",
# db="madang", charset="utf8")
# curs = conn.cursor(pymysql.cursors.DictCursor)
# publisher = '대한미디어'
# sql = "select * from book where publisher = " + publisher
# curs.execute(sql)
# rows = curs.fetchall()
# for row in rows:
#     print(row)

# conn.close
import pymysql

conn = pymysql.connect(host="localhost", user="root", password="12345678", db="madang", charset="utf8")
curs = conn.cursor(pymysql.cursors.DictCursor)
publisher = "'대한미디어'"
sql = "select * from book where publisher = " + publisher
curs.execute(sql)
rows = curs.fetchall()
for row in rows:
    print(row['bookid'], row['bookname'], row['publisher'], row['price'])

curs.execute(sql)
rows = curs.fetchall()
for row in rows:
    print(row)
    print(row['bookid'], row['bookname'], row['publisher'], row['price'])

conn.close()
# '''bookid = "1"
# sql = "select * from book where bookid =" + bookid'''


# '''publisher = "'삼성당'"
# sql = "select * from book where publisher = " + publisher'''

# '''bookname = "축구"
# sql = "select * from book where bookname like concat('%', '축구', '%')"
# sql = "select * from book where bookname like '%축구%';"
# sql = "select * from book where bookname like '%" + bookname + "%'"'''