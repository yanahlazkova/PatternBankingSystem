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

    def set_account_type(self, account_type):
        pass

    def __str__(self):
        return (f'Client ID: {self.__owner}\n'
                f'Account: "{self.__account_type}" - "{self.__account_number}"\n'
                f'balance: {self.__balance} $')


class AccountBuilder(ABC):
    def __init__(self):
        self._account = None

    @abstractmethod
    def add_account_type(self):
        pass

    @abstractmethod
    def add_account_number(self, account_number):
        pass

    @abstractmethod
    def add_owner(self, owner):
        pass


class SavingsAccountBuilder(AccountBuilder):
    def __init__(self):
        super().__init__()
        self._account = SavingsAccount()
        self._account.set_account_type()

    def add_account_number(self, account_number):
        self._account.account_number = account_number

    def add_owner(self, owner):
        self._account.owner = owner


class SavingsAccount(AbstractAccount):
    def set_account_type(self):
        self.account_type = 'saving'
