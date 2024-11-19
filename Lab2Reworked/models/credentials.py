from dataclasses import dataclass


@dataclass
class FacebookCredentials:
    login: str
    password: str


@dataclass
class LinkedInCredentials:
    email: str
    password: str

