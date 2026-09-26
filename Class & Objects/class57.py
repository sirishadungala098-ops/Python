class Number:
    def __init__(self, num):
        self.num = num

    def even(self):
        return self.num % 2 == 0

    def odd(self):
        return self.num % 2 != 0

    def prime(self):
        if self.num < 2:
            return False
        for i in range(2, self.num):
            if self.num % i == 0:
                return False
        return True
    def palindrome(self):
        return str(self.num) == str(self.num)[::-1]
n = Number(11)
print("Even:", n.even())
print("Odd:", n.odd())
print("Prime:", n.prime())
print("Palindrome:", n.palindrome())