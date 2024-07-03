names = ("hanz", "günter", "richard")
ages = (20, 25, 30)

people = []

for name, age in zip(names, ages):
    person_data = (name.title(), age)
    people.append(person_data)

print(people)