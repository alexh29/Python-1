
def is_palindrome(string):
    return string == string[::-1]

result = is_palindrome("racecar")
print(result)  # Output will be True

result = is_palindrome("hello")
print(result)  # Output will be False
