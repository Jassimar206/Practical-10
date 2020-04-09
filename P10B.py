import mysql.connector
mydbase = mysql.connector.connect(user='root', passwd='root',host='localhost', database="pract_10")
dbase = mydbase.cursor()
dbase.execute("select * from register")
print("Data Inserted : ")
r = dbase.fetchall()
for i in r:
    print(i)