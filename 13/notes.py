import random

random.seed(10, 2)
print(random.random())

print(random.sample(["spam", "spum", "spom"], k=1))

random.seed(0)
a = random.choice([1,2])

random.seed(0)
b = random.choice([1,2])

print(a,b)
print(a-b)


print("\n###########\n")


class Oben:
    def __init__(self):
        print("Oben")

class Links(Oben):
    def __init__(self):
        print("Links")
        super().__init__()
    pass
          
class Rechts:
    def __init__(self):
        print("Rechts")
          
class Unten(Links, Rechts):
    def __init__(self):
        print("Unten")
        super().__init__()
    pass


Unten()

print("\n###########\n")

class ueberbasis:
    def  __init__(self):
        print("ueberbasis")
    def i(self):
        pass
class basis:
    def  __init__(self):
        print("basis")
    def h(self):
        pass
class links(basis):
    def  __init__(self):
        print("links")
        # super().__init__()
        # basis.__init__(self)
        ueberbasis.__init__(self)
    def g(self):
        pass
class rechts(basis):
    def  __init__(self):
        print("rechts")
        super().__init__()
    def f(self):
        pass
class mitte(links, rechts):
    def  __init__(self):
        print("mitte")
        # super().__init__()
        rechts.__init__(self)
    def f(self):
        pass
class unten ( mitte ):
    pass
    def  __init__(self):
        print("unten")
        super().__init__()
        # basis.__init__(self)
 
        
obj = unten()
print("\n###########\n")
# linksobj = links()

print("\n###########\n")
