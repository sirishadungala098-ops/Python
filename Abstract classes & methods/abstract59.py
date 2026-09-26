from abc import ABC, abstractmethod

class Authentication(ABC):
    @abstractmethod
    def authenticate(self):
        pass
class Password(Authentication):
    def authenticate(self):
        print("Login using Password")
class OTP(Authentication):
    def authenticate(self):
        print("Login using OTP")
class GoogleLogin(Authentication):
    def authenticate(self):
        print("Login using Google")
class Biometric(Authentication):
    def authenticate(self):
        print("Login using Biometric")
Password().authenticate()
OTP().authenticate()
GoogleLogin().authenticate()
Biometric().authenticate()