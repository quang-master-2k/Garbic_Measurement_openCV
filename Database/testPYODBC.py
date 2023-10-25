import pyodbc

text_insert = ['A', 'B', 'C']
server = 'quangsog-Inspiron-5570'
database = 'HBI_app'
username = 'sa'
password = '123456Qa'
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
conn = pyodbc.connect(connection_string)
sql_thickness = "SELECT Tolerance FROM ComparisonDatabase WHERE Garment_Style = ? AND Pattern_Code = ? AND Piece_Name = ?"
text_query_thickness = [text_insert[0], text_insert[1], text_insert[2]]
tolerance = conn.execute(sql_thickness, text_query_thickness).fetchone()
conn.commit()
conn.close()
print(tolerance[0])