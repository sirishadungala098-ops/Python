class EducationalInstitution:
    def conduct_classes(self):
        print("Classes are conducted")
class Department:
    def __init__(self, name):
        self.name = name
class ExaminationService:
    def conduct_exam(self):
        print("Examination is conducted")
class University(EducationalInstitution):
    def __init__(self):
        self.departments = [
            Department("Computer Science"),
            Department("Commerce"),
            Department("Science")
        ]
    def conduct_examination(self, exam_service):
        exam_service.conduct_exam()
university = University()
exam = ExaminationService()
university.conduct_classes()
university.conduct_examination(exam)