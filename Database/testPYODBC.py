import pyodbc

server = 'quangsog-Inspiron-5570'
database = 'HBI_app'
username = 'sa'
password = '123456Qa'
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
conn = pyodbc.connect(connection_string)

cursor = conn.cursor()
cursor.execute("SELECT * FROM FirstMethod")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()