#dictionary

num = int(input("Input number of students: "))
w = []
sum_age = 0
sum_grade = 0

for i in range(num):
    student ={}
    student['name'] = str(input("Student's name: "))
    student['age'] = int(input("Student's age: "))
    student['grade'] = float(input("Student's grade: "))
    w.append(student)
    sum_age += student['age']
    sum_grade += student['grade']

average = sum_age / num 
average2= sum_grade / num  
print(w)     
print({"average_age: ": average , "average_grade: ":average2})