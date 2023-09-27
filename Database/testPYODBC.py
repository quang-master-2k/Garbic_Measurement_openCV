import pyodbc
import pandas as pd
from sqlalchemy import create_engine
import time

start_time = time.time()
text_insert = ['AA', 'CC', 'DD', 5]
server = 'quangsog-Inspiron-5570'
database = 'HBI_app'
username = 'sa'
password = '123456Qa'
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
engine = create_engine(f'mssql+pyodbc:///?odbc_connect={connection_string}')

query = f"SELECT Dimension_Name, Dimension_Value FROM FirstMethod WHERE Garment_Style = '{text_insert[0]}' AND Pattern_Code = '{text_insert[1]}' AND Piece_Name = '{text_insert[2]}' AND Size = {text_insert[3]}"
df = pd.read_sql(query, engine)

df['Measurement_Value'] = [1,2,3,4,5,6,7,8]

print(df)

engine.dispose()  # Close the SQLAlchemy engine
end_time = time.time()

elapsed_time = end_time - start_time

print(f"Code execution time: {elapsed_time} seconds")