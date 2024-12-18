from abc import ABC, abstractmethod
from faker import Faker

fake = Faker()


class AbstractAccount(ABC):
    def __init__(self):
        self.__account_type: str = ''
        self.__account_number: str = ''
        self.__balance: float = 0.0
        self.__owner_id: str = ''
        self.__interest_rate: float = 0.0

    @abstractmethod
    def set_account_type(self):
        pass

    # def get_account_type(self):
    #     return self.__account_type

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def set_owner_id(self, owner_id):
        self.__owner_id = owner_id

    # def get_owner_id(self):
    #     return self.__owner_id

    def set_interest_rate(self, interest_rate):
        self.__interest_rate = interest_rate

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

    @abstractmethod
    def interest_accrual(self):
        """ метод нарахування відсотків"""
        pass

    def __str__(self):
        return (f'Client ID: {self.owner_id}\n'
                f'Account: "{self._account_type}" - "{self.account_number}"\n'
                f'balance: {self.balance} $')


class SavingsAccount(AbstractAccount):
    def set_account_type(self):
        self.__account_type = 'savings'

    def set_balance(self, balance):
        self.__balance += self.__balance
        return self.__balance

    def deposit(self, amount):
        self.set_balance(amount)

    def withdraw(self, amount):
        self.balance -= amount if self.balance - amount else f'Не достатньо коштів на рахунку'

    def interest_accrual(self):
        interest = self.interest_rate * self.balance / 100
        self.balance += interest
        print(f'Balance is {self.balance}')


class DepositAccount(AbstractAccount):
    def __init__(self, fixed_period_time=None):
        self.fixed_period_time = fixed_period_time # фіксований період часу в місяцях
        self.interest_penalty = 5 # відсоток штрафу при знятті коштів

    def set_account_type(self):
        self.account_type = 'deposit'

    def set_balance(self, balance):
        return self.balance

    def deposit(self, amount):
        self.set_balance(amount)

    def withdraw(self, amount):
        """ Заборона зняття коштів до закінчення депозитного періоду,
        або можливість зняття зі штрафом """
        # Логіка: 1) Якщо знімається не вся сумма до закінчення періоду - заборона зняття
        # 2) Вся сумма - вирахувати штраф. Перевірити чи достатньо коштів для зняття зі штрафом
        if self.fixed_period_time > 0:
            if amount < self.balance:
                # заборона зняття
                print(f'Не можливо зняти {amount} $ до закінчення депозитного періоду')
                return
            if amount == self.__balance:
                penalty = self.penalty_accrual()
                amount_withdraw = self.balance - penalty

                print(f'Нараховано штраф {penalty} $, Сума до видачі: {self.balance - penalty} $')
                self.set_balance(-self.balance)

    def penalty_accrual(self):
        """ нарахування штрафу"""
        penalty = self.balance * self.interest_penalty / 100
        return penalty

    def interest_accrual(self):
        """ Має можливість накопичувати відсотки протягом фіксованого періоду часу (в місяцях)
        Період часу при нарахуванні відсотків буде зменьшуватись на 1 місяць """
        if self.fixed_period_time > 0:
            interest = self.interest_rate * self.balance / 100
            self.balance += interest
            self.fixed_period_time -= 1
            print(f"Відсотки нараховані ({interest} $). На рахунку {self.balance}")
        else:
            print("Термін накопичення відсотків закінчився")


class CreditAccount(AbstractAccount):
    def set_account_type(self):
        self.account_type = 'credit'

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
    def create_account(account_type, account_data) -> AbstractAccount:
        if account_type == 'savings':
            account = SavingsAccount()
            account.set_account_type()
            account.set_account_number(fake.random_number(27))
            return account
        elif account_type == 'deposit':
            return DepositAccount()
        elif account_type == 'credit':
            return CreditAccount()
        else:
            raise ValueError("Un account type")

    @staticmethod
    def deposit(self, account, amount):
        account.balance += amount
        print()
        return f'Your balance = {self.balance}'
