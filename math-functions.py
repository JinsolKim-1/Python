import math

gallons = 37.78
distance = -56.32

a = 4
b = 2
c = 6

print (round(gallons))
print (math.ceil(gallons))
print (math.floor(gallons))
print (abs(distance))
print (math.sqrt(gallons), " = " ,round(math.sqrt(gallons)), " Gallons", " or ",
       gallons*3.785, "=" ,round(gallons*3.785), " Liters")
print (math.pow(gallons,3), " = " ,round(math.pow(gallons,3)), " Gallons", " or ",
       math.pow(gallons,3)*3.785, "=",round(math.pow(gallons,3)*3.785), " Liters")

print (max(a,b,c))
print (min(a,b,c))