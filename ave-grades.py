
num = int(input("How many subjects you have: "))
x = []
sum = 0

for i in range(num):
    z = int(input("Input Grades: "))
    x.append (z)
    sum += z

print(x)
ave = sum / num
print("Your average is: ", ave)