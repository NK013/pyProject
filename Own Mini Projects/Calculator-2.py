# loop
while True:

    # functions
    def divide(a, b):
        if b == 0:
            return "[!] Du kannst nicht mit 0 dividieren!"
        else:
            return a / b

    # operation list
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": divide,
        "^": lambda a, b: a ** b,
    }

    # get selected operation
    selected_option = input("""[!] Bitte wähle eine der folgenden Optionen:

    '+': addieren
    '-': subtrahieren
    '*': multiplizieren
    '/': dividieren
    '^': quadrieren

[?] Was möchtest du tun? """)

    operation = operations.get(selected_option)

    # calculation
    if operation:
        a = int(input("[!] Bitte gib die erste Zahl deiner Rechnung ein: "))
        b = int(input("[!] Bitte gib die zweite Zahl deiner Rechnung ein: "))

        print(f"[i] Ergebnis: {operation(a, b)}")
    else:
        print("[!] Fehlerhafte Auswahl!")

    # stop/restart programm
    ans = input("[?] Möchtest du weiter rechnen? (Ja/Nein) ").strip().lower()

    if ans:
        if ans == "nein" or ans == "n" or ans == "no":
            print("[✗] Programm wird gestoppt...")
            break
        elif ans == "ja" or ans == "j" or ans == "y" or ans == "yes" or ans == "c" or ans == "continue":
            print("[✓] Programm wird gestartet...")
            continue
        else:
            print("[!] Fehlerhafte Eingabe!")
            print("[✗] Programm wird gestoppt...")
            break
    else:
        print("[!] Fehlerhafte Eingabe!")
        print("[✗] Programm wird gestoppt...")
        break