#!/usr/bin/python3
Student = __import__('10-student').Student

student1 = Student("john", "jon", 23)
student2 = Student("has", "kan", 45)

jsttud1 = student1.to_json()
jsttud2 = student2.to_json(['first_name', 'age'])

print(jsttud1)
print(jsttud2)
