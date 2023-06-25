
x = int(input("How many number on First list:  "))
y = int(input("How many number on Second list: "))

list1 = [int(input("Enter a number for the first list: ")) for _ in range(x)]
list2 = [int(input("Enter a number for the second list: ")) for _ in range(y)]

def find_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection_set = set1.intersection(set2)
    return intersection_set

intersection_set = find_intersection(list1, list2)

print("Intersection: ", intersection_set)
    


    