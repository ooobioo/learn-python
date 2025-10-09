# Kontrollstrukturen

## If-Else Statements

```
zahl = int(input("Gib eine Zahl ein: "))

if zahl > 0:
print("Die Zahl ist positiv.")
elif zahl < 0:
print("Die Zahl ist negativ.")
else:
print("Die Zahl ist null.")

print(f"Die Zahl ist {zahl}.")
```

## Ternary Operators / Conditional Expressions

```
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
```

### Uebung: Schreibe ein Programm, das eine Zahl einliest und ausgibt, ob die Zahl negativ oder nicht-negativ ist. Verwende einen Ternary Operator.

```
zahl = int(input("Bitte eine Zahl eingeben: "))
string = "nichtnegativ" if zahl >= 0 else "negativ"
print(f"Die Zahl ist {string}.")
```
