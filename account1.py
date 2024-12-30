from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, account_number, owner, interest_rate):
        self.__account_type = None
        self.__account_number = account_number
        self.__balance = 0  # Початковий баланс завжди 0
        self.__owner = owner
        self.__interest_rate = interest_rate

    @property
    def account_type(self):
        return self.__account_type

    @account_type.setter
    def account_type(self, account_type):
        self.__account_type = account_type

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

    def increase_balance(self, amount):
        """Збільшити баланс"""
        self.__balance += amount
        return self

    def reduce_balance(self, amount):
        """Зменшити баланс"""
        self.__balance -= amount

    @property
    def owner(self):
        return self.__owner

    @property
    def interest_rate(self):
        return self.__interest_rate

    @abstractmethod
    def deposit(self, amount):
        """Внесення коштів на рахунок."""
        # self.__balance += amount
        pass

    @abstractmethod
    def withdraw(self, amount):
        """Зняття коштів з рахунку."""
        pass

    def calculate_interest(self):
        """Обчислення відсотків."""
        return self.balance * self.interest_rate / 100

    def apply_interest(self):
        """Нарахування відсотків на баланс."""
        interest = self.calculate_interest()
        print(f"Нараховано відсотки {interest}$")
        self.deposit(interest)

    def get_account_info(self):
        return (f'Client: {self.__owner}\n'
                f'Account: "{self.__account_type}" - "{self.__account_number}"\n'
                f'Interest rate: {self.__interest_rate}%\n'
                f'balance: {self.__balance}$')

    def __str__(self):
        return self.get_account_info()


class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner, interest_rate):
        super().__init__(account_number, owner, interest_rate)
        self._overdraft_limit = 0
        self.account_type = 'savings'

    def set_overdraft_limit(self, limit):
        self._overdraft_limit = limit
        return self

    def deposit(self, amount):
        self.increase_balance(amount)
        print(f'На рахунку: {self.balance}$')

    def withdraw(self, amount):
        if self.balance >= self._overdraft_limit + amount:
            self.reduce_balance(amount)
            print(f'На рахунку: {self.balance}$')
        else:
            raise ValueError(f'Недостатньо коштів на рахунку {self.balance} $\n'
                             f'Мінімальна допустима межа {self._overdraft_limit} $')


class DepositAccount(BankAccount):
    def __init__(self, account_number, owner, interest_rate):
        super().__init__(account_number, owner, interest_rate)
        self.account_type = 'deposit'
        self.__fixed_period_time = 0  # фіксований період часу в місяцях
        self._interest_penalty = 2  # відсоток штрафу при знятті коштів

    @property
    def fixed_period_time(self):
        return self.__fixed_period_time

    def set_fixed_period_time(self, period_time):
        self.__fixed_period_time = period_time
        return self

    def set_interest_penalty(self, interest_penalty):
        self._interest_penalty = interest_penalty

    def deposit(self, amount):
        self.increase_balance(amount)

    def withdraw(self, amount):
        print('deposit account')
        penalty = self.penalty_accrual(amount)
        if self.balance >= amount + penalty:
            self.reduce_balance(amount + penalty)
            print(f'Нараховано штраф {penalty} $, Залишок на рахунку: {self.balance} $')

        else:
            print(f'Недостатньо грошей на рахунку. Штраф: {penalty} $'
                  f'Баланс: {self.balance} $')

    def penalty_accrual(self, amount):
        """ нарахування штрафу"""
        if self.__fixed_period_time > 0:
            return amount * self._interest_penalty / 100
        else:
            return 0

    def interest_accrual(self):
        if self.__fixed_period_time > 0:
            self.apply_interest()
            self.__fixed_period_time -= 1
        else:
            print('Депозитний період закінчився, можете зняти гроші з рахунку')

    def get_account_info(self):
        return (f'Client: {self.owner}\n'
                f'Account: "{self.account_type}" - "{self.account_number}"\n'
                f'Interest rate: {self.interest_rate}%\n'
                f'Залишок депозитного періоду {self.__fixed_period_time}\n'
                f'balance: {self.balance}$')


