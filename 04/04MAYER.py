# 1 #############################################
def teilbare1(top,dividend):
    li = []
    for zahl in range(1, top):
        if zahl % dividend == 0:
            li.append(zahl)
    return li

def teilbare2(top,dividend):
    return [zahl for zahl in range(1,top) if zahl % dividend == 0]

print(teilbare1(100,7))
print(teilbare2(100,7))
print()

# 2 #############################################
li = [3.4, 0.2, 1.0, 33.1, 4.0]

def ganzzahlen(liste):
    li = []
    for zahl in liste:
        if (zahl - int(zahl)) == 0:
            li.append(int(zahl))
    
    return li

print(ganzzahlen(li))
print()

# 3 #############################################
def anfang_und_ende(seq_obj):
    first, *other, last = seq_obj
    return first, last, other

tup = (1,"ab",3, "c")
print(anfang_und_ende(tup))