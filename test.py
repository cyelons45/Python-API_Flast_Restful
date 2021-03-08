import sqlite3

connection = sqlite3.connect('data.db')
print("Opened database successfully")
cursor = connection.cursor()
# create_table = "CREATE TABLE users (id INT PRIMARY KEY,username TEXT, password TEXT)"
# cursor.execute(create_table)

# INSERT QUERY
user = [
    (6, 'joseph', 'asdf'),
    (2, 'samuel', 'abcd'),
    (3, 'king', 'efgh'),
    (4, 'peter', 'ijkl')
]
# user = (1, 'jose', 'asdf')
insert_query = "INSERT INTO users VALUES (?,?,?)"
# cursor.execute(insert_query, user)

cursor.executemany(insert_query, user)

connection.commit()

# # SELECT QUERY
# select_query = "SELECT * FROM users"
# for row in cursor.execute(select_query):
#     print(row)
connection.close()
