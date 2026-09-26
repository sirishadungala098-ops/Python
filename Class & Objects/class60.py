class Temperature:
    def celsius_to_fahrenheit(self, c):
        return (c * 9/5) + 32
    def fahrenheit_to_celsius(self, f):
        return (f - 32) * 5/9
t = Temperature()
print(t.celsius_to_fahrenheit(25))
print(t.fahrenheit_to_celsius(77))