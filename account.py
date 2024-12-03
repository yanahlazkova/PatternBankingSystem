from abc import ABC, abstractmethod


class AbstractAccount(ABC):
    account_number: int
    balance: float
    owner_name: str
    interest_rate: float

    @abstractmethod
    def get_account_type(self):
        pass

    @abstractmethod
    def get_owner(self):
        pass

    @abstractmethod
    def set_balance(self, balance):
        pass

    def __str__(self):
        return (f'Client: Name {self.owner_name}'
                f'Type account: "savings"'
                f'balance: {self.balance}')


class SavingsAccount(AbstractAccount):
    def __init__(self, owner):
        self.account_type = 'savings'
        self.owner = owner

    def get_account_type(self):
        return self.account_type

    def get_owner(self):
        return self.owner

    def set_balance(self, balance):
        return self.balance


class DepositAccount(AbstractAccount):
    def __init__(self, owner):
        self.account_type = 'deposit'
        self.owner = owner

    def get_account_type(self):
        return self.account_type

    def get_owner(self):
        return self.owner

    def set_balance(self, balance):
        return self.balance


class CreditAccount(AbstractAccount):
    def __init__(self, owner):
        self.account_type = 'credit'
        self.owner = owner

    def get_account_type(self):
        return self.account_type

    def get_owner(self):
        return self.owner

    def set_balance(self, balance):
        return self.balance


class AccountFactory:
    @staticmethod
    def create_account(account_type, owner) -> AbstractAccount:
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
        return f'Your balance = {self.balance}'
