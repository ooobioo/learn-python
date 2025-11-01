# Frage 1
print("\n## 1 ####")

x = """
"""

print(len(x))


# Frage 2
print("\n## 2 ####")

x = 9
y = 12
result = x // 2 * 2 / 2 + y % 2 ** 3
print(result)

# number = 5  # binary 0101
bit_position = 0  # checking least significant bit
mask = 1 << bit_position  # mask = 1 (binary 0001)
mask = 2 << bit_position  # mask = 1 (binary 0010)
for i in range(1,11):
    if i & mask:
        print(f"{i:>2} Bit is set")
    else:
        print(f"{i:>2} Bit is not set")


# Frage 3
print("\n## 3 ####")


# Example: Keep only even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
is_even = lambda x: x % 2 == 0
filtered = filter(is_even, numbers)
print(list(filtered))  # Output: [2, 4, 6]


vect = ["alpha", 'bravo', "charlie"]
new_vect = filter(lambda s: s[-1].upper() in ['A', 'O'], vect)
for x in new_vect:
    print(x[1], end="")
print()

numbers = list(range(1000))
istdurchXteilbar = lambda x: x % 36 == 0
newnumbers = filter(istdurchXteilbar, numbers)
print(list(newnumbers))

numbers = [-2, -1, 0, 1, 2, True, False ]
newnumbers = filter(None, numbers)
print(list(newnumbers))



# Frage 4
print("\n## 4 ####")

class Collection:
    stamps = 2

    def __init__(self, stuff):
        self.stuff = stuff
        self.somevalue = "huhu"

    def dispose(self):
        del self.stuff

binder = Collection(1)
binder.dispose()

print(Collection.__dict__)
print(binder.__dict__)


# Frage 5
print("\n## 5 ####")

num = 1
def func():
    num = 3
    print(num, end= ' ')

func()
print(num)


# Frage 7
print("\n## 7 ####")

x = 0
assert x == 0, "hier gehts nicht weiter"
print("das prgramm läuft weiter...")


# Frage 9
print("\n## 9 ####")

print("ich" "bin" "toll")


# Frage 10
print("\n## 10 ####")

import platform

print(platform.version())



# Frage 11
print("\n## 11 ####")

class Ceil:
    Token = 1
    def get_token(self):
        return 1

class Floor(Ceil):
    def get_token(self):
        return 2
    def set_token(self):
        pass

holder= Floor()
print(hasattr(holder, "Token"), hasattr(Ceil, "set_token"))
print(hasattr(holder, "Token"), hasattr(Ceil, "get_token"))


# Frage 12
print("\n## 12 ####")

try:
    f = open("non_existing_file", "w")
    print(1, end=" ")
    s = f.readline() # w kann nur schreiben, nicht lesen
    print(2, end=" ")
except IOError as error:
    print(3, end=" ")
else:
    f.close()
    print(4, end=" ")
finally:
    print(5)


# Frage 18
print("\n## 18 ####")

class Class:
    def __init__(self):
        pass

object = Class()
object = Class


# Frage 21
print("\n## 21 ####")

x=1
while x<2e6:
    print(x, '*')
    x = x << 1


# Frage 25
print("\n## 25 ####")

class Klasse1():
    xvariable = 0

    def __init__(self):
        Klasse1.xvariable += 1


class Klasse2(Klasse1):
    def __init__(self):
        self.myvariable = 0
        super().__init__()

class Klasse3(Klasse2):
    def __init__(self):
        self.myvariable = 0
        # super().__init__()

class Klasse4():
    pass


k2obj = Klasse2()
k3obj = Klasse3()

print(issubclass(Klasse3, Klasse2))
print(issubclass(Klasse3, Klasse1))
print(issubclass(Klasse1, Klasse2))
print(issubclass(Klasse4, Klasse2))


print(k2obj.xvariable)
print(k3obj.xvariable)


print(k2obj.xvariable)
print(k3obj.xvariable)

print(Klasse1.xvariable)


# Frage 33
print("\n## 33 ####")

print(float("1.3"))
# print(float("1,3"))


# Frage 34
print("\n## 34 ####")


# string sind immutabel

string = "hallo"
# del string[2]



# Frage 36
print("\n## 36 ####")

x = 55
x = str(x + 5)
x *= 2 + 1
print(x)

x = 55
x = str(x + 5)
# x = x * 2 + 1   # Error
print(x)

x = 60
x **= 2 + 1
print(x)

x = 60
x = x ** 2 + 1
print(x)



############################

for i in range(10):
    pass

print(i)



class Restaurant(object):
    bankrupt = False
    def open_branch(this):
        if not this.bankrupt:
            print("branch opened")

restaurant = Restaurant()
restaurant.open_branch()



################


print()

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    print("initial assignment:".ljust(40, "."), spam)
    do_local()
    print("After local assignment:".ljust(40, "."), spam)
    do_nonlocal()
    print("After nonlocal assignment:".ljust(40, "."), spam)
    do_global()
    print("After global assignment:".ljust(40, "."), spam)

scope_test()
print("In global scope:".ljust(40, "."), spam)

class X:
    pass



###########################


def square(x):
    return x * x

numbers = [1, 2, 3, 4]
squared = map(square, numbers)
print(list(squared))

def upperchar(x: str):
    return x.upper()

string = "hallo alter"
gross = map(upperchar, string)
print(list(gross))