numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]

numbers = [1, 2, 3, 4]
numbers.append(5)

if new_numbers == numbers:
    print("It's the same.")
else:
    print("It's not the same.")

num = input("Number: ")

if float(num) > 0:
    print("num is positive")
elif float(num) is 0:
    print("num is zero")
else:
    print("num is negative")