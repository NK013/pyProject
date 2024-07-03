try:
    number = int(input("Bitte gib eine ganze Zahl ein: "))
    print("Number is: " + str(number))
except ValueError:
    print("Das ist keine ganze Zahl!")