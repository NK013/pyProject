# map method
def cube(number):
    return number ** 3

numbers = [1, 2, 3, 4, 5]
cubed_numbers = map(cube, numbers)

for number in cubed_numbers:
    print(number)


# filter method
def is_even(number):
    return number % 2 == 0

numbers = [1, 56, 3, 5, 24, 19, 88, 37]
even_numbers = filter(is_even, numbers)