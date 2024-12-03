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
    def set_main_account(self, number_account):
        pass


class Client(AbstractPerson):
    def __init__(self, name, client_id):
        self.name = name
        self.client_id = client_id
        self.main_account = None

    def get_client_id(self):
        return self.client_id()

    def get_name(self):
        return self.name()

    def set_main_account(self, number_account):
        self.main_account(number_account)
