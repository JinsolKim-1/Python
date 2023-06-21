import math

x = "dog's age? "
y = "cat's age? "
z = "bird's age? "

x = str(x)
y = str(y)
z = str(z)

a = "dog's weight? "
b = "cat's weight? "
c = "bird's weight? "

a = str(a)
b = str(b)
c = str(c)

pet = str(input("what is your pet? "))
age = int(input("What is your "+ str(x) or str(y) or str(z)))
weight = float(input("What is your "+ str(a) or str(b) or str(c)))

age = age *52
weight = weight / 2.205

if pet == ("dog"):
    print (age)
    print (weight)
        
elif pet == ("cat"):
    print (age)
    print (weight)

elif pet == ("bird"):
    print (age)
    print (weight)
    
else:
    print ("That's an exotic animal!")

    
