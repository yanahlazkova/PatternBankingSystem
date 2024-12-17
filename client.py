import uuid
from abc import ABC, abstractmethod


class AbstractPerson(ABC):
    @abstractmethod
    def get_client_id(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def add_account(self, number_account):
        pass


class Client(AbstractPerson):
    def __init__(self, name, client_id):
        self.name = name
        self.client_id = client_id
        self.list_accounts = []

    def get_client_id(self):
        return self.client_id()

    def get_name(self):
        return self.name()

    def add_account(self, number_account):
        self.list_accounts.append(number_account)

    def get_list_accounts(self):
        return "\n".join(str(account) for account in self.list_accounts)

    def __str__(self):
        return (f'id: {self.client_id}\tname: {self.name}\n'
                f'accounts:\n'
                f'{self.get_list_accounts()}')



from faker import Faker
fake = Faker()


class ClientFactory:
    @staticmethod
    def create_client():
        client = Client(fake.name(), str(uuid.uuid4()))

        return client


for _ in range(5):
    new_client = ClientFactory.create_client()
    client_account = 'UA' + str(fake.random_number(27))
    new_client.add_account(client_account)
    print(new_client)

new_account = 'UA' + str(fake.random_number(27))
new_client.add_account(new_account)

print(new_client)