from abc import ABC, abstractmethod


class Account(ABC):
    account_number: int
    balance: float
    owner_id: str
    interest_rate: float

    @abstractmethod
    def account_type(self):
        pass

    @abstractmethod
    def owner(self):
        pass


class SavingsAccount(Account):
    def __init__(self, owner):
        self.owner = owner

    def account_type(self):
        return 'savings'

    def owner(self):
        return self.owner


class DepositAccount(Account):
    def __init__(self, owner):
        self.owner = owner

    def account_type(self):
        return 'deposit'

    def owner(self):
        return self.owner


class CreditAccount(Account):
    def __init__(self, owner):
        self.owner = owner

    def account_type(self):
        return 'credit'

    def owner(self):
        return self.owner


class AccountFactory:
    @staticmethod
    def create_account(account_type, owner):
        if account_type == 'savings':
            return SavingsAccount(owner=owner)
        elif account_type == 'deposit':
            return DepositAccount(owner=owner)
        elif account_type == 'credit':
            return CreditAccount(owner=owner)
        else:
            raise ValueError("Unknown account type")

    @staticmethod
    def deposit(self, account: DepositAccount, amount: float):
        account.balance += amount
        print()
