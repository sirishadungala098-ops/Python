class Calculator:
    def add(self, a, b):
        return a + b
    def display(self):
        result = self.add(10, 20)
        print("Sum:", result)
c = Calculator()
c.display()