from bank import Bank
from client import Client, ClientFactory
from account import AccountFactory
from faker import Faker
import uuid

fake = Faker()

my_bank = Bank()
print('---Створення нового клієнта---\n')
my_bank.create_new_client(fake.name())
print('\n---Додавання клієнту кредитного рахунку---\n')
my_bank.open_new_account_client(client=my_bank.clients[0], account_type='credit')
my_bank.get_list_clients()
my_bank.get_list_accounts()

