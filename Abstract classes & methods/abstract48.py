from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    def send(self):
        pass

    def display_message(self):
        print("Message: Hello")


class SMS(Notification):

    def send(self):
        print("SMS sent")


n = SMS()
n.send()
n.display_message()