import uuid
from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def client_id(self):
        pass

    @abstractmethod
    def name(self):
        pass


class Client(Person):
    def __init__(self, name, client_id):
        self.name = name
        self.client_id = client_id

    def client_id(self):
        return self.client_id()

    def name(self):
        return self.name()
