w = bool(23) # Wahr
x = bool('') # Falsch
y = bool(' ')# Wahr
z = bool([False])   # Falsch
v = bool(None) # Falsch

print(w, x, y, z, v)

# x = None + 1 # TypeError 

# prüft auf Unicode Werte
x = ("A" > "!") # True
x = ("A" > "a") # False
x = ("@" > "a") # False
x = ("诶" > "a")    # True, da Unicode Wert von 诶 größer als der von a
x = ("诶xxxx" > "a") # True, da Unicode Wert von 诶 größer als der von a

for i in range(-2):
    print(i)

print()

# Listen
list = ["a", 27, True, "ende"]
print(list[1])
print(type(list[1]))

print(list)
list[2:2] = [8, 8, 8, 8] # fügt 4x 8 an Index 2 ein
print(list)

# Teil der Liste / Slicing
print(list[1:3]) # Teil der Liste von Index 1 bis 2
print(list[2:-1]) # Teil der Liste von Index 2 bis vorletztes Element
print(list[-3:-1]) # Teil der Liste von drittletztes Element bis vorletztes Element

list2 = list
list3 = list


print(list2)
print(list3)

print()

list2[0] = "geändert"
print(list2)
print(list3) # list3 ist auch geändert, da list2 und list3 auf die gleiche Liste zeigen
print(list) # list ist auch geändert, da list2 und list3 auf die gleiche Liste zeigen

print()

# Lösung: list kopieren
list2 = list.copy()
list3 = list[:]
list2[0] = "neu"
print(list2)
print(list3)
print(list)

print()


# Übung: Erstelle eine Liste mit den Zahlen von 1 bis 12
# Erstelle dann die folgenden Teillisten durch Slicing:
list_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

list_x1a = list_x[4:7]
print(list_x1a)
list_x1b = list_x[3:9][1:-2]
print(list_x1b)

print()

list_x2a = list_x[-2:-9:-3]
print(list_x2a)
list_x2b = list_x[-2:3:-3]
print(list_x2b)

print()

list_x3a = list_x[0:0]
print(list_x3a)
list_x3b = list_x[:0]
print(list_x3b)
list_x3c = list_x[555:666] # leere Liste, da Index out of range
print(list_x3c)
list_x3d = list_x[1:555:-1] # leere Liste, da Schritt -1 und Startindex < Endindex
print(list_x3d)

print()

list_x4 = list_x[:-1] # alle bis auf das letzte Element
print(list_x4)

print()

list_x5a = list_x[-2::-2]
print(list_x5a)
list_x5b = list_x[10::-2]
print(list_x5b)

list_x5c = list_x[-2:0:-2]  # Achtung, das Element an Index 0 wird nicht mitgenommen. Um es mitzunehmen, muss der Endindex -1 oder leer sein.
print(list_x5c)

print()

list_x6 = list_x[15::-5]
print(list_x6)

print()


list_initial = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

list_x = list_initial.copy()
x = list_x

x[7:7] = [8, 8]
print(x)
print(list_x) # list_x ist auch geändert, da y auf die gleiche Liste zeigt
print(list_initial) 

print()

list_y = list_initial.copy()
y = list_y

y[1:1] = [2, 2]
print(y)
print(list_y) # list_x ist auch geändert, da y auf die gleiche Liste zeigt
print(list_initial)

print()

def multimult(*args):
    if len(args) == 0:
        return
    result = 1
    for num in args:
        result *= num
    return result

print(multimult())
print(multimult(1, 2, 3, 4, 5))

print()

def multiadd(*args):
    if len(args) == 0:
        return
    result = 0
    for num in args:
        result += num
    return result

print(multiadd())
print(multiadd(1, 2, 3, 4, 5))

print()

def x(liste, wert=True):
    if wert:
        return max(max(liste), len(liste))
    else:
        return min(min(liste), len(liste))

    
print(x([1, 2, 3, 4, 5, 4, 2, 1]))
print(x([1, 2, 3, 4, 30, 4, 2, 1]))
print(x([1, 2, 3, 4, 5, 4, 3, 2, 1], False))

print()

