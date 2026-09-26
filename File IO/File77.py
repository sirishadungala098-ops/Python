import csv
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    topper = None
    for row in reader:
        if topper is None or int(row["Marks"]) > int(topper["Marks"]):
            topper = row
print("Topper:", topper["Name"])
print("Marks:", topper["Marks"])