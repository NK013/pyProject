numbers = [1, 2, 3, 4, 5]

try:
    print(numbers[10])
except LookupError as ex:
    print(f"Error: {ex}")

print()
print(" [ ----- Before error ----- ]")
print()

raise ValueError("Helooooooooo! I'm the error! :D")

print()
print(" [ ----- After error ----- ]")
print()