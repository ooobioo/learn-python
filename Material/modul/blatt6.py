""" Dies ist ein Modul

und cool """



blatt6wert = 237

def division(dividend, divisor):
    erg, rest = divmod(dividend, divisor)
    print(str(dividend) + " geteilt durch " 
          + str(divisor) + " ist ", end="")
    print(str(erg) + " Rest " + str(rest) + ".")

def numerier(li):
    for pos, wert in enumerate(li):
        print("Element " + str(pos) + " der Liste ist: " + str(wert) )


def gerade(li):
    return list(filter(lambda x: not x%2, li))

def vokale(string):
    return list(filter(lambda x: x in ["a","e","i","o","u"], string))




print("Hallo")
