pet = str(input("What is your pet? "))

x = "dog"
y = "cat"
z = "bird"

age = int(input("What is your pet's age? "))
weight = float(input("What is your pet's weight? "))

age = age * 52
weight = weight / 2.205


if pet == x or pet == y or pet == z:
    print("Your pet's age is approximately " + str(age) + " weeks old")
    print("Your pet's weight in Kilogram is: " + str(weight) + " or " + str(round(weight)) + " Kg")
else:
    print("That's an exotic animal!")
