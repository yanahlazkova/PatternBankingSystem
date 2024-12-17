from abc import ABC, abstractmethod
from faker import Faker

faker = Faker()

class AbstractAccount(ABC):
    account_type: str = None
    account_number: int = None
    balance: float = 0.0
    owner_id: str = None
    interest_rate: float = None

    @abstractmethod
    def set_account_type(self):
        pass

    def get_account_type(self):
        return self.account_type

    def set_account_number(self, account_number):
        self.account_number = account_number

    def set_owner(self, owner_id):
        self.owner_id = owner_id

    def get_owner(self):
        return self.owner_id

    def set_interest_rate(self, interest_rate):
        self.interest_rate = interest_rate

    @abstractmethod
    def set_balance(self, balance):
        pass

    @abstractmethod
    def deposit(self, amount):
        """ Метод внесення коштів на рахунок """
        pass

    @abstractmethod
    def withdraw(self, amount):
        """ Метод зняття коштів з рахунку """
        pass

    def __str__(self):
        return (f'Client ID: {self.owner_id}\n'
                f'Account: "{self.account_type}" - "{self.account_number}"\n'
                f'balance: {self.balance} $')


class SavingsAccount(AbstractAccount):
    def set_account_type(self):
        self.account_type = 'savings'

    def set_interest_rate(self, interest_rate):
        self.interest_rate = interest_rate

    def set_balance(self, balance):
        self.balance += self.balance
        return self.balance

    def deposit(self, amount):
        self.set_balance(amount)

    def withdraw(self, amount):
        self.balance -= amount if self.balance - amount else f'Не достатньо коштів на рахунку'


class DepositAccount(AbstractAccount):
    def set_account_type(self):
        self.account_type = 'deposit'

    def get_account_type(self):
        return self.account_type

    def set_balance(self, balance):
        return self.balance

    def deposit(self, amount):
        self.set_balance(amount)

    def withdraw(self, amount):
        self.balance -= amount if self.balance - amount else f'Не достатньо коштів на рахунку'


class CreditAccount(AbstractAccount):
    def set_account_type(self):
        self.account_type = 'credit'

    def get_account_type(self):
        return self.account_type

    def get_owner(self):
        return self.owner_id

    def set_balance(self, balance):
        return self.balance

    def deposit(self, amount):
        self.set_balance(amount)

    def withdraw(self, amount):
        self.balance -= amount if self.balance - amount else f'Не достатньо коштів на рахунку'


class AccountFactory:
    @staticmethod
    def create_account(account_type) -> AbstractAccount:
        if account_type == 'savings':
            account = SavingsAccount()
            account.set_account_type()
            account.set_account_number(faker.random_number(27))
        elif account_type == 'deposit':
            return DepositAccount()
        elif account_type == 'credit':
            return CreditAccount()
        else:
            raise ValueError("Un account type")

    @staticmethod
    def deposit(self, account: DepositAccount, amount: float):
        account.balance += amount
        print()
        return f'Your balance = {self.balance}'
