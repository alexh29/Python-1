try:
#input, defines value in hours, creates equation for changing from Hrs to min/sec
    timeH = float(input("Enter a time duration in hours: "))

    timeM = timeH * 60

    timeS = timeM * 60
#output
    print("Your time in minutes is:", timeM)
    print("Your time in seconds is:", timeS)
# Error handling
except ValueError:
    print("Enter a numeric value")