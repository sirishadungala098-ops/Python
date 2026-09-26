employees={
    "Siri":50000,
    "Tanu":60000,
    "Bhagya":65000,
    "Sravya":70000,
    "Sailu":75000
}
for name,salary in employees.items():
    if salary > 50000:
        print(name,salary)