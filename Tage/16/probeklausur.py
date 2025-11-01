
tup = (1,2,3)
li = [1,2,3]

# lenx = len(tup)
# ind = tup.index()
# ind = index(tup)
# sorta = sort(tup)
# sortb = sorted(tup)

# lenx = len(li)
# ind = li.
# sorta = li.sort
# sortb = sorted(li)


def zerleg(s):
    wortliste = s.split(" ")
    rueck = []
    for wort in wortliste:
        rueck.append(wort[::-1])
    return rueck

print(zerleg("eins zwei drei"))

from random import randint

def random_char():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    list_gleiche_chars = []
    counter = 0
    while len(list_gleiche_chars) < 3:
        rand_char = alphabet[randint(0, len(alphabet)-1)]
        if rand_char not in list_gleiche_chars:
            list_gleiche_chars.clear()
        list_gleiche_chars.append(rand_char)
        counter += 1
    return counter

print(random_char())