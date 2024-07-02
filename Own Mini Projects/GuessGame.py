tries = 0

print("Tipp: Die Zahl ist zwischen 1 und 100!")

while True:
    num = 47
    guess = int(input("Your guess: "))

    if guess is num:
        tries = tries + 1
        print("You won! (Tries: " + str(tries) + ")")
        break
    elif guess < num:
        print("You guessed number is too low!")
        tries = tries + 1
    elif guess > num:
        print("You guessed number is too high!")
        tries = tries + 1
    else:
        print("Error! Invalid guess!")