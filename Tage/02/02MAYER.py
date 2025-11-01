
class bcolors:
    HEADER     = "\033[95m"
    OKBLUE     = "\033[94m"
    OKGREEN    = "\033[92m"
    WARNING    = "\033[93m"
    FAIL       = "\033[91m"
    BOLD       = "\033[1m"
    UNDERLINE  = "\033[4m"
    ENDC       = "\033[0m"

    # Allgemeine Methode zum Formatieren von Meldungen mit einer bestimmten Farbe und zum automatischen Anhängen von ENDC
    @staticmethod
    def format_message(message, color):
        return f'{color}{message}{bcolors.ENDC}'

    # Convenience-Methoden für einzelne farbige Meldungen
    @staticmethod
    def colored(message, color):
        return bcolors.format_message(message, color)

    @staticmethod
    def warning(message):
        return bcolors.format_message(message, bcolors.WARNING)
    
    @staticmethod
    def ok(message):
        return bcolors.format_message(message, bcolors.OKGREEN)
    
    @staticmethod
    def okblue(message):
        return bcolors.format_message(message, bcolors.OKBLUE)
    
    @staticmethod
    def fail(message):
        return bcolors.format_message(message, bcolors.FAIL)


def zeichenkettenvergleich():
    print(bcolors.ok("Zeichenkettenvergleich wird ausgeführt."))
    REFERENZ = "Referenz"
    referenz_lower = REFERENZ.casefold()

    while True:
        eingabe = input("Bitte ein Wort eingeben (oder 'exit' zum Beenden): ")
        eingabe_lower = eingabe.casefold()

        if eingabe.lower() == 'exit':
            print(bcolors.warning("Das Programm Zeichenkettenvergleich wird beendet."))
            break

        if eingabe_lower > referenz_lower:
            print(bcolors.okblue(f"{eingabe} ist groesser als {REFERENZ}."))
        elif eingabe_lower < referenz_lower:
            print(bcolors.okblue(f"{eingabe} ist kleiner als {REFERENZ}."))
        else:
            print(bcolors.okblue(f"{eingabe} ist gleich {REFERENZ}."))

def verdoppeln():
    print(bcolors.ok("Verdoppeln bis 999 wird ausgeführt."))

    while True:
        eingabe = input("Bitte eine Zahl eingeben (oder exit zum Beenden): ")

        if eingabe == 'exit':
            print(bcolors.warning("Das Programm Verdoppeln wird beendet."))
            break

        try:
            zahl = int(eingabe)
        except ValueError:
            print(bcolors.fail("Das war keine gültige Eingabe!"))
            continue

        if zahl <= 0:
            print(bcolors.fail("Die Zahl muss größer als 0 sein!"))
            continue
        
        while zahl <= 999 / 2:
            zahl *= 2
            print(bcolors.okblue(f"Verdoppelte Zahl: {zahl}"))

def teiler():
    print(bcolors.ok("Teiler finden wird ausgeführt."))

    while True:
        eingabe = input("Bitte eine Zahl eingeben (oder exit zum Beenden): ")

        if eingabe == 'exit':
            print(bcolors.warning("Das Programm Teiler finden wird beendet."))
            break

        try:
            zahl = int(eingabe)
        except ValueError:
            print(bcolors.fail("Das war keine gültige Eingabe!"))
            continue

        if zahl <= 0:
            print(bcolors.fail("Die Zahl muss größer als 0 sein!"))
            continue

        for x in range(1, zahl + 1):
            print(bcolors.okblue(f"Teiler (for) {x}: "), end="")
            print(bcolors.okblue(print_teiler_for(x)))

        i = 1
        while i <= zahl:
            print(bcolors.okblue(f"Teiler (while) {i}: "), end="")
            print(bcolors.okblue(print_teiler_while(i)))
            i += 1 


def print_teiler_for(zahl):
    print_string = ""
    j = 0
    for x in range(1, zahl + 1):
        if zahl % x == 0:
            print_string += f"{x}, "
            j += 1
    print_string = print_string[:-2]
    if j <=2:
        print_string += "   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   Primzahl"

    return print_string


def print_teiler_while(zahl):
    print_string = ""
    i = 1
    j = 0
    while i <= zahl:
        if zahl % i == 0:
            print_string += f"{i}, "
            j += 1
        i += 1
    print_string = print_string[:-2]
    if j <=2:
        print_string += "   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   Primzahl"
    
    return print_string


def main():

    while True:
        print("######################################")
        print("Bitte waehle eine der folgenden Optionen:")
        
        print("  1 - Zeichenkettenvergleich")
        print("  2 - Verdopppeln bis 999")
        print("  3 - Teiler finden")
        auswahl = input("Deine Wahl (oder exit zum Beenden): ")


        if auswahl == 'exit':
            print(bcolors.warning("Das Programm wird beendet."))
            break

        try:
            zahl = int(auswahl)
        except ValueError:
            print(bcolors.fail("Ungültige Eingabe."))
            continue

        if zahl == 1:
            zeichenkettenvergleich()
        elif zahl == 2:
            verdoppeln()
        elif zahl == 3:
            teiler()
        else:
            print(bcolors.fail("Ungültige Eingabe."))
            continue

if __name__ == "__main__":
    main()