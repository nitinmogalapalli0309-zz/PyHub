# Where clause is used to get values which maches reqests
import sqlite3

Connection = sqlite3.connect("assets/Student_records.db")
print("Connection has been made successfuly!")
cursor = Connection.cursor()
query = """SELECT NAMES,MARKS FROM Student_Records WHERE MARKS>50 AND ID<2"""  # AND AND OR CAN BE USED

cursor.execute(query)
records = cursor.fetchall()

for x, y in records:
    print(x, y)

Connection.close()
input("Press Enter key to exit ")
