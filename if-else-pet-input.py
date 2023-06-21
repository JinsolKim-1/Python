import math

pet = str(input("what is your pet? "))
age = int(input("what is your pet's age? "))
weight = float(input("What is your pet' weight? "))

a = "What is your dog's weight? "
b = "What is your cat's weight? "
c = "What is your bird's weight? "

x = "What is your dog's age? "
y = "What is your cat's age? "
z = "What is your bird's age? "


age = age *52
weight = weight / 2.205

if pet == ("dog"):
    print (age)
        
elif pet == ("cat"):
    print (y)
elif pet == ("bird"):
    print (z)
else:
    print ("That's an exotic animal!")

    
