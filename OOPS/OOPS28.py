class BillingService:
    def generate_bill(self, amount):
        print("Hospital bill:", amount)
class Hospital:
    def create_bill(self, billing_service):
        billing_service.generate_bill(5000)
hospital = Hospital()
billing = BillingService()
hospital.create_bill(billing)