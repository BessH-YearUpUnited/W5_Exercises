import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='RootB33r!',
    database = "db_from_python"
)

mycursor = db.cursor()
#mycursor.execute("CREATE DATABASE db_from_python")
#mycursor.execute("SHOW DATABASES")

# mycursor.execute("DROP TABLE customers")
# mycursor.execute('''CREATE TABLE customers (
#                  id INT AUTO_INCREMENT PRIMARY KEY
#                  , name VARCHAR(255)
#                  , address VARCHAR(255))'''
#                  )
# mycursor.execute("SHOW TABLES")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John Doe", "2467 28 1/2 St., Grand Junction, CO 81909")
mycursor.execute(sql, val)

db.commit()

print(mycursor.rowcount, "record inserted")
# for x in mycursor:
#     print(x)