class CreditAccount(BankAccount):
    def __init__(self, account_number, owner, interest_rate):
        super().__init__(account_number, owner, interest_rate)
        self.account_type = 'credit'
        self.__credit_limit = 0  # кредитний ліміт
        # self.__credit_amount = 0 # сума кредиту
        self.__amount_accrued_interest = 0  # сума нарахованих відсотків
        # balance - кредитний залишок

    @property
    def credit_limit(self):
        return self.__credit_limit

    def set_credit_limit(self, credit_limit):
        self.__credit_limit = credit_limit
        return self

    #
    # @property
    # def credit_amount(self):
    #     return self.__credit_amount

    def deposit(self, amount):
        """Внесення коштів - зменьшення кредиту."""
        if self.balance + amount < 0:
            self.increase_balance(amount)
            print(f'Залишок по кредиту: {self.balance}$')
        elif self.balance + amount == 0:
            self.increase_balance(amount)
            print(f'Кредит погашено. \nЗалишок по кредиту: {self.balance}$')
        else:
            dif = self.balance + amount
            self.increase_balance(abs(self.balance))
            print(f'Кредит погашено. Заберіть здачу {dif}$')

    def withdraw(self, amount):
        """Зняття коштів, збільшення заборгованості по кредиту"""
        if self.__credit_limit >= self.balance - amount:
            self.reduce_balance(amount)
        else:
            print(f'Сума кредиту перевищує максимальний ліміт {self.__credit_limit}$')

    def apply_loan_interest(self):
        """Нарахування відсотків кредиту"""
        interest = self.calculate_interest()
        self.__amount_accrued_interest += interest
        self.apply_interest()


    def get_account_info(self):
        return (f'Client: {self.owner}\n'
                f'Account: "{self.account_type}" - "{self.account_number}"\n'
                f'Кредитний ліміт: {self.__credit_limit}$\n'
                f'Interest rate: {self.interest_rate}%\n'
                f'Сума нарахових відсотків: {abs(self.__amount_accrued_interest)}$\n'
                f'Залишок кредиту: {abs(self.balance)}\n')


class BankAccountBuilder:
    def __init__(self, account_number, owner):
        self.account_number = account_number
        self.owner = owner
        self.balance = 0
        self.interest_rate = 0

    def with_interest_rate(self, interest_rate):
        self.interest_rate = interest_rate
        return self

    # def build(self, account_type, overdraft_limit=None, period_time=None, credit_limit=None):
    def build(self, account_type, overdraft_limit=None, credit_limit=None, period_time=None, balance=0):
        self.balance = balance
        if account_type == "savings":
            return (SavingsAccount(self.account_number,
                                   self.owner,
                                   self.interest_rate)
                    .set_overdraft_limit(overdraft_limit)
                    .increase_balance(self.balance))
        elif account_type == "credit":
            return (CreditAccount(self.account_number,
                                  self.owner,
                                  self.interest_rate)
                    .set_credit_limit(credit_limit)
                    .increase_balance(0))
        elif account_type == "deposit":
            return (DepositAccount(self.account_number,
                                   self.owner,
                                   self.interest_rate)
                    .set_fixed_period_time(period_time)
                    .increase_balance(self.balance))
        else:
            raise ValueError("Invalid account type")

from faker import Faker

fake = Faker()
account_number, owner, balance = account_data = ('UA' + str(fake.random_number(27)),
                                                 fake.name(),
                                                 0)
interest_rate = 5
credit_limit = 100000
# period_time = 12
#
# deposit_builder = (BankAccountBuilder(account_number, owner)
#                    .with_interest_rate(interest_rate))
# deposit_account = deposit_builder.build('deposit',
#                                         period_time=period_time,
#                                         balance=balance)
#
# print(deposit_account)
#
# # Creating savings_account
# savings_builder = (BankAccountBuilder(account_number, owner)
#                    .with_interest_rate(interest_rate))
# savings_account = savings_builder.build('savings',
#                                         credit_limit=100,
#                                         balance=10000)
#
# print('Savings account:\n', savings_account)

# Creating credit account
credit_builder = (BankAccountBuilder(account_number, owner)
                  .with_interest_rate(interest_rate))
credit_account = credit_builder.build('credit', credit_limit=credit_limit)

print('Credit account:\n', credit_account)

# Withdraw on deposit_account
# print("Зняття грошей")
# x = True
# while x:
#     amount_money = float(input('Введіть сумму зняття коштів: '))
#     deposit_account.withdraw(amount_money)
#     print()
#     print('Нарахування відсотків та зменьшення періоду')
#     deposit_account.interest_accrual()
#     print(deposit_account)
#     print()
#     withdraw = input('Продовжити? ')
#     if withdraw == 'N' or withdraw == 'n':
#         break
#     print()

print('\n---Зняття кредитних коштів:---\n')
credit_account.withdraw(50000)
print(credit_account)
credit_account.withdraw(26000)
print(credit_account)
print('Погашення кредиту:')
credit_account.deposit(3000)
credit_account.deposit(3000)
print('Нарахування відсотків:')
credit_account.apply_loan_interest()
credit_account.apply_loan_interest()
print()
print('---Погашення кредиту---')
credit_account.deposit(77175)
print(credit_account)
