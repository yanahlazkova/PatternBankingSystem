from bank import Bank
from client import Client, ClientFactory
from faker import Faker


fake = Faker('uk_UA')

my_bank = Bank()
print('---Створення нового клієнта---\n')
client = my_bank.create_new_client(fake.name())
account_savings = my_bank.open_new_account_client(client, 'savings')
print(client)
print('\n---Додавання клієнту кредитного рахунку---\n')
credit_account = my_bank.open_new_account_client(client=client, account_type='credit')
print('\n---Збільшення кредитного ліміту---\n')
credit_account.set_credit_limit(100000)
print(client)
print('\n---Поповнення ощадного рахунку з кредитного---\n')
credit_account.transfer(account_savings, 60000)
print(credit_account, account_savings)
print('\n---Нарахування відсотків на кредитний рахунок---\n')
credit_account.apply_loan_interest()
print('\n---Створення ще одного клієнта ---\n')
client_two = my_bank.create_new_client(fake.name())
account_savings_two = my_bank.open_new_account_client(client_two, 'savings')
account_savings_two.increase_balance(100000)
print(client_two)
print('\n---Переведення коштів від другого клієнта першому ---\n')
my_bank.transfer_between_client_account(account_savings_two, credit_account, 60000)

print('First client\n', credit_account)
print('Second client\n', account_savings_two)

print('\n---Загальний баланс банку ---\n')
my_bank.get_list_accounts()
print(my_bank.get_total_balance(), '$')
