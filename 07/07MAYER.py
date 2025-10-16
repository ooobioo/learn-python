# plattmachen

liste = [[1,2],3,[4,[5,6]],7]

def plattmachen1(l: list):
    ergebnis = []
    def machplatt(l: list):
        nonlocal ergebnis
        for el in l:
            if type(el) == list:
                machplatt(el)
            else:
                ergebnis.append(el)
    machplatt(l)
    return ergebnis

print("Platt1:", plattmachen1(liste))


def plattmachen2(l: list):
    ergebnis = []
    for el in l:
        if type(el) == list:
            ergebnis.extend(plattmachen2(el))
        else:
            ergebnis.append(el)
    return ergebnis

print("Platt2:", plattmachen2(liste))