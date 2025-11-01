# Unterstriche in Zahlen
# In Python können Sie Unterstriche in Zahlen verwenden, um die Lesbarkeit zu verbessern.
# Diese Unterstriche werden ignoriert und haben keinen Einfluss auf den Wert der Zahl.
große_zahl = 1_000_000
kleine_zahl = 0.000_001
print(große_zahl)  # Ausgabe: 1000000
print(kleine_zahl)  # Ausgabe: 1e-06

# Zahlen in verschiedenen Basen
# Python unterstützt verschiedene Zahlensysteme wie Binär (Basis 2), Oktal (Basis 8) und Hexadezimal (Basis 16).
binär = 0b1010  # Binär für 10
oktal = 0o12     # Oktal für 10
hexadezimal = 0xA  # Hexadezimal für 10
print(binär)        # Ausgabe: 10
print(oktal)       # Ausgabe: 10
print(hexadezimal)  # Ausgabe: 10 


# maximale Basis ist 36

zahl = int("Z", 36)  # Z in Basis 36 ist 35 in Dezimal
print(zahl)      # Ausgabe: 35

zahl = int("421", 8)  # 421 in Oktal
print(zahl)      # Ausgabe: 273

zahl = 0b101 +2     # Binär für 7
print(zahl)     # Ausgabe: 7

zahl = 0o101 + 2     # Oktal für 67
print(zahl)     # Ausgabe: 67

zahl = 0x1A + 2    # Hexadezimal für 28
print(zahl)     # Ausgabe: 28

zahl = 0b101 + 0o10 + 0x1A + int("11", 6) + int("D", 22)    # 5 + 8 + 26 + 7 + 13
print(zahl)     # Ausgabe: 59


# Bitoperationen
a = 0b1100  # 12 in Dezimal
b = 0b1010  # 10 in Dezimal
print(bin(a & b))  # Bitweises UND: 0b1000 (8 in Dezimal)
print(bin(a | b))  # Bitweises ODER: 0b1110 (14 in Dezimal)
print(bin(a ^ b))  # Bitweises XOR: 0b0110 (6 in Dezimal)
print(bin(~a))     # Bitweises NICHT: -0b1101 (-13 in Dezimal)
print(bin(a << 2))  # Linksverschiebung: 0b110000 (48 in Dezimal)
print(bin(a >> 2))  # Rechtsverschiebung: 0b0011 (3 in Dezimal) 

# Gleitkommazahlen
# Gleitkommazahlen werden in Python als 'float' bezeichnet und entsprechen dem IEEE 754 Standard.
# Sie können Gleitkommazahlen in wissenschaftlicher Notation schreiben.         
ganzzahl = 12345678901234567890
gleitkommazahl = 1.2345678901234567890e10
print(ganzzahl)        # Ausgabe: 12345678901234567890
print(gleitkommazahl)  # Ausgabe: 12345678901.234567    
# Beachten Sie, dass die Genauigkeit von Gleitkommazahlen begrenzt ist.
# Python verwendet standardmäßig 64-Bit Gleitkommazahlen, was etwa 15-17 signifikante Dezimalstellen bietet.
# Für höhere Genauigkeit können Sie das 'decimal'-Modul verwenden.
from decimal import Decimal, getcontext
getcontext().prec = 30  # Setzt die Genauigkeit auf 30 Dezimalstellen
präzise_zahl = Decimal('1.23456789012345678901234567890')
print(präzise_zahl)  # Ausgabe: 1.234567

zahl= 1,7e-3
print(zahl)  # Ausgabe: 0.001777    
zahl = 1,7e3    
print(zahl)  # Ausgabe: 1700.0  



# Exponentiation
# In Python können Sie die Exponentiation mit dem '**'-Operator durchführen.
basis = 2
exponent = 10
ergebnis = basis ** exponent
print(ergebnis)  # Ausgabe: 1024    
# Sie können auch die eingebaute Funktion 'pow()' verwenden, die drei Argumente akzeptiert: Basis, Exponent und optional ein Modulus.
ergebnis_mod = pow(basis, exponent, 1000)  # (2^10) % 1000
print(ergebnis_mod)  # Ausgabe: 24


