def outer():
    def inner():
        print("Hello from inner function")
    return inner
result = outer()
result()