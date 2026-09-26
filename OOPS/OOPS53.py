class Employee:
    def work(self):
        print("Employee is working")
class Doctor(Employee):
    def work(self):
        print("Doctor treats patients")
class Nurse(Employee):
    def work(self):
        print("Nurse takes care of patients")
class Patient:
    def __init__(self, name):
        self.name = name
class BillingService:
    def generate_bill(self, amount):
        print("Hospital bill:", amount)
class Hospital:
    def __init__(self):
        self.doctors = [
            Doctor()
        ]
        self.patients = [
            Patient("Ravi"),
            Patient("Priya")
        ]
    def create_bill(self, billing):
        billing.generate_bill(5000)
hospital = Hospital()
billing = BillingService()
hospital.doctors[0].work()
hospital.create_bill(billing)