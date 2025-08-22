import sqlite3


connection = sqlite3.connect('passwords.db')
print("The connection to the database was successfully established.")
cursor = connection.cursor()

sql_command = """CREATE TABLE IF NOT EXISTS entries (
    id INTEGER PRIMARY KEY,
    website TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
); """

cursor.execute(sql_command)
print("The 'entries' table has been created or already exists.")

connection.commit()
connection.close()
print("Conexiunea a fost inchisa.")
