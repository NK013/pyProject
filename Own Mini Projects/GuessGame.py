from random import randint

tries = 0
num = randint(1, 100)

print("Guess the number between 1 and 100!")

while True:
    strGuess = input("Your guess: ").strip()
    guess = int(strGuess)

    if not strGuess:
        print("Invalid input!")

    if guess == num:
        tries = tries + 1
        print("You won! (Tries: " + str(tries) + ")")
        break
    elif guess < num:
        print("Your guessed number is too low!")
        tries = tries + 1
    elif guess > num:
        print("Your guessed number is too high!")
        tries = tries + 1