class Vermenge():
    def __init__(self):
        self.__mengwert = 0
        self._x = 0
        print(__name__)
    
    def __str__(self):
        return f"mengwert: {self.__mengwert } x:{self._x}"
    
    @staticmethod
    def m():
        print("Hallo!")

    @classmethod
    def m(cls):
        print("Ich bin", cls)

    @property    
    def x(self):
        print("lese_y")
        return self._x
    
    @x.setter
    def x(self, k):
        print("setze_x")
        if isinstance(k,int):
            self._x = k
        else:
            raise TypeError("Kein Int")

    def get_mengenwert(self):
        return self.__mengwert


class Gemenge(Vermenge):
    pass

vermengelt = Vermenge()
vermengelt.m()
vermengelt._x = 2

print(vermengelt.get_mengenwert())
vermengelt._Vermenge__mengwert = 1
print(vermengelt.get_mengenwert())

print("###############")

print(__name__)
print(Vermenge.__name__)
print(vermengelt.__class__.__name__)
print(vermengelt)

# print(Vermenge())
# print(Gemenge())



class A(object): pass
class B(object): pass
class C(object): pass
class D(object): pass
class E(object): pass
class K1(A,B,C): pass
class K2(D,B,E): pass
class K3(D,A): pass


# class Foo(K1,K2,K3): pass
# class Foo(K1,K3,K2): pass
# class Foo(K2,K1,K3): pass
# class Foo(K2,K3,K1): pass
class Foo(K3,K1,K2): pass

xy = Foo()

xxx = 1

print(isinstance(xxx, (str, float, int)))


class X: pass
class Y: pass
class Z(X, Y): pass
x, y, z = X(), Y(), Z()

print(type(z))

print(z.__class__.__mro__)

########################################

class Ham:
    def __init__(self):
        print(type(self).__name__ + '.__init__()', end=' ')
        self.__update()
      
    def update(self):
        print(type(self).__name__ + '.update()')
    __update = update  

Ham()

########################################


# class Gammelfehler(Exception):
#     pass

# def int_check(x):
#     if x > 10: raise Gammelfehler()

# int_check(33)

