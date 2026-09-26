import csv
try:
    with open("students.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("CSV file not found")
except PermissionError:
    print("Permission denied")
except Exception as e:
    print("Error:", e)