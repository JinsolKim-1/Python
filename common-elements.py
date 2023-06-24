
x = int(input("How many number on First list:  "))
y = int(input("How many number on Second list: "))

first = []
sec = []
ans =[]

for i in range (x):
    c = int(input("Input First set of numbers: "))
    first.append (c)
for i in range (y):
    d = int(input("Input Second set of numbers: "))
    sec.append (d)

for i in first:
    for j in sec:
        if i == j:
            ans.append(i)

print ("1st list: ", first)
print ("2nd list: ", sec)
print ("Comparison: ", ans)

