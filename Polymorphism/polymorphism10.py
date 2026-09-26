class Android:
    def show_features(self):
        print("Android: Customizable and flexible")
class iPhone:
    def show_features(self):
        print("iPhone: Secure and user-friendly")
class WindowsPhone:
    def show_features(self):
        print("Windows Phone: Windows-based interface")
phones = [Android(), iPhone(), WindowsPhone()]
for phone in phones:
    phone.show_features()