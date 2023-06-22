num = int(input("Enter the number to check: "))
lower = int(input("Enter the lower bound: "))
upper = int (input("Enter the upper bound: "))

if num <= upper or num == upper:
    print ("The number is within range!")
elif num < lower or num >= upper:
    print ("The number is out of range! ")

k=input(("press ") + ("'ENTER'") + (" to exit"))