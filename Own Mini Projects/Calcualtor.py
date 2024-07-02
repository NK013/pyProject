while True:

    num1 = float(input("Bitte gib die erste Zahl diener Rechung ein: "))
    num2 = float(input("Bitte gib die zweite Zahl diener Rechung ein: "))
    operator = input("Was möchtest du rechnen? (+|-|*|/): ")

    sNum1 = str(num1)
    sNum2 = str(num2)

    res = 0

    if operator is "+":
        res = num1 + num2
        sRes = str(res)
        print(f"Deine Rechnung: {sNum1} + {sNum2}")
        print(f"Dein Ergebnis: {sRes}")
    elif operator is "-":
        es = num1 - num2
        sRes = str(res)
        print(f"Deine Rechnung: {sNum1} - {sNum2}")
        print(f"Dein Ergebnis: {sRes}")
    elif operator is "*":
        res = num1 * num2
        sRes = str(res)
        print(f"Deine Rechnung: {sNum1} * {sNum2}")
        print(f"Dein Ergebnis: {sRes}")
    elif operator is "/":
        res = num1 / num2
        sRes = str(res)
        print(f"Deine Rechnung: {sNum1} / {sNum2}")
        print(f"Dein Ergebnis: {sRes}")
    else:
        print("Error! Operater is invalid!")

    ans = input("Möchtest du erneut rechnen? (Ja|Nein): ")

    if ans == "Nein" or ans == "nein" or ans == "no" or ans == "n":
        print("Programm wird beendet...")
        break
    else:
        print("Programm wird neugestartet...")