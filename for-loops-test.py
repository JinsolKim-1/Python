#practice problem #1: for-loops
x = int(input("Enter a positive integer: "))
par = 0

for i in range (1, x+1):
    if i % 2 == 0:
        par += i
        
print ("The sum of even numbers in range 1 to " + str(x) + " is: " + str(par))

k = str(input("Press ENTER to exit!"))