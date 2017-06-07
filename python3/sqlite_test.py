import sqlite3

connect = sqlite3.connect('test.sqlite')

cursor = connect.cursor()
cursor.execute('SELECT * FROM main.foo;')

connect.commit()
