from abc import ABC, abstractmethod


class AbstractAccount:
    def __init__(self):
        self.__account_type = None
        self.__account_number = None
        self.__balance = 0.0
        self.__owner = None
        self.__interest_rate = None

    @property
    def account_type(self):
        return self.__account_type

    @account_type.setter
    def account_type(self, account_type):
        self.__account_type = account_type

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, account_number):
        self.__account_number = account_number

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner):
        self.__owner = owner

    @property
    def interest_rate(self):
        return self.__interest_rate

    @interest_rate.setter
    def interest_rate(self, interest_rate):
        self.__interest_rate = interest_rate

    def set_account_type(self):
        pass

    def __str__(self):
        return (f'Client ID: {self.__owner}\n'
                f'Account: "{self.__account_type}" - "{self.__account_number}"\n'
                f'balance: {self.__balance} $')


class SavingsAccount(AbstractAccount):
    overdraft_limit: float

    def set_account_type(self):
        self.account_type = 'savings'

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError('Insufficient funds')

    def interest_accrual(self):
        interest = self.interest_rate * self.balance / 100
        self.balance += interest


class DepositAccount(AbstractAccount):
    fixed_period_time: int  # фіксований період часу в місяцях
    interest_penalty: int  # відсоток штрафу при знятті коштів

    def set_account_type(self):
        self.account_type = 'deposit'

    def set_fixed_period_time(self, period_time):
        self.fixed_period_time = period_time

    def set_interest_penalty(self, interest_penalty):
        self.interest_penalty = interest_penalty

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        penalty = self.penalty_accrual(amount)
        if self.balance + penalty >= amount:
            self.balance -= (amount + penalty)
            print(f'Нараховано штраф {penalty} $, Залишок на рахунку: {self.balance} $')

        else:
            raise ValueError(f'Недостатньо грошей на рахунку. Штраф: {penalty} $'
                             f'Баланс: {self.balance} $')

    def penalty_accrual(self, amount):
        """ нарахування штрафу"""
        penalty = amount * self.interest_penalty / 100
        return penalty


class AccountBuilder(ABC):
    def __init__(self):
        self._account = None

    @abstractmethod
    def create_account(self):
        pass

    @abstractmethod
    def set_account_type(self):
        pass

    @abstractmethod
    def add_account_number(self, account_number):
        pass

    @abstractmethod
    def add_owner(self, owner):
        pass

    @abstractmethod
    def set_initial_balance(self, balance):
        pass

    @abstractmethod
    def set_interest_rate(self, interest_rate):
        pass

    def build(self):
        return self._account


class SavingsAccountBuilder(AccountBuilder):
    def create_account(self):
        self._account = SavingsAccount()

    def set_account_type(self):
        self._account.set_account_type()

    def add_account_number(self, account_number):
        self._account.account_number = account_number

    def add_owner(self, owner):
        self._account.owner = owner

    def set_initial_balance(self, balance):
        self._account.balance = balance

    def set_interest_rate(self, interest_rate):
        self._account.interest_rate = interest_rate


class DepositAccountBuilder(AccountBuilder):
    def create_account(self):
        self._account = DepositAccount()

    def set_account_type(self):
        self._account.set_account_type()

    def add_account_number(self, account_number):
        self._account.account_number = account_number

    def add_owner(self, owner):
        self._account.owner = owner

    def set_initial_balance(self, balance):
        self._account.balance = balance

    def set_interest_rate(self, interest_rate):
        self._account.interest_rate = interest_rate

    def fixed_period_time(self, period_time):
        self._account.set_fixed_period_time(period_time)

    def set_interest_penalty(self, interest_penalty):
        self._account.set_interest_penalty(interest_penalty)


class AccountFactory:
    @staticmethod
    def construct_account(account_type, account_data) -> AbstractAccount:
        if account_type == 'savings':
            owner, account_number, balance, interest_rate = account_data
            account_builder = SavingsAccountBuilder()
            account_builder.create_account()
            account_builder.set_account_type()
            account_builder.add_account_number(account_number)
            account_builder.add_owner(owner)
            account_builder.set_initial_balance(balance)
            new_account = account_builder.build()
            return new_account
        elif account_type == 'deposit':
            owner, account_number, balance, interest_rate, period_time, interest_penalty = account_data
            account_builder = DepositAccountBuilder()
            account_builder.create_account()
            account_builder.add_account_number(account_number)
            account_builder.add_owner(owner)
            account_builder.set_initial_balance(balance)
            account_builder.set_interest_rate(interest_rate)
            account_builder.fixed_period_time(period_time)
            account_builder.set_interest_penalty(interest_penalty)
            new_account = account_builder.build()
            return new_account


from faker import Faker

fake = Faker()

new_data_savings_account = ('Alex', fake.random_number(27), 1000, 5)
new_account = AccountFactory().construct_account('savings', new_data_savings_account)

print(new_account)

new_data_deposit_account = ('Peter', fake.random_number(27), 5000, 10, 12, 0.1)
deposit_account = AccountFactory().construct_account('deposit', new_data_deposit_account)
print(deposit_account)
