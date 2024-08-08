try:
#input
    currency = float(input("Enter the amount of money is USD: "))


#Processing
    processing = currency * 0.93

#output
    print("The value of your money in EUR is:", processing)

except ValueError:
    print("Please enter a numeric value")