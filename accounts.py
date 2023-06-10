import pyodbc
from dotenv  import load_dotenv
import os
from datetime import datetime
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

    @staticmethod
    def current_time():
        return datetime.now()

    def __init__(self, name: str, open_balance: float = 0.0):
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO accounts (account_name, account_balance) VALUES (?,?)", (name, open_balance))
            cursor.execute("SELECT @@IDENTITY AS ID")
            self.id = cursor.fetchone()[0]
            self.name = name
            self._balance = open_balance
            print(f"Account {name}, [id={self.id}] created with opening balance {round(open_balance, 2)}")

    def deposit(self, amount: float):
        if amount < 0:
            raise ValueError("Wrong amount to deposit")
            with connection.cursor() as cursor:

        cursor = connection.cursor()

        try:
                self._balance += amount
                cursor.execute("UPDATE accounts SET account_balance = ? WHERE account_id =?",
                               (self._balance, self.id))
                cursor.execute(("INSERT INTO transactions (account_id, transaction_time, amount) VALUES (?,?,?)"),
                               (self.id,Account.current_time(), amount))
                print(f"{amount} deposited to Account {self.name}")
        except Exception:
            cursor.rollback()
    def withdraw(self, amount: float):
        if amount < 0 or amount > self._balance:
            raise ValueError("Wrong amount to withdraw")
        cursor = connection.cursor()

        try:
                self._balance -= amount
                cursor.execute("UPDATE accounts SET account_balance = ? WHERE account_id =?",
                               (self._balance, self.id))
                cursor.execute(("INSERT INTO transactions (account_id, transaction_time, amount) VALUES (?,?,?)"),
                               (self.id, Account.current_time(), -amount))
                print(f"{amount} withraw from account {self.name}")
        except Exception:
            cursor.rollback()
        finally:
            cursor.cl
    def show_balance(self):
        print(f"Account {self.name} balance: {self._balance}")

def do_transaction(account_from: Account, account_to: Account, amount: float):



if __name__ == '__main__':
    account = Account('Piotr',100)
    account_two = Account('Maciej', 50)
    do_transaction(account_two, account, 51)

    connection.close()