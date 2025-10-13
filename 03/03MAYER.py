# 1 ####################################################################
def wechsel(*args):
    if len(args) < 2:
        return "Zu wenige Argumente"
    
    x = 0
    # counter = 0
    flip = True

    for i in args:
        if type(i) != int:
            return "Alle Argumente müssen Ganzzahlen sein"
        # x = (x + i) if counter % 2 == 0 else (x - i)
        x = (x + i) if flip else (x - i)
        # counter += 1
        flip = not flip

    return x

print("Im Wechsel subtrahiert und addiert: ", wechsel(1,2,3,4,5)) 
print("Im Wechsel subtrahiert und addiert: ", wechsel(1,2,3,4,5,6)) 
print("Im Wechsel subtrahiert und addiert: ", wechsel(1,2,3,4,5,6,7)) 
print("Im Wechsel subtrahiert und addiert: ", wechsel(1,2,3,4,5,6,7,8)) 

print()

# 2 ####################################################################
def ist_null(zahl):
    if type(zahl) != int:
        return "Alle Argumente müssen Ganzzahlen sein"
    
    return "Wahr" if bool(zahl) == 0 else "Falsch"

print("10 ist null: ", ist_null(10))
print("0 ist null: ", ist_null(0))
print("1 ist null: ", ist_null(1))
print("8 ist null: ", ist_null(8))

print()

# 3 ####################################################################
def komplex_betrag(zahl):
    if type(zahl) != complex:
        return "Das Argument muss eine komplexe Zahl sein"
    
    return (zahl.real**2 + zahl.imag**2)

print("Betrag: ",komplex_betrag(3 + 4j))

print()

# 4 ####################################################################
def unendl_schritte(zahl):
    if type(zahl) != float:
        return "Das Argument muss eine Kommazahl sein"
    if zahl <= 1:
        return "Die Zahl muss größer als 1 sein"
    
    x = zahl
    counter = 0
    inf = float('inf')

    while x < inf:
        x *= zahl
        counter += 1
    else:
        return counter
    
print("Schritte bis unendlich (1,5): ", unendl_schritte(1.5))
print("Schritte bis unendlich (3,5): ", unendl_schritte(3.5))
print("Schritte bis unendlich (3,0): ", unendl_schritte(3.0))

print()

# 5 ####################################################################
def list_halbier(liste):
    if type(liste) != list:
        return "Das Argument muss eine Liste sein"
    
    length = len(liste)

    if length < 2:
        return "Die Liste muss mindestens 2 Zahlen enthalten"
    
    # Division
    # / gibt immer ein float zurück 4/2 → 2.0
    # // gibt ein int zurück außer mindestens ein Operand ist schon float
    # / erhält den Dezimalanteil
    # // rundet ab („in Richtung -∞“), also bei negativen Zahlen weiter nach unten: -5//2 ergibt -3, nicht -2

    if(length % 2 == 0):
        length_half = length//2
    else:
        length_half = length//2 + 1
      
    return [liste[:length_half], liste[length_half:]]

print(list_halbier([1,2,3,4,5,6,7,8,9,10]))
print(list_halbier([1,2,3,4,5,6,7,8,9]))
print(list_halbier([1,2,3,4,5,6,7,8]))
print(list_halbier([1,2,3,4,5,6,7]))
print(list_halbier([1,2,3,4,5,6]))
print(list_halbier([1,2,3,4,5]))