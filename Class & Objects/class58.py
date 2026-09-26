class StringOperations:
    def reverse(self, text):
        return text[::-1]
    def vowels(self, text):
        count = 0
        for ch in text:
            if ch in "aeiouAEIOU":
                count += 1
        return count
    def palindrome(self, text):
        return text == text[::-1]
s = StringOperations()
print(s.reverse("python"))
print(s.vowels("python"))
print(s.palindrome("madam"))