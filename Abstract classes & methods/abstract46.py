from abc import ABC, abstractmethod

class Course(ABC):

    @abstractmethod
    def start(self):
        pass

    def display_course_details(self):
        print("Course: Python")


class OnlineCourse(Course):

    def start(self):
        print("Online course started")


c = OnlineCourse()
c.start()
c.display_course_details()