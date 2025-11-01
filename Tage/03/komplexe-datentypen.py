# Komplexe Datentypen in Python

# Listen, Tupel, Mengen und Dictionaries sind komplexe Datentypen, die mehrere Werte speichern können.
# Sie sind sehr nützlich, um Daten zu organisieren und zu verwalten.

# Zeichenketten (Strings)
# Eine Zeichenkette (String) ist eine Folge von Zeichen
s = "Hallo Welt"
print(s)
print(type(s))
print(len(s)) # Länge des Strings
print(s[0]) # Erstes Zeichen
print(s[-1]) # Letztes Zeichen
print(s[0:5]) # Teilstring von Index 0 bis 4
print(s[6:]) # Teilstring von Index 6 bis Ende
print(s[:5]) # Teilstring von Anfang bis Index 4
print(s[::2]) # Jedes zweite Zeichen
print(s[::-1]) # String umgekehrt
print(s.lower()) # Kleinbuchstaben
print(s.upper()) # Großbuchstaben
print(s.replace("Welt", "Python")) # Ersetzt "Welt" durch "Python"
print(s.split(" ")) # Teilt den String an Leerzeichen in eine Liste
print("Hallo" in s) # Prüft, ob "Hallo" in s enthalten ist
print("Python" in s) # Prüft, ob "Python" in s enthalten ist
print(s + " - Wie geht's?") # Konkatenation
print(s * 3) # Wiederholung
print(f"{s} - Wie geht's?") # f-String
print("Hallo" + " " + "Welt") # Konkatenation mit Leerzeichen
print("Hallo", "Welt") # print mit Leerzeichen
print("Hallo" + str(42)) # Konkatenation mit Zahl (Zahl muss in String umgewandelt werden)
print("Hallo" + str(3.14)) # Konkatenation mit Zahl (Zahl muss in String umgewandelt werden)
print("Hallo" + str(True)) # Konkatenation mit Bool (Bool muss in String umgewandelt werden)
print("Hallo" + str(None)) # Konkatenation mit None (None muss in String umgewandelt werden)
print("Hallo" + str([1, 2, 3])) # Konkatenation mit Liste (Liste muss in String umgewandelt werden)
print("Hallo" + str((1, 2, 3))) # Konkatenation mit Tupel (Tupel muss in String umgewandelt werden)
print("Hallo" + str({"a": 1, "b": 2})) # Konkatenation mit Dictionary (Dictionary muss in String umgewandelt werden)

# Listen
# Eine Liste ist eine geordnete Sammlung von Werten, die veränderbar ist. (mutable)
lst = [1, 2, 3, 4, 5]
print(lst)
print(type(lst))
print(len(lst)) # Länge der Liste
print(lst[0]) # Erstes Element
print(lst[-1]) # Letztes Element
print(lst[0:3]) # Teil der Liste von Index 0 bis 2
print(lst[::2]) # Jedes zweite Element
print(lst[::-1]) # Liste umgekehrt
lst.append(6) # Fügt 6 am Ende der Liste hinzu
print(lst)
lst.insert(0, 0) # Fügt 0 am Anfang der Liste hinzu
print(lst)
lst.remove(3) # Entfernt das erste Vorkommen von 3
print(lst)
lst.pop() # Entfernt das letzte Element und gibt es zurück
print(lst)
lst.pop(0) # Entfernt das erste Element und gibt es zurück
print(lst)
lst[0] = 10 # Ändert das erste Element zu 10
print(lst)
print(3 in lst) # Prüft, ob 3 in der Liste enthalten ist
print(10 in lst) # Prüft, ob 10 in der Liste enthalten ist
print(lst + [7, 8, 9]) # Konkatenation mit einer anderen Liste
print(lst * 2) # Wiederholung der Liste
for i in lst:
    print(i) # Iteration über die Liste und Ausgabe jedes Elements  
print(sum(lst)) # Summe der Elemente in der Liste
print(min(lst)) # Minimum der Elemente in der Liste
print(max(lst)) # Maximum der Elemente in der Liste
print(sorted(lst)) # Sortierte Liste (original bleibt unverändert)
lst.sort() # Sortiert die Liste (original wird verändert)
print(lst)
lst.reverse() # Kehrt die Liste um (original wird verändert)
print(lst)
print(lst.count(2)) # Zählt, wie oft 2 in der Liste vorkommt
print(lst.index(4)) # Gibt den Index des ersten Vorkommens von 4 zurück
lst.clear() # Entfernt alle Elemente aus der Liste
print(lst)


# Tupel
# Ein Tupel ist eine geordnete Sammlung von Werten, die unveränderbar ist. (immutable)
tup = (1, 2, 3, 4, 5)
print(tup)
print(type(tup))
print(len(tup)) # Länge des Tupels
print(tup[0]) # Erstes Element


print(tup[-1]) # Letztes Element
print(tup[0:3]) # Teil des Tupels von Index 0 bis 2
print(tup[::2]) # Jedes zweite Element             
print(tup[::-1]) # Tupel umgekehrt
print(3 in tup) # Prüft, ob 3 im Tupel enthalten ist
print(10 in tup) # Prüft, ob 10 im Tupel enthalten ist
print(tup + (6, 7, 8)) # Konkatenation mit einem

print(tup * 2) # Wiederholung des Tupels
for i in tup:
    print(i) # Iteration über das Tupel und Ausgabe jedes Elements  
print(sum(tup)) # Summe der Elemente im Tupel
print(min(tup)) # Minimum der Elemente im Tupel
print(max(tup)) # Maximum der Elemente im Tupel
print(sorted(tup)) # Sortierte Liste (original bleibt unverändert)
# tup[0] = 10 # TypeError: 'tuple' object does not support item assignment
# tup.append(6) # AttributeError: 'tuple' object has no attribute 'append'
# tup.remove(3) # AttributeError: 'tuple' object has no attribute 'remove'
# tup.pop() # AttributeError: 'tuple' object has no attribute 'pop'
# tup.clear() # AttributeError: 'tuple' object has no attribute 'clear' andere Tupel
# tup.insert(0, 0) # AttributeError: 'tuple' object has no attribute 'insert'   
