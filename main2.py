import pyodbc
from dotenv  import load_dotenv
import os

load_dotenv()

database_password = os.environ.get('DATABASE_PASSWORD')
database_server = 'morfeusz.wszib.edu.pl'
database_name = 'pikoloda'
database_user = 'pikoloda'
driver = '{ODBC Driver 18 for SQL Server}'

connection_string = f'Driver={driver};' \
                    f'SERVER={database_server};' \
                    f'DATABASE={database_name};' \
                    f'UID={database_user};' \
                    f'PWD={database_password};' \
                    'Encrypt=no;'

connection = pyodbc.connect(connection_string)

cursor = connection.cursor()


cursor.execute("INSERT INTO  users (name, age)  VALUES('Piotr', 35)")
cursor.execute("INSERT INTO  users (name, age)  VALUES('Krzysztof', 44)")

cursor.commit()

cursor.execute("INSERT INTO  users (name, age)  VALUES('Jan', 44)")

for row in cursor.execute("SELECT * FROM users"):
    print(row)



cursor.close()
connection.close()









