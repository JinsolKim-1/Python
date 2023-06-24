
rows = int(input("How many rows: "))
columns = int(input("How many columns: "))
sign = input("Enter a variable: ")

for i in range (rows):
    for j in range(columns):
        print (sign, end = "")
    print()

k = str(input("Press ENTER to exit!"))