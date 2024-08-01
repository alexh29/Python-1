try:
#Assigning my variables
    principal = int(input("What is your principal amount: "))
    interest = int(input("What is your interest rate (in percentage): "))
    time = int(input("How long is your time period (in years): "))

#this explains the calculation
    processing = principal * interest * time/100


#this displays the final answer
    print("The simple interest is:", processing)

except ValueError:

    print("Please enter a numeric value")