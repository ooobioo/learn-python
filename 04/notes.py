list1 = [1, 2, 3] # erstellt eine liste im speicher
list2 = list1[:] # erstellt ein kopie der liste
list3 = list1 # zeiger auf list1

print(list2 is list1, list3 is list1 )

x = 4
y = 4
print(x is y) # beide variablen sind immutabel und zeiger auf den gleichen platz im speicher

print()

####################################
def min_max_diff(liste):

    print(liste)

    # kopie der liste erstellen unnd diese nach groesse sortieren
    # kopie = liste[:]
    # kopie.sort()

    # index des ersten und letzen elements der kopie in der original liste ermitteln und voneinander abziehen
    # spread = liste.index(kopie[-1]) - liste.index(kopie[0])

    max_wert = max(liste)
    min_wert = min(liste)

    spread = liste.index(max_wert) - liste.index(min_wert)

    # den betrag des spreads zurueckgeben
    return(abs(spread))


print(min_max_diff([1,2,3,4,5,6]))
print(min_max_diff([1,2,9,3,0,1,6]))
print(min_max_diff([1,2,9,3,0,100,6]))
print(min_max_diff([1,2,9,3,0,100,6,1000]))
print(min_max_diff([1,1,1,1,1]))

print()

# EINFUEGEN ###################################
liste = [1,2,3]

liste.append(4)
print(liste)

liste.extend([5,6])
print(liste)

liste.extend("abc")
print(liste)

liste.extend(["abc", "def"])
print(liste)

liste.insert(1, "A")
print(liste)

liste.insert(999, "A")
print(liste)

liste.insert(-999, "A")
print(liste)

print()
# LOESCHEN ###################################

# pop -> nach position loeschen
liste = [1,200,3]
print(liste)
geloescht = liste.pop(1)
print(geloescht)
print(liste)

print()
# remove -> nach wert loeschen
liste = [1, 200, 1, 3, 1]
print(liste)
geloescht = liste.remove(1)
print(liste)
geloescht = liste.remove(1)
print(liste)

print()
# reverse -> liste umdrehen
liste = [1, 200, 1, 3, 1]
print(liste)
liste.reverse()
print(liste)

print()
# AUFGABE ###########################
def remove_all(liste, wert):
    print(liste)
    
    # for element in liste:
    #     if element == wert:
    #         liste.remove(wert)
    
    while liste.count(wert):
        liste.remove(wert)
    
    return liste

print(remove_all([1,2,3,2,5], 2))
print(remove_all([1,2,3,2,5,2,3], 2))

print()
# SORT ###################################
liste = ["Peter", "Jan", "Bernd", "Katharina", "Ben"]
print(liste)
# hier werden nicht die srings verglichen, sondern der rueckgabewert von len
liste.sort(key=len)
print(liste)

liste.sort(key=len, reverse=True)
print(liste)

print()
# AUFGABE ###########################
liste = ["Bimm", "Bamm", "Bumm", "Bbmm"]
print(liste)

def hol_zweiten_buchstaben(string):
    return string[1]

liste.sort(key=hol_zweiten_buchstaben)
print(liste)
print()

####

liste = ["Bimm", "Bamm", "Bumm", "Bbmm"]
print(liste)

def zweiter_bst(li):
    li.sort(key=hol_zweiten_buchstaben)
    return li

print(zweiter_bst(liste))
print()

####

liste = ["Bimm", "Bamm", "Bumm", "Bbmm"]
print(liste)

def zweiter_bst(li):
    li.sort(key=lambda s: s[1])
    return li

print(zweiter_bst(liste))
print()

#####
print() 

liste = ["Bimm", "Bamm", "Bumm", "Bbmm"]
print(liste)

for paar in enumerate(liste):
    print(paar)

for index, wert in enumerate(liste):
    print(index, "|", wert)


print()
# AUFGABE ###########################

liste = [0,2,4,6,8,10]

def wert_erhoehen(li):
    print(li)
    for index, wert in enumerate(li):
        li[index] = wert + index
    return li

print(wert_erhoehen(liste))

print()
# AUFGABE ###########################

wortliste = ["Apfel", "Banane", "Katze", "Hund", "Haus", "Auto", "Tisch", "Stuhl", "Fenster", "Tür", "Garten", "Blume", "Sonne", "Mond", "Stern", "Wasser", "Feuer", "Erde", "Luft", "Baum", "Vogel", "Fisch", "Berg", "Fluss", "Stadt", "Dorf", "Buch", "Schule", "Straße", "Freund"]


def filter_buchstaben(liste, buchstabe):
    neueliste = []
    for wort in liste:
        if buchstabe in wort.lower():
            neueliste.append(wort)
    return neueliste

print(filter_buchstaben(wortliste, "a"))
print(filter_buchstaben(wortliste, "b"))
print(filter_buchstaben(wortliste, "c"))
print(filter_buchstaben(wortliste, "d"))
print(filter_buchstaben(wortliste, "e"))
print(filter_buchstaben(wortliste, "t"))
print(filter_buchstaben(wortliste, "ne"))


print()
# DELETE #######################################
li = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(li)
del li[:-4:3]
print(li)

print()
# TUPEL #######################################
tup = (1,2,3,4)
print(tup)

x1, x2, x3, x4 = tup
print(x2)

a,b = 10,20
a,b = b,a
print(a,b)

tup = (1,2,3,4,5,6,7,8,9)

x1, *x, x2 = tup
print(x1, x2, x)