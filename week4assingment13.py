# Input
user_input = input("Enter a string: ")

# Processing: Remove spaces and convert the string to lowercase
simple_input = user_input.replace(" ", "").lower()

# checks if simple input is same backwards
if simple_input == simple_input[::-1]:
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')
