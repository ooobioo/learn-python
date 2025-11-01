x=3

while x > 0:
    print(x, end="")
    x //=2

print()


# STRINGS ###################

string = "erster teil" "zweiter teil"
print(string, end="\\")

print()
print(end="\t")
print("x")
print("x")

print()

import time

def zahlen_bis_x(x):
    for i in range(x+1):
        print("Zahl:", i, end="\r")
        time.sleep(0.0001)
    print()

zahlen_bis_x(2000)

# raw string
# präfix r

string = r"string mit \n steuerzeichen"
print("string mit \t steuerzeichen")
print(r"string mit \t steuerzeichen wie \\n. \n")

print("Es ist {0}:{1} Uhr".format(11,20))
print("Es ist {stunden}:{minuten} Uhr".format(minuten=11,stunden=20))

print()

# f string
preis=19.99
print(f"Das kostet {preis} € netto")
print(f"Das kostet {round(preis*1.19, 2)} € brutto")
print(f"Das kostet {preis*1.19:.2f} € brutto")
print(f" xxx {{ {preis} }} xxx")

print()

#konvertierung
expr = "Dies ist \u26f5"
print(f"{expr!s}")
print(f"{expr!r}")
print(f"{expr!a}")

print()

print(f"{22.2070 : .3f}")
print(f"{22.2070 : .2f}")
print(f"{22.2070 : .6f}")

print()

print(f"{1:03d}")
print(f"{11:03d}")
print(f"{111:03d}")

print()

print(f"{'abc':^15}")
print(f"{'a':^15}")
print(f"{'abcdefg':^15}")

print()

print(f"{'abc':>15}")
print(f"{'a':>15}")
print(f"{'abcdefg':>15}")

print()

#### AUFGABE

def preci(i: int, c: float):
    print(f"Mit {i:>2} Stellen hinter dem Komma: {c:<30.{i}f} | xxx")
    return

preci(2, 3.1415)
preci(5, 3.1415)
preci(10, 3.1415)
preci(20, 3.1415)

print()

string: str = "Dieser Satz   hat fünf Wörter"
print(string.split())
print(string.split(" "))
print(string.split("e"))
print(string.split(maxsplit=2))

print()

print("XababaY XababaY".split("aba"))
print("XababaY XababaY".rsplit("aba"))

print()
print()
print()

# MENGEN #######################

li = [1,2,3,4]
menge = set(li)
nicht_aenderbare_menge = frozenset(li)
print(menge)
print(nicht_aenderbare_menge)

menge.add(5)
# nicht_aenderbare_menge.add(5) # attribute error
print(menge.add(6))
print(menge.add(6))
print(menge)

menge.discard(3)
print("R:",menge.remove(5))
# print("R:",menge.remove(9))
print("D:",menge.discard(5))
print(menge)


def mengenrelationen(m1: set, m2: set):
    li = ["<","<=",">",">=","&", "x", "y", "y","|"]
    # Define a mapping from string to set operator function
    operators = {
        "<": lambda a, b: a < b,    # Proper subset
        "<=": lambda a, b: a <= b,  # Subset or equal
        ">": lambda a, b: a > b,    # Proper superset
        ">=": lambda a, b: a >= b,   # Superset or equal
        "&": lambda a, b: a & b,
        "|": lambda a, b: a | b,
    }

    return { op: operators[op](m1,m2) if op in operators else "Error: Operator not found" for op in li  }

print()
menge_1 = {1,2}
menge_2 = {1,2,8,10,12,14,16}
menge_3 = {1,2,8,10,12,14,16}

print(mengenrelationen(menge_1,menge_2))
print(mengenrelationen(menge_2,menge_1))
print(mengenrelationen(menge_2,menge_3))
print()


# SEITENEFFEKTE ############

a=5
b=5

print(id(a))
print(id(b))

def f(a=[1,2,3]):
    a += [4,5,6]
    print(a)

f()
f()
f()

print()

def modify_list(lst):
    lst.append(100)  # Modify the list (mutable)
    print(lst)

my_list = [1, 2, 3]
modify_list(my_list.copy())  # Pass a copy to simulate call by value

print(my_list)  # Output: [1, 2, 3], original list unchanged