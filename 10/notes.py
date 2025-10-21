print(type([1,2,3]))

d1 = dict(a=1, b=2)
d2 = {'a': 1, 'b': 2}
d3 = dict([('a',1), ('b',2)])

print(d1, d2, d3)



# RANDOM ############################
import random

x = "WELCOME"

# x = {x} #  eine menge/set ist nicht subscriptable / kann daher nicht iteriert werden
# A Python set is not subscriptable because sets are unordered collections.
# That means they don’t have a fixed order of elements — so indexing (e.g. myset[0]) doesn’t make sense.

print("Random:",random.choice(x))
print("Random:",random.choice(range(0,99)))

print(type((4)))
print(type((4,)))
print(type(range(0,99)))

print()

def f(k):
    i = 0
    while i < 5:
        try:
            i += k
        except:
            print("exception")
            return None
        finally:
            print("finally")

f("e")
print(f"{int(1e6):,}".replace(',', '.'))
print(int(1e6))