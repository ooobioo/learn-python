# Funktionen
# Funktionen sind wiederverwendbare Codeblöcke, die eine bestimmte Aufgabe erfüllen.
# Sie werden mit dem Schlüsselwort def definiert, gefolgt vom Funktionsnamen und
# einer Liste von Parametern in Klammern. Der Funktionskörper wird durch Einrückung
# definiert.    
def begruessung(name):
    """Diese Funktion begruesst die Person mit dem angegebenen Namen."""
    print("Hallo,", name + "!") 
    print("Willkommen in der Welt der Python-Funktionen.")
# Aufruf der Funktion
begruessung("Alice")
begruessung("Bob")
# Funktionen können auch Werte zurückgeben, indem sie das Schlüsselwort return verwenden.
def addiere(a, b):
    """Diese Funktion gibt die Summe von a und b zurück."""
    return a + b
# Aufruf der Funktion und Speichern des Rückgabewerts in einer Variablen
ergebnis = addiere(5, 3)
print("Die Summe ist:", ergebnis)
# Funktionen können auch mehrere Werte zurückgeben, indem sie diese in einem Tupel verpacken.
def rechne(a, b):
    """Diese Funktion gibt die Summe und das Produkt von a und b zurück."""
    summe = a + b
    produkt = a * b
    return summe, produkt
# Aufruf der Funktion und Entpacken der Rückgabewerte in separate Variablen
s, p = rechne(4, 6)
print("Summe:", s)
print("Produkt:", p)
# Funktionen können auch Standardwerte für Parameter haben.
def begruessung_mit_titel(name, titel="Herr/Frau"):
    """Diese Funktion begruesst die Person mit dem angegebenen Namen und Titel."""
    print("Hallo,", titel, name + "!")
# Aufruf der Funktion mit und ohne Angabe des Titels
begruessung_mit_titel("Schmidt", "Dr.")
begruessung_mit_titel("Meyer")
# Funktionen können auch verschachtelt sein, d.h. eine Funktion kann innerhalb einer anderen Funktion definiert werden.
def aussenfunktion(x):
    """Diese Funktion definiert eine innere Funktion und ruft sie auf."""
    def innenfunktion(y):
        """Diese innere Funktion quadriert die Eingabe."""
        return y * y
    return innenfunktion(x)
# Aufruf der äußeren Funktion
resultat = aussenfunktion(5)
print("Das Quadrat ist:", resultat)
# Funktionen können auch als Argumente an andere Funktionen übergeben werden.
def anwenden(funktion, wert):
    """Diese Funktion wendet eine gegebene Funktion auf einen Wert an."""
    return funktion(wert)
# Definieren einer einfachen Funktion zum Quadrieren
def quadriere(n):
    return n * n
# Aufruf der anwenden-Funktion mit der quadriere-Funktion als Argument
ergebnis = anwenden(quadriere, 7)
print("Das Ergebnis ist:", ergebnis)
# Funktionen können auch Lambda-Ausdrücke sein, die anonyme Funktionen darstellen.
# Lambda-Funktionen werden mit dem Schlüsselwort lambda definiert, gefolgt von einer
# Liste von Parametern, einem Doppelpunkt und einem Ausdruck.
# Lambda-Funktionen können nur einen einzigen Ausdruck enthalten und keinen
# Funktionskörper mit mehreren Anweisungen.
# Sie werden häufig für kurze, einmalige Funktionen verwendet.
# Beispiel einer Lambda-Funktion zum Quadrieren
quadriere_lambda = lambda x: x * x
# Aufruf der Lambda-Funktion
ergebnis = quadriere_lambda(8)
print("Das Ergebnis der Lambda-Funktion ist:", ergebnis)
# Lambda-Funktionen können auch als Argumente an andere Funktionen übergeben werden.
ergebnis = anwenden(lambda x: x + 10, 5)
print("Das Ergebnis der Lambda-Funktion als Argument ist:", ergebnis)       
# Lambda-Funktionen können auch in Kombination mit Funktionen wie map(), filter() und reduce() verwendet werden.
# Beispiel mit map(), um eine Liste von Zahlen zu quadrieren
zahlen = [1, 2, 3, 4, 5]
quadrierte_zahlen = list(map(lambda x: x * x, zahlen))
print("Quadrierte Zahlen:", quadrierte_zahlen)
# Beispiel mit filter(), um nur gerade Zahlen aus einer Liste zu filtern
gerade_zahlen = list(filter(lambda x: x % 2 == 0, zahlen))
print("Gerade Zahlen:", gerade_zahlen)
# Beispiel mit reduce(), um die Summe einer Liste von Zahlen zu berechnen
from functools import reduce
summe = reduce(lambda x, y: x + y, zahlen)
print("Summe der Zahlen:", summe)       
# Funktionen können auch Dokumentationsstrings (Docstrings) haben, die eine Beschreibung der Funktion enthalten.
# Docstrings werden in dreifachen Anführungszeichen geschrieben und können mit der Funktion help() angezeigt werden.
print(help(begruessung))
print(help(addiere))
print(help(rechne))
print(help(begruessung_mit_titel))
print(help(aussenfunktion))
print(help(anwenden))
# Docstrings sind nützlich, um den Zweck und die Verwendung einer Funktion zu erklären.
# Sie helfen anderen Entwicklern (und auch Ihnen selbst), den Code besser zu verstehen.
# Funktionen sind ein wichtiger Bestandteil der Programmierung in Python und ermöglichen es, den Code modular,      
# wiederverwendbar und leichter verständlich zu machen.