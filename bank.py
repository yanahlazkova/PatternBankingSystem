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
        # client_factory = ClientFactory()
        # new_client = client_factory.create_client(name, client_id)
        # client_account = client_factory.create_account('savings', new_client, overdraft_limit=100)
        new_client = ClientFactory().create_client(name, client_id)
        self.add_client_to_list(new_client)
        # self.add_account(client_account)
        return new_client

    def open_new_account_client(self, client, account_type):
        client_account = (ClientFactory().
                          create_account(account_type=account_type,
                                         client=client))
        self.add_account_to_list(client_account)
        return client_account

    @staticmethod
    def transfer_between_client_account(with_account, to_account, amount):
        """Проведення транзакцій між рахунками різних клієнтів"""
        with_account.transfer(to_account, amount)

    def add_client_to_list(self, client):
        self.clients.append(client)

    def add_account_to_list(self, account):
        self.accounts.append(account)

    def get_total_balance(self):
        """Обчислення загальних активів банку"""
        return sum(account.balance for account in self.accounts)

    def get_list_clients(self):
        for index, client in enumerate(self.clients):
            print(index+1, client)

    def get_list_accounts(self):
        for index, account in enumerate(self.accounts):
            print(index+1, account)
