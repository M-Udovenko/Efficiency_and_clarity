from abc import ABC, abstractmethod
from models.credentials import FacebookCredentials, LinkedInCredentials
from models.social_network import SocialNetwork, Facebook, LinkedIn


class SocialNetworkFactory(ABC):
    @abstractmethod
    def create_network(self) -> SocialNetwork:
        pass


class FacebookFactory(SocialNetworkFactory):
    def __init__(self, login: str, password: str):
        self.credentials = FacebookCredentials(login, password)

    def create_network(self) -> Facebook:
        return Facebook(self.credentials)


class LinkedInFactory(SocialNetworkFactory):
    def __init__(self, email: str, password: str):
        self.credentials = LinkedInCredentials(email, password)

    def create_network(self) -> LinkedIn:
        return LinkedIn(self.credentials)

