num = int(input("Enter the number to check: "))
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

if num <= upper and num >= lower:
    print ("The number is within range!")
elif num < lower:
    print ("The number is below the range! ")
elif num > upper:
    print ("The number is above the range! ")

k=input(("press ") + ("'ENTER'") + (" to exit"))