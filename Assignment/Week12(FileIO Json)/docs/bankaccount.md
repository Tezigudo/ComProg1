# Module `account.py` and `database.py`


There is no definite rule on how you should implement your objects.  However, at
least the following are required:

* `account.py` module is not allowed to use for writing a JSON file. 
* `database.py` module is the only one that you can use for writing a JSON file.
* Please use `accounts.json` as a file name for storing the data.</u>

The module `account.py` defines the `BankAccount` class.  Each `ฺBankAccount` object consists of
the `number`, `name`, `balance` and `db` properties.  The `balance` property must be a positive numbers, where the `name` 
and `number` are `String`. The `db` property must be a `BankDB` object.

    >>> from account import BankAccount

    >>> type(BankAccount.number)
    <class 'property'>
    >>> type(BankAccount.name)
    <class 'property'>
    >>> type(BankAccount.balance)
    <class 'property'>
    >>> type(BankAccount.db)
    <class 'property'>


Initialization
==============

 A`BankDB` object must be initialized with a name of database.

    >>> from database import BankDB

    >>> db = BankDB("accounts")
    >>> db
    BankDB(name="accounts")

A `BankAccount` object must be initialized with an account number, a name, a balance and `BankDB` object.

Once the `BankAccount` object has been created, it executes the `insert` method from `BankDB` object automatically to create `accounts.json` file, 
and put the data below into the file.

    new_data = {
            bank_account.number: {
                "name": bank_account.name,
                "balance": bank_account.balance,
            }
        }

The examples of initialization are shown below.

    >>> import json

    >>> p1 = BankAccount("333-333", "Torres", 5000, db)
    >>> p1
    Account(number="333-333", name="Torres", balance=5000, db="accounts")

    >>> p2 = BankAccount("555-555", "Alex", 8000, db)
    >>> p2
    Account(number="555-555", name="Alex", balance=8000, db="accounts")

    >>> with open("accounts.json", "r") as data_file:
    ...     data = json.load(data_file)
    ... 
    >>> data["333-333"]
    {'name': 'Torres', 'balance': 5000}
    >>> data["555-555"]
    {'name': 'Alex', 'balance': 8000}

    >>> p3 = BankAccount("666-666", "Bob", "4000", db)
    Traceback (most recent call last):
    ...
    TypeError: balance must be a number

    >>> p4 = BankAccount(888888, "Jota", 4000, db)
    Traceback (most recent call last):
    ...
    TypeError: account number must be a string

    >>> p5 = BankAccount("999-999", "Mane", -500, db)
    Traceback (most recent call last):
    ...
    ValueError: balance must be greater than zero


Using methods
===================

###`BankAccount` class consists of the `deposit`, `withdraw` and `transfer` methods.


####`deposit` method: 

    >>> p1.deposit(200)
    UPDATE account 333-333 balance = 5200

    >>> with open("accounts.json", "r") as data_file:
    ...     data = json.load(data_file)
    ...
    >>> data['333-333']['balance']
    5200

    >>> p1
    Account(number="333-333", name="Torres", balance=5200, db="accounts")

####`withdraw` method:

    >>> p2.withdraw(5000)
    UPDATE account 555-555 balance = 3000

    >>> with open("accounts.json", "r") as data_file:
    ...     data = json.load(data_file)
    ...
    >>> data['555-555']['balance']
    3000

    >>> p2
    Account(number="555-555", name="Alex", balance=3000, db="accounts")

    >>> p2.withdraw(4000)
    Not enough money

####`transfer` method:

    >>> p2.transfer(2000,p1)
    UPDATE account 555-555 balance = 1000
    UPDATE account 333-333 balance = 7200

    >>> with open("accounts.json", "r") as data_file:
    ...     data = json.load(data_file)
    ...
    >>> data['333-333']
    {'name': 'Torres', 'balance': 7200}
    >>> data['555-555']
    {'name': 'Alex', 'balance': 1000}

    >>> p2.transfer(3000,p1)
    Not enough money
    >>> p2
    Account(number="555-555", name="Alex", balance=1000, db="accounts")

###`BankDB` class consists of the `insert`, `search` and `delete` methods.
We have mentioned about `insert` method earlier. Let's see more details of `search` and `delete` methods.

    >>> db.search("333-333")
    Name=Torres, Balance=7200
    >>> db.search("777-777")
    No data for account number: 777-777

    >>> db.delete("777-777")
    No data for account number: 777-777
    >>> db.delete("333-333")
    DELETE account 333-333
    >>> with open("accounts.json", "r") as data_file:
    ...     data = json.load(data_file)
    ...
    >>> data['333-333']
    Traceback (most recent call last):
    ...
    KeyError: '333-333'