1+-2 # Ausgabe: -1
1--2 # Ausgabe: 3
1*-2 # Ausgabe: -2
1/-2 # Ausgabe: -0.5
1//-2 # Ausgabe: -1
5//2 # Ausgabe: 2
11//2 # Ausgabe: 5
5//-2 # Ausgabe: -3
5%2 # Ausgabe: 1
1%-2 # Ausgabe: -1
1**-2 # Ausgabe: 1.0
1+-2*3 # Ausgabe: -5
(1+-2)*3 # Ausgabe: -3
1+(-2*3) # Ausgabe: -5
1**2**3 # Ausgabe: 1
(1**2)**3 # Ausgabe: 1
-3**2 # Ausgabe: -9
(-3)**2 # Ausgabe: 9
2**3**2 # Ausgabe: 512
(2**3)**2 # Ausgabe: 64
2**(3**2) # Ausgabe: 512
# Reihenfolge der Operatoren:
# 1. Klammern
# 2. Exponentiation
# 3. Vorzeichen
# 4. Multiplikation, Division, Ganzzahlige Division, Modulo
# 5. Addition, Subtraktion
# Operatoren mit gleicher Priorität werden von links nach rechts ausgewertet, mit Ausnahme der Exponentiation, die von rechts nach links ausgewertet wird.


# And operator able to perform bitwise shifts is coded as
a = 5  # In Binär: 0b0101
b = 3  # In Binär: 0b0011      
print(a & b)  # Bitweises UND: 0b0001 (1 in Dezimal)
print(a | b)  # Bitweises ODER: 0b0111 (
print(a ^ b)  # Bitweises XOR: 0b0110 (6 in Dezimal)
print(~a)     # Bitweises NICHT: -0b0110 (-6 in Dezimal)
print(a << 1)  # Linksverschiebung: 0b1010 (10 in Dezimal)
print(a >> 1)  # Rechtsverschiebung: 0b0010 (2 in Dezimal)  
# Ausgabe: 7 in Dezimal)   
# Bitweise Operatoren haben eine niedrigere Priorität als arithmetische Operatoren. 
# Das bedeutet, dass arithmetische Operationen zuerst ausgeführt werden.
result = a + b & 2  # Entspricht a + (b &
print(result)  # Ausgabe: 7 (5 + (3 & 2) = 5 + 2 = 7) 2)
result = (a + b) & 2  # Entspricht (a + b) & 2
print(result)  # Ausgabe: 0 ((5 + 3) & 2 = 8 & 2 = 0)   
# Bitweise Operatoren können auch mit Zuweisungsoperatoren kombiniert werden.
a &= 2  # Entspricht a = a & 2
print(a)  # Ausgabe: 0 (5 & 2 = 0)      
a |= 2  # Entspricht a = a | 2
print(a)  # Ausgabe: 2 (0 | 2 = 2)      
a ^= 3  # Entspricht a = a ^ 3
print(a)  # Ausgabe: 1 (2 ^ 3 = 1)      
a <<= 1  # Entspricht a = a << 1
print(a)  # Ausgabe: 2 (1 << 1 = 2)      
a >>= 1  # Entspricht a = a >> 1
print(a)  # Ausgabe: 1 (2 >> 1 = 1) 
# Bitweise Operatoren können auch mit anderen Datentypen wie booleschen Werten und Bytes verwendet werden.
x = True
y = False
print(x & y)  # Ausgabe: False (True & False = False)
print(x | y)  # Ausgabe: True (True | False = True)     
print(x ^ y)  # Ausgabe: True (True ^ False = True)
print(~x)     # Ausgabe: -2 (~True = -2)
# Bytes
b1 = bytes([0b10101010, 0b11001100])
b2 = bytes([0b11110000, 0b00001111])
b_and = bytes([a & b for a, b in zip(b1, b2)])
b_or = bytes([a | b for a, b in zip(b1, b2)])
b_xor = bytes([a ^ b for a, b in zip(b1, b2)])
print(b_and)  # Ausgabe: b'\xa0\x0c' (0b10100000, 0b00001100)
print(b_or)   # Ausgabe: b'\xfa\xcf' (0b11111010, 0b11001111)
print(b_xor)  # Ausgabe: b'\x5a\xc3' (0b01011010, 0b11000011)


