file = open("other-file.txt", mode="r+")

print("Before edit: ")
print(file.read())
print("")

file.write("\nHello! I'm the python-file!")

print("After edit: ")
print(file.read())

file.close()