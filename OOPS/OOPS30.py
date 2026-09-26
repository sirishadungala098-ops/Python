class CertificateGenerator:
    def generate(self, student):
        print("Certificate generated for", student)
class Course:
    def __init__(self, course_name):
        self.course_name = course_name
    def complete_course(self, certificate_generator):
        print(self.course_name, "completed")
        certificate_generator.generate("Sirisha")
course = Course("Python")
certificate = CertificateGenerator()
course.complete_course(certificate)