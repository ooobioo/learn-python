# Liste
mylist = [1, 2, 3, 4]

# Tupel
mytuple = ("apple", "banana", "cherry")

# Dictionary
mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Menge
myset = {"apple", "banana", "cherry"}

spam = """"""
ham = """
"""

print(spam, ham)
print("-")
print("", end="")

print("Spam,Ham,Eggs"[5:8])
print("Spam,Ham,Eggs"[-8:-5])
print("Spam,Ham,Eggs"[5:-5])
print("Spam,Ham,Eggs"[-5:-8])  # empty slice: end before start
print("Spam,Ham,Eggs"[-5:5])   # empty slice: end before start


# ZEICHENKODIERUNGEN ####################

# bytes string
string = str("püthon")
b"python"
# bytes_string = b"püthon" # Error - ü nicht in ASCII
bytes_string = string.encode("iso-8859-15")

print(bytes_string)

euro = "\N{euro sign}"
print(euro)

print(chr(8364))
print(chr(8365))

# ch = chr('a') # -> TypeError - chr nimmt nur integer als eingabe
ch = chr(97)
or_ = ord(ch)
print(or_, ch)


# FEHLERBEHANDLUNG #######################################

print()

try:
    print(ord("123"))  # -> Error - ord braucht einen character als input
except TypeError:
    print("Error: ord braucht einen character als input")
else:
    print("hier else")
finally:
    print("hier finally")

print()
try:
    print(ord("b"))  # -> Error - ord braucht einen character als input
except TypeError:
    print("Error: ord braucht einen character als input")
else:
    print("hier else")
finally:
    print("hier finally")

print()
try:
    print(ord("bb"))  # -> Error - ord braucht einen character als input
except Exception:
    print("Irgendein Error: ord braucht einen character als input")
else:
    print("hier else")
finally:
    print("hier finally")

print()

try:
    print(ord("123"))  # -> Error - ord braucht einen character als input
except TypeError as e:
    print(e.args[0])
else:
    print("hier else")
finally:
    print("hier finally")

print()
print()


def test_type(x):
    if isinstance(x, int):
        raise TypeError("ERROR: kein int")
    return x*x


try:
    print(test_type("s"))
except TypeError as e:
    print(e.args[0])

print()

####################

xliste = [7, 1, 5, 4, 10]

assert max(xliste) < 20
# assert max(xliste) < 9


print()

try:
    raise IndexError
except IndexError:
    print("b")
