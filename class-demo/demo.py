import psycopg2
# establish connection
connection = psycopg2.connect('dbname=example user=postgres password=85037279af')
# sets a cursor to begin executing commands
cursor = connection.cursor()
cursor.execute('DROP TABLE IF EXISTS table2;')
cursor.execute('''
    CREATE TABLE table2 (
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT FALSE
    );
''')

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (1, True))

cursor.execute('INSERT INTO table2 (id, completed)' +  'VALUES (%(id)s, %(completed)s);', {
    'id': 2,
    'completed': False
})

cursor.execute('INSERT INTO table2 (id, completed)' +  'VALUES (%(id)s, %(completed)s);', {
    'id': 3,
    'completed': True
})


cursor.execute('SELECT * from table2;')
result = cursor.fetchall()
print('fetchall:', result)

cursor.execute('SELECT * from table2;')
result2 = cursor.fetchone()
print('fetchone:', result2)

cursor.execute('SELECT * from table2;')
result3 = cursor.fetchmany(2)
print('fetchmany',result3)

connection.commit() # commits the transaction
connection.close()
cursor.close()
