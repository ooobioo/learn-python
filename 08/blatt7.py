
CONST = "yxz123"


def plattmachen2(li: list):
    ergebnis = []
    for el in li:
        if isinstance(el, list):
            ergebnis.extend(plattmachen2(el))
        else:
            ergebnis.append(el)
    return ergebnis
