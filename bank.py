# Паттерн Singleton (Одиночка).
# Используется для управления единственным экземпляром класса. Например, для класса,
# представляющего сам банк, чтобы гарантировать, что во всей системе существует только один объект Bank.

class Bank:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Bank, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.clients = []
        self.accounts = []

    def add_client(self, client):
        self.clients.append(client)

    def add_account(self, account):
        self.accounts.append(account)
