def subtract(a: int, b: int):
    if a > b:
        return a - b
    else:
        return b - a

zahl1: float = float(input("Gib die erste Zahl ein: "))
zahl2: int = int(input("Gib die zweite Zahl ein: "))

print("Ergebnis:" , subtract(zahl1, zahl2))