# Booleans
# In Python sind Booleans eine eingebaute Datenstruktur, die zwei Werte repräsentiert: True und False.
# Diese Werte werden häufig in Kontrollstrukturen wie if-Anweisungen   
# und Schleifen verwendet, um Bedingungen zu überprüfen.
# Booleans können auch als Ganzzahlen betrachtet werden, wobei True den Wert 1 und False den Wert 0 hat.
a = True
b = False
print(a)        # Ausgabe: True
print(b)        # Ausgabe: False
print(int(a))   # Ausgabe: 1
print(int(b))   # Ausgabe: 0
print(float(a)) # Ausgabe: 1.0
print(float(b)) # Ausgabe: 0.0
# Booleans können mit logischen Operatoren kombiniert werden.
print(a and b)  # Ausgabe: False (True AND False = False)
print(a or b)   # Ausgabe: True (True OR False = True)
print(not a)    # Ausgabe: False (NOT True = False)
print(not b)    # Ausgabe: True (NOT False = True)
# Logische Operatoren haben eine bestimmte Priorität.
# NOT hat die höchste Priorität, gefolgt von AND und dann OR.
# Klammern können verwendet werden, um die Reihenfolge der Auswertung zu ändern.
x = True
y = False
z = True        
print(x or y and z)        # Ausgabe: True (x OR (y AND z) = True OR (False AND True) = True OR False = True)
print((x or y) and z)      # Ausgabe: True ((x OR y) AND z = (True OR False) AND True = True AND True = True)
print(not x or y)       # Ausgabe: False (NOT x OR y = NOT True OR False = False OR False = False)
print(not (x or y))     # Ausgabe: False (NOT (x OR y) = NOT (True OR False) = NOT True = False)
# Booleans können auch in mathematischen Operationen verwendet werden.
print(a + 5)    # Ausgabe: 6 (True + 5 = 1 + 5 = 6)
print(b + 5)    # Ausgabe: 5 (False + 5 = 0 + 5 = 5)
print(a * 10)   # Ausgabe: 10 (True * 10 = 1 * 10 = 10)
print(b * 10)   # Ausgabe: 0 (False * 10 = 0 * 10 = 0)
# Booleans können auch in Datenstrukturen wie Listen, Tupeln und Dictionaries verwendet werden.
bool_list = [True, False, True]
bool_tuple = (False, True, False)
bool_dict = {True: "Ja", False: "Nein"}
print(bool_list)   # Ausgabe: [True, False, True]
print(bool_tuple)  # Ausgabe: (False, True, False)
print(bool_dict)   # Ausgabe: {True: 'Ja', False: 'Nein'}
print(bool_dict[True])   # Ausgabe: Ja
print(bool_dict[False])  # Ausgabe: Nein    
# Booleans können auch in Funktionen verwendet werden.
def is_even(n):
    return n % 2 == 0   
print(is_even(4))  # Ausgabe: True
print(is_even(5))  # Ausgabe: False 
def is_positive(n):
    if n > 0:
        return True
    else:
        return False
print(is_positive(10))  # Ausgabe: True
print(is_positive(-5))  # Ausgabe: False
def logical_and(x, y):
    return x and y
print(logical_and(True, True))    # Ausgabe: True
print(logical_and(True, False))   # Ausgabe: False
print(logical_and(False, True))   # Ausgabe: False      
print(logical_and(False, False))  # Ausgabe: False
def logical_or(x, y):
    return x or y
print(logical_or(True, True))     # Ausgabe: True
print(logical_or(True, False))    # Ausgabe: True
print(logical_or(False, True))    # Ausgabe: True
print(logical_or(False, False))   # Ausgabe: False
def logical_not(x):
    return not x
print(logical_not(True))   # Ausgabe: False     
print(logical_not(False))  # Ausgabe: True

# Komplexe Zahlen
# In Python sind komplexe Zahlen eine eingebaute Datenstruktur, die aus einem Realteil und einem Imaginärteil besteht.
# Der Imaginärteil wird durch das Suffix 'j' oder 'J' dargestellt.
# Komplexe Zahlen werden häufig in wissenschaftlichen und technischen Anwendungen verwendet.
a = 2 + 3j
b = 1 - 4j
print(a)        # Ausgabe: (2+3j)
print(b)        # Ausgabe: (1-4j)
print(a.real)   # Ausgabe: 2.0 (Realteil)
print(a.imag)   # Ausgabe: 3.0 (Imaginärteil)
print(b.real)   # Ausgabe: 1.0 (Realteil)
print(b.imag)   # Ausgabe: -4.0 (Imaginärteil)
