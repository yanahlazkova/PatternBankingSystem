from bank import Bank
from client import Client, ClientFactory
from account import AccountFactory
from faker import Faker
import uuid

fake = Faker()

my_bank = Bank()

for index in range(1):
    new_client = ClientFactory.create_client(fake.name(), str(uuid.uuid4()))
    account_data = new_client.client_id, str(fake.random_number(27))
    new_account = AccountFactory().create_account('savings', account_data)
    new_client.add_account(new_account.account_number)
    my_bank.add_client(new_client)
    my_bank.add_account(new_account)

print("Clients:")
for client in my_bank.get_list_clients():
    print(f"Name: {client.name}, ID: {client.client_id}")

print("\nAccounts:")
for account in my_bank.get_list_accounts():
    # print(f"Account Type: {account.get_account_type()}, Owner: {account.get_owner_id}")
    print(account)