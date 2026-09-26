from abc import ABC, abstractmethod

class Authentication(ABC):
    @abstractmethod
    def login(self):
        pass

class PasswordLogin(Authentication):
    def login(self):
        print("Login using password")

class OTPLogin(Authentication):
    def login(self):
        print("Login using OTP")

logins = [PasswordLogin(), OTPLogin()]

for login in logins:
    login.login()