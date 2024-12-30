from abc import ABC, abstractmethod
from account1 import BankAccountBuilder, BankAccount


class AbstractPerson(ABC):
    @abstractmethod
    def get_client_id(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def add_account(self, number_account: BankAccount):
        pass


class Client(AbstractPerson):
    def __init__(self, name, client_id):
        self.name = name
        self.client_id = client_id
        self.list_accounts = []

    def get_client_id(self):
        return self.client_id()

    def get_name(self):
        return self.name

    def add_account(self, account: BankAccount):
        self.list_accounts.append(account)

    def get_list_accounts(self):
        return "\n".join(f'\t{index + 1} {account.account_type}: {account.account_number}' for index, account in enumerate(self.list_accounts))

    def __str__(self):
        return (f'id: {self.client_id}\tname: {self.name}\n'
                f'accounts:\n'
                f'{self.get_list_accounts()}')



from faker import Faker


fake = Faker()

class ClientFactory:

    def create_client(self, name, client_id):
        client = Client(name=name, client_id=client_id)
        client_account = self.create_account('savings', client_name=client.get_name(), overdraft_limit=100)
        client.add_account(client_account)
        return client, client_account

    @staticmethod
    def create_account(account_type,
                       client_name,
                       interest_rate=5,
                       account_number='UA' + str(fake.random_number(27)),
                       overdraft_limit=None,
                       credit_limit=None,
                       period_time=None,
                       balance=0
                       ):
        account_builder = (BankAccountBuilder(client_name, account_number)
                           .with_interest_rate(interest_rate))
        if account_type == 'savings':
            return account_builder.build(account_type, overdraft_limit=overdraft_limit)
        if account_type == 'deposit':
            return account_builder.build(account_type, period_time=period_time, balance=balance)
        if account_type == 'credit':
            return account_builder.build(account_type, credit_limit=credit_limit)





# from faker import Faker
# fake = Faker()
#
# for index in range(5):
#     new_client = ClientFactory.create_client(fake.name(), str(uuid.uuid4()))
#     client_account = 'UA' + str(fake.random_number(27))
#     new_client.add_account(client_account)
#     print(f'{index + 1}.', new_client)
#
# new_account = 'UA' + str(fake.random_number(27))
# new_client.add_account(new_account)
#
# print(new_client)