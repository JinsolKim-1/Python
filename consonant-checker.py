#practice problem #3: for-loops
z = input("Enter a word or a sentence: ")
z = z.lower()
par = 0

for i in z:
    if i in 'bcdfghjklmnpqrstvwxyz':
        par += 1

print ("Number of consonant letters: " + str(par))

k = str(input("Press ENTER to exit!"))