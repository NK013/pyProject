#functions in variables
def add(a, b):
    print(a + b)

adder = add
del add

adder(5, 4)


# sort
numbers = [5, 2, 9, 1, 6]
highest = max(numbers)

print(highest)

# lambda
print(lambda a, b: a-b)