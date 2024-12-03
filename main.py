from bank import Bank
from client import Client
from account import AccountFactory
from faker import Faker
import uuid

fake = Faker()

my_bank = Bank()

for _ in range(5):
    new_client = Client(fake.name(), uuid.uuid4())
    new_account = AccountFactory().create_account('savings', new_client)
    my_bank.add_client(new_client)
    my_bank.add_account(new_account)

print("Clients:")
for client in my_bank.get_list_clients():
    print(f"Name: {client.name}, ID: {client.client_id}")

print("\nAccounts:")
for account in my_bank.get_list_accounts():
    print(f"Account Type: {account.get_account_type()}, Owner: {account.owner.name}")
