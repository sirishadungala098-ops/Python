class GoogleLogin:
    def login(self):
        print("Login using Google")
class FacebookLogin:
    def login(self):
        print("Login using Facebook")
class EmailLogin:
    def login(self):
        print("Login using Email")
def authenticate(user):
    user.login()
authenticate(GoogleLogin())
authenticate(FacebookLogin())
authenticate(EmailLogin())