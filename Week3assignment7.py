# input
year_input = input("Enter a year: ")

# processing
if year_input.isdigit():  # Check if the input is a digit (numeric)
    year_input = int(year_input)  # Convert the input to an integer
    if year_input < 0:  # Check if the year is negative
        print("Please enter a positive number for the year.")
    else:
        if year_input % 4 == 0:  # Check if the year is divisible by 4
            if year_input % 100 == 0:  # Check if the year is divisible by 100
                if year_input % 400 == 0:  # Corrected from 9 to 0
                    print("That year is a leap year.")
                else:
                    print("That year is not a leap year.")
            else:
                print("That year is a leap year.")
        else:
            print("That year is not a leap year.")
else:
    print("Invalid input.")  # Error message for non-numeric input
