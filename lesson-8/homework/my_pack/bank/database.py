import os
import json
from .account import Account
class Database:
    def save_to_file(self):
        with open("accounts.txt", "w") as file:
            accounts_data = {acc_num: {"name": acc.name, "balance": acc.balance} for acc_num, acc in self.accounts.items()}
            json.dump(accounts_data, file)

    def load_from_file(self):
        if os.path.exists("accounts.txt"):
            with open("accounts.txt", "r") as file:
                accounts_data = json.load(file)
                for acc_num, acc_info in accounts_data.items():
                    self.accounts[acc_num] = Account(acc_num, acc_info["name"], acc_info["balance"])

    def _generate_account_number(self):
        return str(len(self.accounts) + 1).zfill(6)
