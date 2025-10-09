# 1 ####################################################################

def wechsel(*args):
    if len(args) < 2:
        return "Zu wenige Argumente"
    
    x = 0
    counter = 0

    for i in args:
        if type(i) != int:
            return "Alle Argumente müssen Ganzzahlen sein"
        x = (x + i) if counter % 2 == 0 else (x - i)
        counter += 1

    return x

print(wechsel(1,2,3,4,5)) 

print()

# 2 ####################################################################
def ist_null(zahl):
    if type(zahl) != int:
        return "Alle Argumente müssen Ganzzahlen sein"
    
    return "Wahr" if bool(zahl) == 0 else "Falsch"

print(ist_null(10))
print(ist_null(0))
print(ist_null(1))

print()

# 3 ####################################################################
def komplex_betrag(zahl):
    if type(zahl) != complex:
        return "Das Argument muss eine komplexe Zahl sein"
    
    return (zahl.real**2 + zahl.imag**2)

print(komplex_betrag(3 + 4j))

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
    
print(unendl_schritte(1.5))
print(unendl_schritte(3.5))

print()

# 5 ####################################################################
def list_halbier(liste):
    if type(liste) != list:
        return "Das Argument muss eine Liste sein"
    
    length = len(liste)

    if length < 2:
        return "Die Liste muss mindestens 2 Zahlen enthalten"
    
    length_half = int(length/2)
    

    a = liste[:length_half] if length % 2 == 0 else liste[:length_half+1]
    b = liste[length_half:] if length % 2 == 0 else liste[length_half+1:]
  
    return [a,b]

print(list_halbier([1,2,3,4,5,6,7,8,9,10]))
print(list_halbier([1,2,3,4,5,6,7,8,9]))
print(list_halbier([1,2,3,4,5,6,7,8]))
print(list_halbier([1,2,3,4,5,6,7]))
print(list_halbier([1,2,3,4,5,6]))
print(list_halbier([1,2,3,4,5]))