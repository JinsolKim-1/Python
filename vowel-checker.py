#practice problem #2: for-loops
x = input("Enter a word or sentence: ")
x = x.lower()
par = 0

for i in x:
    if i in 'aeiou':
        par += 1

print ("Number of vowels: " + str(par))

k = str(input("Press ENTER to exit!"))