# args
def multigreet(*args):
    for name in args:
        print(f"Hello, {name}!")

multigreet("Rolf", "Bob", "Anne")


# kwargs
def pretty_print(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

pretty_print(title="The Matrix", director="Wachowski", year=1999)


# other uses for * and **
nums = [1, 2, 3, 4, 5]

print(*nums, sep=" • ")
