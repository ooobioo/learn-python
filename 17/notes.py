def outer_function(x):
    def inner_function(y):
        return x + y  # inner_function remembers x even after outer_function finishes
    return inner_function  # return the inner function (closure)

closure1 = outer_function(10)  # create a closure with x=10 / x wird beim funtionsaufruf eingeschlossen
print(closure1(5))  # Output: 15
print(closure1(20)) # Output

closure2 = outer_function(100)  # create a closure with x=100 / x wird beim funtionsaufruf eingeschlossen
print(closure2(5))  # Output: 15
print(closure2(20)) # Output


###################################



def create_counter():
    count = 0  # private variable

    def increment():
        nonlocal count
        count += 1
        return count

    def decrement():
        nonlocal count
        count -= 1
        return count

    def get_count():
        return count

    return increment, decrement, get_count

inc, dec, get = create_counter()

print(inc())  # 1
print(inc())  # 2
print(get())  # 2
print(dec())  # 1
# The variable 'count' is not accessible directly from outside
try:
    # print(count)
    print()
except NameError:
    print("count is not accessible outside the closure")


##########################


def intervallerzeuger(a: int, b: int):
    def inner(x):
        return True if a <= x < b else False
    return inner

closure3 = intervallerzeuger(5,10)
print(closure3(8))
print(closure3(15))



#################################
print("##### MEMOIZER\n")

def memoizer():
    memory = {} # nur immutable datentypen koennen keys eines dictionaries sein

    def calculator(x, y):
        if (x,y) not in memory:
            print(f"{(x,y)} ---> neu berechen")
            memory[(x,y)] = x ** y ** y
        else:
            print(f"{(x,y)} ---> nicht neu berechen")
        return memory[(x,y)]
    
    return calculator

func = memoizer()



print(func(2,3))
print(func(4,3))
print(func(2,3))
print(func(5,2))
print(func(5,2))
print(func(4,2))
print(func(4,3))

#################################

def rahmen ( anzahl ):
    li = []
    def runterzaehler():
        if len( li ) < anzahl:
            li.append( 'x' )
            return f"noch {anzahl - len( li )} Aufrufe"
        else:
           return "die Funktion ist jetzt verbraucht"
    return runterzaehler


f = rahmen(5)
print(f())
print(f())
print(f())
print(f())
print(f())
print(f())
print(f())


################


def merk_mir():
    gemerkt = []
    def summe(n):
        gemerkt.append(n)
        return sum(gemerkt)
    return summe

f = merk_mir()

print(f(10))
print(f(20))
print(f(30))
print(f(40))
print(f(50))
print(f(-110))