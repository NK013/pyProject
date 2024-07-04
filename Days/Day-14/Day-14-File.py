file = open("Days/Day-14/other-file.txt", mode="r+")

print()
print("Before edit: ")
print(file.read())
print()

file.write("\nHello! I'm the python-file!")
file.close()

file = open("Days/Day-14/other-file.txt", mode="r")

print("After edit: ")
print(file.read())
print()

file.close()
