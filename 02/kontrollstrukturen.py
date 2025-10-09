# IF-ELSE AND FLOW CONTROL


######################################
# If-Else Statements
zahl = int(input("Gib eine Zahl ein: "))

if zahl > 0:
    print("Die Zahl ist positiv.")
elif zahl < 0:
    print("Die Zahl ist negativ.")
else:
    print("Die Zahl ist null.")

print(f"Die Zahl ist {zahl}.")

######################################
# If-Else Statements
x=10

if x == 1:
    var = 20
else:
    var = 30

######################################
# Ternary Operators / Conditional Expressions
x=10

var = (20 if x == 1 else 30)

nice = True
personality = ("mean", "nice")[nice]
print("The cat is ", personality)

condition = True
print(2 if condition else 1)
#Output is 2

print((1, 2)[condition])
#ZeroDivisionError is raised

# Uebung: Schreibe ein Programm, das eine Zahl einliest und ausgibt, ob die Zahl negativ oder nicht-negativ ist. Verwende einen Ternary Operator.
zahl = int(input("Bitte eine Zahl eingeben: "))
string = "nichtnegativ" if zahl >= 0 else "negativ"
print(f"Die Zahl ist {string}.")


# Schleifen
######################################
# While-Schleife
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# While-Schleife mit Else
# Wenn die Bedingung der While-Schleife nicht mehr erfuellt ist, wird der Code im Else-Block ausgefuehrt.
# Bei break-Anweisungen wird der Else-Block uebersprungen.
count = 0
while count < 5:
    print("Count:", count)
    count += 1
else:
    print("Fertig!")

# Break und Continue
condition = True
x = 0
while condition:
    print(x)
    x += 1
    if x >= 20:
        break
        # Break-Anweisung beendet die Schleife
    print(x, end = " - ")
    if x >= 10:
        print(" Reached 10, continuing...")
        continue
        # This will skip the print statement below when x >= 10 and go back to the start of the loop
    print(x, end = " | ")

# Uebung: Schreibe ein Programm, das zwei Zahlen einliest und die erste Zahl solange um 1 erhoeht und ausgibt, bis sie gleich der zweiten Zahl ist.
zahl1 = int(input("Gib eine Startzahl ein: ")) + 1
zahl2 = int(input("Gib eine Endzahl ein: "))

i=zahl1

while i != zahl2:
    print(i, ",", end=" ")
    i += 1
else:
    print()

# For-Schleife
for x in range(zahl1, zahl2):
    print(x, ", ", end="")
print()

# For-Schleife mit Schrittweite
for x in range(zahl1, zahl2, 4):
    print(x, ", ", end="")
print()

# Uebung: Schreibe ein Programm, das zwei Zahlen einliest und alle geraden Zahlen zwischen der ersten und der zweiten Zahl ausgibt.
for x in range(zahl1, zahl2):
    if x % 2 == 0:
        print(x, ", ", end="")
print()

# Pass Statement
# Das Pass-Statement wird verwendet, wenn eine Anweisung syntaktisch erforderlich ist, aber kein Code ausgefuehrt werden soll.
# Es wird oft als Platzhalter in leeren Schleifen oder Funktionen verwendet.
for i in range (10):
    pass
print(i) # Ausgabe: 9
