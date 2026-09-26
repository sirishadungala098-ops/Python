from abc import ABC, abstractmethod

class Course(ABC):
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    @abstractmethod
    def start_course(self):
        pass

class OnlineCourse(Course):
    def start_course(self):
        print("Online:", self.name)

class OfflineCourse(Course):
    def start_course(self):
        print("Offline:", self.name)

OnlineCourse("Python", "3 Months").start_course()
OfflineCourse("Java", "6 Months").start_course()