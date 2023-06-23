#practice problem #4: for-loops
y = int(input("Input a number: "))

print("multiplication table for: " + str(y))

for i in range (0, 21):
    ans = i*y
    print (i , " x " , y , "=" , ans)

k = str(input("Press ENTER to exit!"))