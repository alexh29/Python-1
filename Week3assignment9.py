

char_input = input("Enter a single character: ")


if len(char_input) == 1 and char_input.isalpha():
    char = char_input.lower()
    if char in 'aeiou':

        print("the character is a voewl.")
    else:

        print("the character is a consonant")
else:
    if len(char_input) !=1:

        print("Error: Please only enter one character")
    else:
        print("Error: The input is not a letter")