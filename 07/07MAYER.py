# plattmachen

liste = [[1,2],3,[4,[5,6]],7]

def plattmachen1(l: list):
    ergebnis = []
    def machplatt(l: list):
        nonlocal ergebnis
        for el in l:
            if type(el) == list:
                machplatt(el)
            else:
                ergebnis.append(el)
    machplatt(l)
    return ergebnis

print("Platt1:", plattmachen1(liste))


def plattmachen2(l: list):
    ergebnis = []
    for el in l:
        if type(el) == list:
            ergebnis.extend(plattmachen2(el))
        else:
            ergebnis.append(el)
    return ergebnis

print("Platt2:", plattmachen2(liste))

print()
# 1 #############################################

def mein_index(wort, liste: list):
    try:
        return liste.index(wort)
    except:
        return None

liste = ["hund","katze","maus","elefant"]

print("Index:", mein_index("katze",liste))

print()
# 2 #############################################

def ergebnisse(a=0, b=1):
    if not all(isinstance(x, (int, float)) for x in (a, b)):
        raise TypeError("Parameters must be integer or float")
    
    results = []
    for operator in ["+", "-", "*", "/", "**", "%", "//"]:
        try:
            result = (operator, round(eval(str(a) + operator + str(b)),3))
            results.append(result)
        except Exception as e:
            results.append((operator, f"{type(e).__name__}: {str(e)}"))

    return tuple(results)

print("Ergebnisse:",ergebnisse(19,-5))
# print("Ergebnisse:",ergebnisse(11,"x"))

print()
# 3 #############################################

def quersumme(string: str):
    if not isinstance(string, str):
        raise TypeError("Parameter must be a string")
    
    ergebnis = 0
    for char in string:
        try:
            ergebnis += ord(char)
        except Exception as e:
            return e.args[0]
            
    return ergebnis

print("Quersumme:",quersumme("12a[]"))

print()
# 4 #############################################

fischarten = [
    "Barsch", "Hecht", "Karpfen", "Forelle", "Aal", "Zander", "Lachs", "Dorsch", "Wels", "Rotfeder", "Blaubarsch", "Köhler", "Schleie", "Barschart", "Kaiserfisch", "Makrele", "Hering", "Seelachs", "Scholle", "Flunder", "Seebrasse", "Äsche", "Gründling", "Brachse", "Döbel", "Elritze", "Flussbarsch", "Quappe", "Rapfen", "Sonnenbarsch", "Stint", "Stör", "Trüsche", "Wolfsbarsch", "Aalmutter", "Buntbarsch", "Katzenhai", "Makrele", "Muräne", "Fischotter", "Rochen", "Sandaal", "Stör", "Torpedofisch", "Trumpf", "Weißfisch", "Zackenbarsch", "Zitterrochen", "Zunge", "Zwergwels"
]

print(fischarten, end="\n\n")
fischarten.sort(key=quersumme, reverse=True)
print(fischarten, end="\n\n")
