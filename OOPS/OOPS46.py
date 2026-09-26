class Doctor:
    def __init__(self, name):
        self.name = name
class Patient:
    def __init__(self, name):
        self.name = name
class BillingService:
    def generate_bill(self, amount):
        print("Bill amount:", amount)
class Hospital:
    def __init__(self):
        self.doctors = [
            Doctor("Dr. Ravi"),
            Doctor("Dr. Priya")
        ]
        self.patients = [
            Patient("Arun"),
            Patient("Sita")
        ]
    def create_bill(self, billing_service):
        billing_service.generate_bill(5000)
hospital = Hospital()
billing = BillingService()
hospital.create_bill(billing)