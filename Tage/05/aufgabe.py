liste = ["hallo", "du", "beautiful", "neuer", "python", "lerner", "!"]

def erstelle_ergebnis(strings):
    min_max = list(filter(lambda s: len(s) > 4, strings))
    laengen_liste = list(map(lambda s: len(s), min_max))
    laengen_string = "---".join(map(str, laengen_liste))
    return (laengen_liste, laengen_string)

def laengen(strings):
    # Filtere Strings mit Länge > 4
    gefilterte_strings = list(filter(lambda s: len(s) > 4, strings))
    # Mappe die Längen der gefilterten Strings
    laengen_liste = list(map(len, gefilterte_strings))
    # Erzeuge den String mit Längen, getrennt durch '---'
    laengen_string = '---'.join(map(str, laengen_liste))
    return (laengen_liste, laengen_string)

def oneliner(strings):
    return ( list(map(len, list(filter(lambda s: len(s) > 4, strings)) )), '---'.join(map(str, list(map(len, list(filter(lambda s: len(s) > 4, strings)))))))




print()
print(erstelle_ergebnis(liste))
print()
print(laengen(liste))
print()
print(oneliner(liste))

print()
filter_test = list(filter(lambda s: len(s), liste))
print(filter_test)