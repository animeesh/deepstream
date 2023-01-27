import mysql.connector as sql

db = sql.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="Hydrocabonlt",
    # auth_plugin='mysql_native_password'
)
if db.is_connected() == False:
    print("not connected")
if db.is_connected() == True:
    print(" connected")

curs = db.cursor()
try:
    curs.execute(f"CREATE TABLE sample_tab1 (id int AUTO_INCREMENT primary key, frame smallint UNSIGNED, People_count smallint UNSIGNED)")
except:
    print("Table exists...")

curs.execute(f"INSERT INTO sample_tab1 (frame, People_count) VALUES (%s, %s)",(31,3))
curs.execute(f"INSERT INTO sample_tab1 (frame, People_count) VALUES (%s, %s)",(91,23))
curs.execute(f"INSERT INTO sample_tab1 (frame, People_count) VALUES (%s, %s)",(3241,9))
curs.execute(f"INSERT INTO sample_tab1 (frame, People_count) VALUES (%s, %s)",(13,322))
curs.execute(f"INSERT INTO sample_tab1 (frame, People_count) VALUES (%s, %s)",(51,6))
curs.execute(f"INSERT INTO sample_tab1 (frame, People_count) VALUES (%s, %s)",(6,233))
curs.execute(f"INSERT INTO sample_tab1 (frame, People_count) VALUES (%s, %s)",(111,23))
curs.execute(f"INSERT INTO sample_tab1 (frame, People_count) VALUES (%s, %s)",(132,11))
curs.execute(f"INSERT INTO sample_tab1 (frame, People_count) VALUES (%s, %s)",(234,12))


if curs.execute("SELECT frame FROM sample_tab1 ORDER BY id DESC LIMIT 1") == (234,):
    print("done")

for x in curs:
    print((list(x))[0])

db.commit() 
