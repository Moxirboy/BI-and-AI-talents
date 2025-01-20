from .database import Database
from .account import Account
class Bank(Database):
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        account_number = self._generate_account_number()
        account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = account
        self.save_to_file()
        print(f"Account created successfully! Account Number: {account_number}")

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(account)
        else:
            print("Account not found!")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            if amount > 0:
                account.balance += amount
                self.save_to_file()
                print(f"Deposit successful! New balance: {account.balance}")
            else:
                print("Invalid deposit amount!")
        else:
            print("Account not found!")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            if 0 < amount <= account.balance:
                account.balance -= amount
                self.save_to_file()
                print(f"Withdrawal successful! New balance: {account.balance}")
            else:
                print("Invalid withdrawal amount or insufficient balance!")
        else:
            print("Account not found!")
    def _generate_account_number(self):
        return str(len(self.accounts) + 1).zfill(6)