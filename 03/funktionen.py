def antwort(name, v="ist", d="heute", aw="da"):
    print(name, v, d, aw)

antwort("Peter")
antwort("Peter", "war")
antwort("Peter", "war", "heute morgen", "dort")
antwort("Peter", aw="weg")
antwort("Peter", d="morgen", aw="hier")



def multiplizieren(x, y=2):
    return x * y

def addieren(a, b, c=3, d=4):
    return a + b + c + d


print(multiplizieren(3))
print(multiplizieren(3, 3))

print(addieren(1, 2))
print(addieren(1, 2, 5))
print(addieren(1, 2, d=5))
# FEHLER ---> print(addieren(1, 2, d=5, 6)) 

print()

def mein_print(s, *args):
    print(s)
    # args ist ein Tupel und kann iteriert werden
    for a in args:
        print(a, end=" ")
    print()

mein_print("Hallo")
mein_print("Hallo", 1, 2, 3, 4, 5)
mein_print("Hallo", "Peter", "Paul", "Mary")

print()

def print_type(*args):
    for a in args:
        if type (a) == int:
            print(a, "ist eine Ganzzahl")
        print(a, type(a))

print_type(1, 1.5, "Hallo", [1, 2, 3], (1, 2), {1, 2}, None, True, False)

print()


