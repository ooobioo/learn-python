
liste = ["eins", "zwei", "drei"]
teilsymbol = "---"

liste2 = teilsymbol.join(liste)

print(liste2)

###################

print([[c for c in range(r)] for r in range(3) if r!=0]) # [[0], [0,1]]
### print([c for c in range([1,2])]) # Error


print("this" and "that", sep=" ")

x = "this" and "that"
y = "this" and "that" and "test"
z = "this" and True

print(x)
print(y)
print(z)

print()
############

vorname = ()
nachname = 0

name_test_1 = vorname and nachname
name_test_2 = bool(vorname and nachname)

print(name_test_1)
print(name_test_2)

name_test_1 = vorname or nachname
name_test_2 = bool(vorname or nachname)

print(name_test_1)
print(name_test_2)
print()

###############


vorname = "thomas"

name_test_1 = vorname and nachname
name_test_2 = bool(vorname and nachname)

print(name_test_1)
print(name_test_2)
name_test_1 = vorname or nachname
name_test_2 = bool(vorname or nachname)

print(name_test_1)
print(name_test_2)
print()

###############

nachname = "mayer"

name_test_1 = vorname and nachname
name_test_2 = bool(vorname and nachname)

print(name_test_1)
print(name_test_2)
name_test_1 = vorname or nachname
name_test_2 = bool(vorname or nachname)

print(name_test_1)
print(name_test_2)
print()


# Bei and
# wahr > wird der Wert des letzten wahren Ausdrucks zurückgegeben
# falsch > wird der Wert des ersten falschen Ausdrucks zurückgegeben

# Bei or 
# wahr > wird der Wert des ersten wahren Ausdrucks zurückgegeben
# falsch > wird der Wert des letzten falschen Ausdrucks zurückgegeben


# In Python werden folgende Werte als False interpretiert (sie sind also „falsy“), wenn sie in einem booleschen Kontext geprüft werden:

# False (der boolesche Wert selbst)
# None
# 0 (und alle anderen numerischen Nullen, z.B. 0.0, 0j)
# Leere Sequenzen: "" (leerer String), [] (leere Liste), () (leeres Tupel)
# Leere Mengen und Mappings: {} (leeres Dictionary), set(), frozenset()
# Objekte und Instanzen, deren eigene __bool__() oder __len__() Methode einen Wert ergibt, der als false gilt (z.B. __len__() == 0).​
# Alle anderen Werte werden in booleschem Kontext als True gewertet. Das ist besonders beim Einsatz in Bedingungen wie if oder while hilfreich.​


################


# Entpacken / Unpacking von Tupels

tup = (1,2,3,4,5,6,7)

x = tup[0]
y = tup[1]
rest = tup[2:]
print(x, y, rest, sep=" | ")

t1, t2, *rest = tup
rest = tuple(rest)
print(t1, t2, rest, sep=" | ")


x1, *rest, xn = tup
rest = tuple(rest)
print(x1, rest, xn, sep=" | ")



tup = ([], (), [])
tup[0].append(3)
tup[0].append(4)
tup[2].append(123)

print(tup)


#####

# funktionen

# nur list
# sort, append, del, pop, remove

# beide
# max(), len(), min(), index

print(len(tup))
print(max((1,2,304,5)))
print([2,2,3]>[1,2,3,7]) # die beiden ersten elemente werden verglichen

tup2 = (1,2,3,4,2,5,6,2)
liste = [1,2,3,4,5]

print(tup2.index(3))
print(liste.index(3))
print(liste.count(3))
print(tup2.count(2))
print(tup2.count(2))


teilsymbol = " ---- "
liste = ["string1", "string2", "string3"]
liste2 = [" --- ", "string1", "string2", "string3"]
liste3 = [[" --- ", " || "], "string1", "string2", "string3"]

print(teilsymbol.join(liste))
print(liste3[0][0].join(liste3[1:]))
print(liste3[0][1].join(liste3[1:]))


print()

# Map #############

def double(n):
    return n * 2

numbers = [5,6,7,8,9]
result = map(double,numbers)
print(result)
print(list(result))


# Filter #############

def is_even(n):
    return n % 2 == 0

numbers = [1,2,3,4,5,6,7,8,9]
even_numbers = filter(is_even,numbers)
print(even_numbers)
print(list(even_numbers))

print()

def ab(z):
    return z < "k"

s = "asbldefcmfjkopblycefzx"
print("".join(filter(ab,s)))

print()

# ein tupel mit nur einem element sieht so aus (1,) - ohne das komma ist es kein tuple sondern ein int

k = (1,)
print(type(k))
k = (1)
print(type(k))

print()

#####################


# Dictionaries

di = {
    "parenthesis" : "runde Klammern",
    "brackets" : "eckige Klammern",
    "curly braces" : "geschweifte Klammern"
}

di2 = {
    1 : "huuh",
    2 : "hooh"
}

def schreib(dict):
    for key, value in dict.items(): print(key, " / " ,value)
    print()
    return

schreib(di)

di["nix"] = "nix Klammer"

schreib(di)

del di["nix"]

schreib(di)

#########################

l1 = [1, 2, 3, 4]
l2 = ["A", "B", "C", "D"]



def neues_dict1(lst1, lst2):
    di = {}
    for index, i in enumerate(lst1):
        di[i] = lst2[index]
    return di

def neues_dict2(lst1, lst2):
    di = {}
    i=0
    while i < len(lst1):
        di[lst1[i]] = lst2[i]
        i+=1
    return di



my_dictionary = neues_dict1(l1, l2)
print("Dict: ", my_dictionary)
print()
my_dictionary = neues_dict2(l1, l2)
print("Dict: ", my_dictionary)


x = ('apple', 'banana', 'cherry')
y = enumerate(x)

print(list(y))

print()


# Zip

l1 = [1, 2, 3, 4]
l2 = ["A", "B", "C", "D", "E", "F"]

l3 = [1, 12, 13, 14]
l4 = ["AA", "BB", "CC", "DD", "EE", "FF"]

d1 = dict(zip(l1,l2))
d2 = dict(zip(l3,l4))

print(d1)

# auf schlüssel prüfen

print(1 in d1)
print(666 in d1)


# dictionaries vereinigen
print()

# wird überschrieben wenn ein schlüssel mehrmals verwendet wird
d3 = d1 | d2

print(d3)


########### Aufgabe


l1 = ["a","b","c","d","e","f","ax","bxxxxx","cx","dx","ex","fx","axx","bxx","cxx","dxx","exx","fxx"]

def dict_kompr(lst):
    dict = {x:len(x) for x in lst}
    return dict

print(dict_kompr(l1))