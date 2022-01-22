# Bank Account

In this assignment, you are to implement a bank account, as shown.

## Modules

Your application consists of two modules, that must be completed by
you. Please look at `bankaccount.md` [documentation](docs/bankaccount.md) 
for more details, including test cases that will be used to grade this module.



### 1. Module `account.py` 


This module contains the `BankAccount` class for creating each user account.


    class BankAccount:
        def __init__(self, number, name, balance, db):
            self.number = number
            self.name = name
            self.balance = balance
            self.db = db
            db.insert(self)


        # add your implementation


        def deposit(self, amount):
            # add your implementation


        def withdraw(self, amount):
            # add your implementation


        def transfer(self, amount, to_account):
            # add your implementation


        def __repr__(self):
            # add your implementation

The provided `account.py` contains only some template code that you must
complete yourself. 

### 2. Module `database.py`

This module contains the `BankDB` class for creating a database file.

    class BankDB:
        def __init__(self, name):
            self.name = name


        def insert(self, bank_account):
            # add your implementation


        def search(self, account_number):
            # add your implementation


        def delete(self, account_number):
            # add your implementation


        def record_transaction(self, account, amount):
            # add your implementation


        def __repr__(self):
            # add your implementation

The provided `database.py` contains only some template code that you must
complete yourself.


## Running Tests

Tests can be performed by running the `main.py`.  They use the `doctest` to run all
examples found inside all the documentation files in the `docs` directory.

    python main.py

## Your Task

1. Complete the implementations of the `account.py` and `database.py`
   modules.  Make sure they all pass the tests.
2. Run `main.py` to see the result and inspect the correctness.
3. Modify the `summary.txt` file.  In this summary, tell us what you have
   completed and what you have not.

**Notes:** Please do not change any file inside the `docs` directory.  These
files will be used to run tests against your submitted code.


## Submission

1. Check that everything is working as expected, i.e., all the tests are
   passed.
2. Commit your code with all related files
    * `account.py`
    * `database.py`
    * `summary.txt`
3. Push the commit to GitHub
4. Wait for GitHub Classroom to mail back your grading result.

## Grading Criteria

1. **Correctness (70%):** Your program must pass all the doctests.
3. **Cleanliness (30%):** Your program must follow the PEP8 convention.  Variable
   names are meaningful.  Docstrings are written for all methods and
   functions.  Comments are added at certain points for others to understand
   your code easily.
   
