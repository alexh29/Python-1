# Input: Ask the user to enter their marks for three subjects
mark1 = input("Enter the marks for subject 1: ")
mark2 = input("Enter the marks for subject 2: ")
mark3 = input("Enter the marks for subject 3: ")

# Error handling: Ensure marks are numeric and within the range of 0 to 100
if mark1.isdigit() and mark2.isdigit() and mark3.isdigit():
    mark1 = int(mark1)
    mark2 = int(mark2)
    mark3 = int(mark3)

    if 0 <= mark1 <= 100 and 0 <= mark2 <= 100 and 0 <= mark3 <= 100:
        # Processing: Calculate the average of the marks
        average = (mark1 + mark2 + mark3) / 3

        # Determine the grade based on the average
        if average >= 90:
            grade = "A"
        else:
            if average >= 80:
                grade = "B"
            else:
                if average >= 70:
                    grade = "C"
                else:
                    if average >= 60:
                        grade = "D"
                    else:
                        grade = "F"

        # Output: Display the calculated grade
        print(f"Your grade is {grade}.")
    else:
        print("Error: Marks should be between 0 and 100.")
else:
    print("Error: Please enter valid numeric values for all marks.")
