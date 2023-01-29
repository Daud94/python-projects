import psycopg2

connection = psycopg2.connect('dbname=example user=postgres password=85037279af')

cursor = connection.cursor()
cursor.execute('''
    CREATE TABLE table2 (
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT FALSE
    );
''')

cursor.execute('''
    INSERT INTO table2 (id, completed) VALUES (1,true);
''')

connection.commit()
connection.close()
cursor.close()