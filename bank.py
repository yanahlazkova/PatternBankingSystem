# Паттерн Singleton (Одиночка).
# Используется для управления единственным экземпляром класса. Например, для класса,
# представляющего сам банк, чтобы гарантировать, что во всей системе существует только один объект Bank.
from client import ClientFactory
import uuid


class Bank:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Bank, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.clients = []
        self.accounts = []

    def create_new_client(self, name, client_id=uuid.uuid4()):
        new_client, client_account = ClientFactory().create_client(name, client_id)
        self.add_client(new_client)
        self.add_account(client_account)

    def add_client(self, client):
        self.clients.append(client)

    def add_account(self, account):
        self.accounts.append(account)

    def open_new_account_client(self, client, account_type):
        client_account = (ClientFactory().
                          create_account(account_type=account_type,
                                         client_name=client.get_name(),
                                         interest_rate=3,
                                         credit_limit=50000))
        self.add_account(client_account)

    def get_list_clients(self):
        for client in self.clients:
            print(client)

    def get_list_accounts(self):
        for account in self.accounts:
            print(account)
