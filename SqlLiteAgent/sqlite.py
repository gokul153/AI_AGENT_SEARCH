import sqlite3

## connect to the SQLite database
connection = sqlite3.connect('student.db')

## create a cursor object using the connection insert record ,create table
cursor = connection.cursor()

## create a table
table_info = """
CREATE TABLE IF NOT EXISTS students (Name Varchar(50),class Varchar(50), roll_no Integer, marks Integer)"""
cursor.execute(table_info)

## insert some more records
cursor.execute("INSERT INTO students VALUES ('John Doe', '10th', 1, 85)")
cursor.execute("INSERT INTO students VALUES ('Jane Smith', 'AI', 2, 90)")   
cursor.execute("INSERT INTO students VALUES ('Alice Brown', 'AI', 3, 95)")
cursor.execute("INSERT INTO students VALUES ('Bob White', 'AI', 4, 80)")

## display the records
print("Records in the students table:")
data = cursor.execute("SELECT * FROM students")
for row in data:
    print(row)
## commit the changes
connection.commit()
connection.close()