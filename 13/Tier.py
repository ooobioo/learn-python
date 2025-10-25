
class Tier():
    def __init__(self):
        self._x = 0
        print("Tier")
    def lese_x(self):
        print("ich lese x")
        return(self._x)
    def schreibe_x(self, k):
        print("ich schreibe x")
        self._x = k
    def loesche_x(self):
        print("ich schreibe x")
        del(self._x)
    x = property(lese_x, schreibe_x, loesche_x)

class Pflanzenfresser(Tier):
    def __init__(self):
        print("Pflanzenfresser")
        super().__init__()
    def p():
        pass
    
class Fleischfresser(Tier):
    def __init__(self):
        print("Fleischfresser")
        super().__init__()
    def f():
        pass

class Allesfresser(Pflanzenfresser, Fleischfresser):
    def __init__(self):
        print("Allesfresser")
        Pflanzenfresser.__init__(self)
        # Fleischfresser.__init__(self)
        pass
    def a():
        pass

print()
obj = Allesfresser()
print(obj.x)
obj.x = 10
print(obj.x)
obj._x = "huhu"
print(obj.x)
print()