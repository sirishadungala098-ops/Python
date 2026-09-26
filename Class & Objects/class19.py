class Hospital:
    def __init__(self, patient_name, age, disease, doctor_name):
        self.patient_name = patient_name
        self.age = age
        self.disease = disease
        self.doctor_name = doctor_name
p1 = Hospital("Ravi", 30, "Fever", "Dr. Kumar")
p2 = Hospital("Anu", 25, "Cold", "Dr. Rani")
p3 = Hospital("Sri", 40, "Diabetes", "Dr. Raj")
print(p1.patient_name, p1.age, p1.disease, p1.doctor_name)
print(p2.patient_name, p2.age, p2.disease, p2.doctor_name)
print(p3.patient_name, p3.age, p3.disease, p3.doctor_name)