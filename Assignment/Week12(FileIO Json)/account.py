class BankAccount:
    def __init__(self, number: str, name: str, balance: int, db) -> None:
        """ Initialize """
        self.number = number
        self.name = name
        self.balance = balance
        self.db = db
        db.insert(self)

    def __repr__(self) -> str:
        """ represent account number name balance and database"""
        return f'Account(number="{self.number}", name="{self.name}"' \
               f', balance={self.balance}, db="{self.db.name}")'

    @property
    def number(self) -> None:
        """ get or set bank account number"""
        return self.__number

    @number.setter
    def number(self, other_number: str) -> None:
        # check whether other account number is string or not
        if not isinstance(other_number, str):
            raise TypeError('account number must be a string')
        # set number
        self.__number = other_number

    @property
    def name(self) -> None:
        """ get or set a account name"""
        return self.__name

    @name.setter
    def name(self, other_name: str) -> None:
        # check whether other account name is string or not
        if not isinstance(other_name, str):
            raise TypeError('name must be a string')
        # set name
        self.__name = other_name

    @property
    def balance(self) -> None:
        """ get or set balance account """
        return self.__balance

    @balance.setter
    def balance(self, new_balance: int) -> None:
        # check whether other balance is digit or not
        if not isinstance(new_balance, (int, float)):
            raise TypeError('balance must be a number')
        if new_balance < 0:  # check if balance positive or not
            raise ValueError('balance must be greater than zero')
        # set balance
        self.__balance = new_balance

    @property
    def db(self) -> None:
        """ get or set account database """
        return self.__db

    @db.setter
    def db(self, other_db) -> None:
        # set the database
        self.__db = other_db

    def deposit(self, amount: int) -> None:
        """ Deposit a money into account in exact amount"""
        self.db.record_transaction(self, amount)

    def withdraw(self, amount: int) -> None:  # redundant
        """ withdraw a money on a acount with an exact amount"""
        if self.balance < amount:  # check if valid amount
            print('Not enough money')
        else:
            self.db.record_transaction(self, -amount)

    def transfer(self, amount: int, to_account) -> None:
        """ transfer a self account into to_account"""
        if self.balance > amount:  # check valid amount
            self.withdraw(amount)
            to_account.deposit(amount)
        else:
            print('Not enough money')
