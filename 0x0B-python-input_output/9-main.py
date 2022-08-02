#!/usr/bin/python3
Student = __import__('9-student').Student

students = [Student("john", "goe", 23), Student("bob", "hal", 98)]

for student in students:
    jstud = student.to_json()
    print(type(jstud))
