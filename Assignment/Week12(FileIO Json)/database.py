import json


class BankDB:
    def __init__(self, name: str) -> None:
        """ Initialize"""
        self.name = name

    def __repr__(self) -> str:
        """ represent a object """
        return f'BankDB(name="{self.name}")'

    def insert(self, bank_account) -> None:
        """ Create a accounts.json file if it doesnt exist else
        overwrite and save progress into json file(dump it into file)"""

        new_data = {
            bank_account.number: {
                'name': bank_account.name,
                'balance': bank_account.balance
            }
        }

        try:
            with open(f'{self.name}.json', 'r') as account:
                # load progress into dictionary
                account_data = json.load(account)

        except FileNotFoundError:
            # catching error if not have file
            # it will create new and wite into it
            with open(f'{self.name}.json', 'w') as account:
                json.dump(new_data, account, indent=4)

        else:
            account_data.update(new_data)  # update dictionary

            # overwrite file and dump it into account JSON file
            with open(f'{self.name}.json', 'w') as account:
                json.dump(account_data, account, indent=4)





    def search(self, account_number: str) -> None:
        """ search whether account number in database or not
        if it True show name and balance """
        try:
            with open(f'{self.name}.json', 'r') as account_file:
                # load data into dictionary
                account_data = json.load(account_file)

            name = account_data[account_number]['name']
            balance = account_data[account_number]['balance']
            # show the balance
            print(f'Name={name}, Balance={balance}')

        except FileNotFoundError as filename:
            print(f'No Data File name {filename} Found')

        except KeyError:  # if it not have those key
            # it will illustrate No account number
            print(f'No data for account number: {account_number}')

    def delete(self, account_number: str) -> None:
        """ delete account on database if it exist """
        try:
            with open(f'{self.name}.json', 'r') as account_file:
                # load data into dictionary
                account_data = json.load(account_file)

            # delete key of account data(bank number)
            del account_data[account_number]
            print(f'DELETE account {account_number}')

        except FileNotFoundError as filename:
            print(f'No Data File name {filename} Found')

        except KeyError:  # if it not have those key
            # it will illustrate No account number
            print(f'No data for account number: {account_number}')

        # update data into account.json (database)
        with open(f'{self.name}.json', 'w') as account_file:
            json.dump(account_data, account_file, indent=4)

    def record_transaction(self, account, amount: int) -> None:
        """ Update the account balance by amount then update JSON file"""

        account.balance += amount  # update the account balance
        self.insert(account)  # update the database balance
        print(f'UPDATE account {account.number} balance = {account.balance}')
