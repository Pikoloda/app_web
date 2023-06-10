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

cursor =connection.cursor()

# cursor.execute("CREATE TABLE users (id int identity, name varchar(100), age int)")
cursor.execute("INSERT INTO  users (name, age)  VALUES('Piotr', 35)")
cursor.execute("INSERT INTO  users (name, age)  VALUES('Krzysztof', 44)")


# cursor = connection.cursor()

# cursor.execute("SELECT * FROM users")
# result = cursor.fetchall()
# result = cursor.fetchone()
# result = cursor.fetchmany(5)

for row in cursor.execute("SELECT * FROM users"):
    print(row)

# while result:
#     print(result)
#     result = cursor.fetchone()


cursor.close()
connection.close()









