# 1 #########################################################
print()
square_dict_30 = {x: x**2 for x in range(1, 31)}
print(square_dict_30)

li= {x for x in range(2, 36, 2)}
print(li)

def multi_rem(li, di: dict):
    for el in li:
        if el in di:
            di.pop(el)
    return di

print(multi_rem(li, square_dict_30))


# 2 #########################################################
print()

small_dict = {
    1: "Eins",
    2: "Zwei",
    3: "Drei",
    4: "",
    5: "Fuenf",
    665: "NOTB"
}

def rename_entry(di: dict, key, new_key):
    if new_key in di:
        return False
    
    value = di.get(key, "Key not found")
    if value != "Key not found":
        di.pop(key)
        di[new_key] = value
        return di
    else:
        return value

print(small_dict)
print(rename_entry(small_dict,4,666))


# 3 #########################################################
print()

def schlsl_oder_falsch(di, x):
    if x in di:
        return type(di[x])
    return False

print(schlsl_oder_falsch(small_dict, 2))
print(schlsl_oder_falsch(small_dict, 22))

# 4 #########################################################
print()

string = "Ich koche heute 5, 6 oder 80 Kartoffeln."

def zahlen(string: str):
    # woerter = string.split()
    # list_zahlen = []
    # for wort in woerter:
    #     if wort.isnumeric():
    #         list_zahlen.append(wort)
    # return list_zahlen
    
    return [word for word in string.replace(",", "").split() if word.isnumeric()]

print(zahlen(string))

# 5 #########################################################
print()

# result = string.index("hete")
# print(result)


result = string.find("heute")
print(result)

############################################
# index -> ValueError: substring not found
# find -> -1

result = string.rindex("heute")
print(result)

result = string.rfind("heute")
print(result)

# die ausgaben von index(), rindex() und find(), rfind() sind jeweils identisch


# 6 #########################################################
print()
string2 = "Ich koche heute keine Kartoffeln."
string3 = "5678"

def bst_num(s: str):
    has_letter = any(char.isalpha() for char in s)
    has_digit = any(char.isdigit() for char in s)
    return has_letter and has_digit

print(bst_num(string))
print(bst_num(string2))
print(bst_num(string3))