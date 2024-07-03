from collections import namedtuple

Student = namedtuple("Student", ["name", "age"])

student = Student(name="Hanz", age=16)
print(f"Hello, {student.name} ({student.age})!")
