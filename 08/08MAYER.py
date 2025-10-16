# 1 #############################################

def mein_index(wort, liste: list):
    try:
        return liste.index(wort)
    except:
        return None

liste = ["hund","katze","maus","elefant"]

# print(mein_index("katze",liste))


# 2 #############################################

def ergebnisse(a=0, b=1):
    ergebnis = []

    if not all(isinstance(x, (int, float)) for x in (a, b)):
        return "Wrong Type - parameters must be int or float"
    if b == 0:
        return "The second parameter is not allowed to be 0"


    for calc in "+-*/":
        try:
            zw = (calc, round(eval(str(a) + calc + str(b)),3))
            ergebnis.append(zw)
        except Exception as e:
            print(e.args[0])
            return None

    return tuple(ergebnis)


print(ergebnisse(100,2.7))

print()
# 2 #############################################

def quersumme(string: str):
    if not isinstance(string, str):
        return "Must be a string."
    
    ergebnis = 0
    for char in string:
        try:
            char = ord(char)
            ergebnis += char
        except Exception as e:
            return e.args[0]
            
    return ergebnis

print(quersumme("12a[]"))

print()

# 3 #############################################

fischarten = [
    "Barsch", "Hecht", "Karpfen", "Forelle", "Aal", "Zander", "Lachs", "Dorsch", "Wels", "Rotfeder", "Blaubarsch", "Köhler", "Schleie", "Barschart", "Kaiserfisch", "Makrele", "Hering", "Seelachs", "Scholle", "Flunder", "Seebrasse", "Äsche", "Gründling", "Brachse", "Döbel", "Elritze", "Flussbarsch", "Quappe", "Rapfen", "Sonnenbarsch", "Stint", "Stör", "Trüsche", "Wolfsbarsch", "Aalmutter", "Buntbarsch", "Katzenhai", "Makrele", "Muräne", "Fischotter", "Rochen", "Sandaal", "Stör", "Torpedofisch", "Trumpf", "Weißfisch", "Zackenbarsch", "Zitterrochen", "Zunge", "Zwergwels"
]

print(fischarten, end="\n\n")  
fischarten.sort(key=quersumme, reverse=True)
print(fischarten, end="\n\n")  