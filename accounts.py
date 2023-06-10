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


class Account:

    def __init__(self, name: str, open_balance: float = 0.0):
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO accounts (account_name, account_balance) VALUES (?,?)", (name, open_balance))
            cursor.execute("SELECT @@IDENTITY AS ID")
            self.id = cursor.fetchone()[0]
            self.name = name
            self._balance = open_balance
            print(f"Account {name}, [id={self.id}] created with opening balance {round(open_balance, 2)}")

    def deposit(self, amount: float):
        if amount > 0:

            with connection.cursor() as cursor:
                self._balance += amount
                cursor.execute("UPDATE accounts SET account_balance = ? WHERE account_id =?",
                               (self._balance, self.id))
                print(f"{amount} deposited to Account {self.name}")

    def withdraw(self, amount: float):
        if 0 < amount <= self._balance:
            with connection.cursor() as cursor:
                self._balance -= amount
                cursor.execute("UPDATE accounts SET account_balance = ? WHERE account_id =?",
                               (self._balance, self.id))
                print(f"{amount} withraw from account {self.name}")

    def show_balance(self):
        print(f"Account {self.name} balance: {self._balance}")


if __name__ == '__main__':
    account = Account('Piotr')
    account.deposit(10)
    account.deposit(0.1)
    account.deposit(0.3)
    account.deposit(7.2)
    account.show_balance()