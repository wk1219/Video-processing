import pymysql

conn = pymysql.connect(host='localhost', user='root', password='mt4714573',
                       db='web', charset='utf8')
curs = conn.cursor()
num = "3"
name = "'test.mp4'"
size = "150"
length = "'20s'"
mtime = "2020-03-21"
res = "'640X480'"

sql = "select * from video"
insert_sql = 'INSERT INTO web.video (norm_num, norm_name, norm_size, norm_length, norm_mtime,norm_resolution) VALUES (%s, %s, %s, %s %s, %s)'
val = (num, name, size, length, mtime, res)
#insert_sql = 'INSERT INTO web.video (norm_num, norm_name, norm_size, norm_length, norm_mtime, norm_resolution) VALUES (2, \'test.mp4\', 150, \'20s\', 2020-03-20, \'640X480\')'
#curs.execute(insert_sql, val)
#conn.commit()
curs.execute(sql)
rows = curs.fetchall()
print(rows)

conn.close()
