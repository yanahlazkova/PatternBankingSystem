from bank import Bank
from client import Client, ClientFactory
from account import AccountFactory
from faker import Faker


fake = Faker()

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
account_savings = client.list_accounts[0]
credit_account.transfer(account_savings, 60000)
print(credit_account, account_savings)
# my_bank.get_list_clients()
# my_bank.get_list_accounts()

