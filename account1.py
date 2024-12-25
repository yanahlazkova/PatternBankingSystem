from abc import ABC, abstractmethod


class BankAccount:
    def __init__(self):
        self.__account_type = None
        self.__account_number = None
        self.__balance = 0.0
        self.__owner = None
        self.__interest_rate = 0.0

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

    # @balance.setter
    def set_initial_balance(self, initial_balance):
        self.__balance = initial_balance

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

    def interest_accrual_on_balance(self):
        """ Натахування відсотків на баланс """
        interest_amount = self.__balance * self.__interest_rate / 100
        self.__balance += interest_amount
        print(f"Нараховано відсотки {interest_amount}$\n"
              f"Баланс: {self.__balance}")

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def __str__(self):
        return (f'Client: {self.__owner}\n'
                f'Account: "{self.__account_type}" - "{self.__account_number}"\n'
                f'Interest rate: {self.__interest_rate}%\n'
                f'balance: {self.__balance}$')


class SavingsAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self._fixed_interest_rate = None
        self._overdraft_limit = None

    def set_account_type(self):
        self.account_type = 'savings'
    #
    # def set_initial_balance(self, initial_balance):
    #     self.set_initial_balance(initial_balance)

    def deposit(self, amount):
        self.deposit(amount)

    def withdraw(self, amount):
        if self.balance >= self._overdraft_limit:
            self.withdraw(amount)
        else:
            raise ValueError(f'Недостатньо коштів на рахунку {self.balance} $\n'
                             f'Мінімальна допустима межа {self._overdraft_limit} $')

    def interest_accrual_on_balance(self):
        """ Натахування відсотків на баланс """
        self.interest_accrual_on_balance()


class DepositAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self._fixed_period_time = None  # фіксований період часу в місяцях
        self._interest_penalty = None  # відсоток штрафу при знятті коштів

    def set_account_type(self):
        self.account_type = 'deposit'

    def set_fixed_period_time(self, period_time):
        self._fixed_period_time = period_time

    def set_interest_penalty(self, interest_penalty):
        self._interest_penalty = interest_penalty
    #
    # def deposit(self, amount):
    #     self.deposit(amount)

    def withdraw_account(self, amount):
        penalty = self.penalty_accrual(amount)
        if self.balance >= amount + penalty:
            self.withdraw(amount + penalty)
            print(f'Нараховано штраф {penalty} $, Залишок на рахунку: {self.balance} $')

        else:
            raise ValueError(f'Недостатньо грошей на рахунку. Штраф: {penalty} $'
                             f'Баланс: {self.balance} $')

    def penalty_accrual(self, amount):
        """ нарахування штрафу"""
        if self._fixed_period_time > 0:
            return amount * self._interest_penalty / 100
        else:
            return 0

    def interest_accrual(self):
        if self._fixed_period_time > 0:
            self.interest_accrual_on_balance()
            self._fixed_period_time -= 1
        else:
            print('Депозитний період закінчився, можете зняти гроші з рахунку')

    def __str__(self):
        return (f'Client: {self.owner}\n'
                f'Account: "{self.account_type}" - "{self.account_number}"\n'
                f'Interest rate: {self.interest_rate}%\n'
                f'Залишок депозитного періоду {self._fixed_period_time}\n'
                f'balance: {self.balance}$')


class CreditAccount(BankAccount):
    def __init__(self):
        """ Баланс - буде сумою кредиту """
        super().__init__()



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

    def set_initial_balance(self, initial_balance):
        self._account.set_initial_balance(initial_balance)

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

    def set_initial_balance(self, initial_balance):
        self._account.set_initial_balance(initial_balance)

    def set_interest_rate(self, interest_rate):
        self._account.interest_rate = interest_rate

    def fixed_period_time(self, period_time):
        self._account.set_fixed_period_time(period_time)

    def set_interest_penalty(self, interest_penalty):
        self._account.set_interest_penalty(interest_penalty)


class AccountFactory:
    @staticmethod
    def construct_account(account_type, account_data) -> BankAccount:
        if account_type == 'savings':
            owner, account_number, balance, interest_rate = account_data
            account_builder = SavingsAccountBuilder()
            account_builder.create_account()
            account_builder.set_account_type()
            account_builder.add_account_number(account_number)
            account_builder.add_owner(owner)
            account_builder.set_initial_balance(balance)
            return account_builder.build()
            # return new_account
        elif account_type == 'deposit':
            owner, account_number, balance, interest_rate, period_time, interest_penalty = account_data
            account_builder = DepositAccountBuilder()
            account_builder.create_account()
            account_builder.set_account_type()
            account_builder.add_account_number(account_number)
            account_builder.add_owner(owner)
            account_builder.set_initial_balance(balance)
            account_builder.set_interest_rate(interest_rate)
            account_builder.fixed_period_time(period_time)
            account_builder.set_interest_penalty(interest_penalty)
            return account_builder.build()
            # return new_account


from faker import Faker

fake = Faker()

new_data_savings_account = ('Alex', fake.random_number(27), 1000, 5)
new_account = AccountFactory().construct_account('savings', new_data_savings_account)

print(new_account)

new_data_deposit_account = ('Peter', fake.random_number(27), 5000, 10, 12, 0.1)
deposit_account = AccountFactory().construct_account('deposit', new_data_deposit_account)
print(deposit_account)
# Withdraw on deposit_account
print("Зняття грошей")
x = True
while x:
    amount_money = int(input('Введіть сумму зняття коштів: '))
    deposit_account.withdraw_account(amount_money)
    print()
    print('Нарахування відсотків та зменьшення періоду')
    deposit_account.interest_accrual()
    print(deposit_account)
    print()
    withdraw = input('Продовжити? ')
    if withdraw == 'N' or withdraw == 'n':
        break
    print()

