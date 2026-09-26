def profile(**kwargs):
    print("Person Profile:")
    for key, value in kwargs.items():
        print(key, ":", value)
profile(
    name="Sirisha",
    age=21,
    city="Rajahmundry",
    profession="Student"
)