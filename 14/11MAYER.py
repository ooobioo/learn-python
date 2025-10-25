##########################################################
print("\n### 1 ######################################################")

class MeinDict(dict):
    def wieviele_typ(self, typ):
        anzahl_keys = sum(1 for k in self.keys() if isinstance(k, typ))
        anzahl_values = sum(1 for v in self.values() if isinstance(v, typ))
        return (anzahl_keys, anzahl_values)
    
    def wieviele_int(self):
        anzahl_keys = (sum(1 for k in self.keys() if(isinstance(k, int))))
        anzahl_values = (sum(1 for v in self.values() if(isinstance(v, int))))
        return (anzahl_keys, anzahl_values)
    
    def wieviele_leere_strings(self):
        anzahl = sum(1 for v in self.values() if(v == ""))
        return anzahl


    
daten = MeinDict({1: "Hallo", "x": 3.14, 2: 42, "y": "Welt", "xxx": ""})

print(daten.wieviele_typ(int))
print(daten.wieviele_typ(str))
print(daten.wieviele_typ(float))

print("Integer", daten.wieviele_int())
print("Leere Strings:", daten.wieviele_leere_strings())


##########################################################
print("\n### 2 ######################################################")

class MyList(list):
    def __str__(self):
        return str(self[::-1])
    
list1 = MyList()
list1.extend([1,2,3,4,5])

print(list1)


##########################################################
print("\n### 3 ######################################################")

def zeichen(s, f):
    menge = set()
    menge.update(char for char in s if(f(char)))
    #   for char in s:
    #       if(f(char)):
    #           menge.add(char)
    return frozenset(menge)

def is_in_alphabet(char):
    return char.lower() in "abcdefghijklmnopqrstuvwxyz" 

string = "Schreiben Sie eine Funktion zeichen( s, f ), die"

print(zeichen(string, is_in_alphabet))


##########################################################
print("\n### 4 ######################################################")

def f(a, *args, **kwargs):
    s = (f"a ist {a}\n")

    if args:
        s += " weitere Argumente sind: "
        for value in args:
            s += f"{value}, "
        s = s[:-2] + "\n"

    if kwargs:
        s += " Schlüsselwortparameter sind: "
        for name, value in kwargs.items():
            s += f"{name}={value}, "
        s = s[:-2] + "\n"

    return s
    
    
print(f(5, 6, 7, k=4, z=3))  
print(f(5, 6, 7))
print(f(5, k=4, z=3))  
