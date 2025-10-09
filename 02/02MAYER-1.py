REFERENZ = "Referenz"
referenz_lower = REFERENZ.casefold()

while True:
    eingabe = input("Bitte ein Wort eingeben (oder 'exit' zum Beenden): ")
    eingabe_lower = eingabe.casefold()

    if eingabe.lower() == 'exit':
        print("Programm wird beendet.")
        break

    if eingabe_lower > referenz_lower:
        print(f"{eingabe} ist groesser als {REFERENZ}.")
    elif eingabe_lower < referenz_lower:
        print(f"{eingabe} ist kleiner als {REFERENZ}.")
    else:
        print(f"{eingabe} ist gleich {REFERENZ}.")