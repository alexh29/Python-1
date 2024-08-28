# Input
rows = input("Enter the number of rows: ")

if rows.isdigit():
    rows = int(rows)
    if rows > 0:
        # Processing: Print the pattern of asterisks
        for i in range(1, rows + 1):
            print('*' * i)
    else:
        print("Please enter a positive number for the rows.")
else:
    print("Invalid input. Please enter a numeric value.")
