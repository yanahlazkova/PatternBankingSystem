from abc import ABC, abstractmethod
from account1 import BankAccountBuilder, BankAccount
import random
import datetime


def generate_unique_account_number(mfo_bank):
    """Генераці унікального номера рахунку клиента."""
    # Отримання поточної дати та часу
    data = datetime.datetime.now()
    data_part = data.strftime("%Y%m%d%H%M%S")

    # Генеруємо випадкову частину номера
    random_part = random.randint(10, 99)

    return f'UA{random_part}{mfo_bank}{data_part}'


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
    def __init__(self):
        self.client = None

    def create_client(self, name, client_id):
        client = Client(name=name, client_id=client_id)
        # client_account = self.create_account('savings',
        #                                      client=client,
        #                                      # account_number=generate_unique_account_number(820172),
        #                                      overdraft_limit=100)
        # return client, client_account
        return client

    @staticmethod
    def create_account(account_type,
                       client,
                       interest_rate=5,
                       account_number=None, #'UA' + str(fake.random_number(27)),
                       overdraft_limit=None,
                       credit_limit=None,
                       period_time=None,
                       balance=0
                       ):
        account_builder = (BankAccountBuilder(client.get_name(), account_number=generate_unique_account_number(820172))
                           .with_interest_rate(interest_rate))
        if account_type == 'savings':
            new_account = account_builder.build(account_type, overdraft_limit=overdraft_limit)
            client.add_account(new_account)
            return new_account
        if account_type == 'deposit':
            new_account = account_builder.build(account_type, period_time=period_time, balance=balance)
            client.add_account(new_account)
            return new_account
        if account_type == 'credit':
            new_account = account_builder.build(account_type, credit_limit=credit_limit)
            client.add_account(new_account)
            return new_account

        def add_account_to_client(self, account):
            self.client.add_account(account)




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