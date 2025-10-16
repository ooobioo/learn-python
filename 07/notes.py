
print( frozenset( (1,2,3) ) > {3,4})
print( frozenset( (1,2,3) ) > {3,4} or set())

##############

x = [ 1,2,3 ]
y = x
z = y[:]

print(x==z, x is z)

x[0:0] = z[1:2] # bei [0:0] wird vor index 0 eingefügt
print(y)

x[2:2] = [6] # bei [2:2] wird vor index 2 eingefügt
print(y)

x[2:2] = [] # bei [2:2] wird vor index 2 eingefügt
print(y)

##############

a = {} # das ist keine leere menge, sondern ein leeres dictionary
b = {3,4,5}

# print(a | b) # TypeError

a = set() # eine leere menge wird mit set() dargestellt
b = {3,4,5}

print(a | b)

##############

a = { 2,3 }
b = { 3,4,5 }

print(a|b, a^b)
print(a|b, a-b)
print(a|b, a&b)

print({1, 2, 3, 4} - {2, 4, 5})
print({1, 2, 3, 4} ^ {2, 4, 5})


#  NAMENSRAUEME  ########################################

print()

# nonlocal
# die variable  wird nicht lokal angelegt
# sucht die variable in allen anderen übergeordnetem namensräumen von innen nach außen - außer dem globalen namensraum, dieser wird nicht durchsucht



def func1():
    num = 3.0
    print(num, end=" | ")

def func2(x):
    x = 3.0
    print(x, end=" | ")

num = 1.0
func1()
print(num)

num = 1.0
func2(num)
print(num)

l = [1,2,3]

def do_something(l: list):
    l.append(22)

print(l)
do_something(l)
print(l)


# LAMBDA

f = lambda x: 10
print(f(20))

l = ["banana","pear","grapes","apple"]

print(sorted(l,key=lambda x:x[::-1])) # sortiert nach dem letzten buchstaben im string
# die liste wird in key zu ananab, raep .... umgewandelt und dann sortiert
# sorted is quasi ein loop über alle elemente in der liste

k = l[::-1]
print(k)

print()

a,b = 10,20
print("1", a,b)
print("2", (lambda: b, lambda: a))
print("3", [0x70465cbec16 < 0x70465cbec0d0])
print("4", (lambda: b, lambda: a)[a<b])
print("5", (lambda: b, lambda: a)[a<b]())

# (lambda: b, lambda: a) - ein tuple mit zwei funktionsobjekten
# (lambda: b, lambda: a)[a<b] - [a<b] -> [True] -> [1] - position 1 des tuples wird angesprochen
# (lambda: b, lambda: a)[a<b]() - über die runden klammern am ende wird die funktion an postion 1 im tuple aufgerufen



# REKURSION #################################################
# eine funktion, die sich selbst aufruft. bis eine abbruchbedingung erfüllt ist

print()

def fib(k):
    if k <= 1:
        return k
        
    return fib(k-1) + fib(k-2)

# print("Fibonacci: ", fib(10))

for i in range(40):
    print(str(i).rjust(3), "{:,}".format(fib(i)).replace(",", ".").rjust(15))
