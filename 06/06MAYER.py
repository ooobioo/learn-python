# 1 ######################################

string = "heute kommen 1, 2 oder 3 freunde zu besuch"

def zahlen(s: str):
    return [word for word in s.replace(",","").split() if word.isnumeric()]

print(zahlen(string))


# 2 #######################################
print()

string = "wo ist der text"

print("Gesuchter Index:",string.index("st"))
# print("Gesuchter Index:",string.index("p")) # Value Error, Programm bricht ab
print("Gesuchter Index:",string.find("st"))
print("Gesuchter Index:",string.find("p")) # Rueckgabewert -1


string = "huhu Xaba Z aba X aY"
print(string.index("aba"))
print(string.find("aba"))
print(string.rindex("aba"))
print(string.rfind("aba"))
print()
print(string.index("X"))
print(string.find("X"))
print(string.rindex("X"))
print(string.rfind("X"))
print()
print(string.index("Z"))
print(string.find("Z"))
print(string.rindex("Z"))
print(string.rfind("Z"))

# rfind( ) und rindex( ) suchen von hinten. Wann ist ihre 
# Ausgabe dieselbe wie bei find( ) und index( )?
# -> die ausgabe ist gleich wenn der gesuchte teilstring nur einmal vorkommt


# 3 #######################################
print()
def bst_num(s: str):
    has_letter = False
    has_digit = False
    for char in s:
        if char.isalpha():
            has_letter = char.isalpha()
        if char.isdigit():
            has_digit = char.isdigit()

    return has_letter & has_digit

    # has_letter = any(char.isalpha() for char in s)
    # has_digit = any(char.isdigit() for char in s)
    # return has_letter and has_digit

string1 = "ich will 2 pizza"
string2 = "ich will keine pizza"

print(bst_num(string1))
print(bst_num(string2))

# 4 #######################################
print()

def division(a: int,b: int):
    div = divmod(a,b)
    return f"{a} geteilt durch {b} ist {div[0]} mit Rest {div[1]}"

print(division(21,3))
print(division(203,3))
print(division(42203,30))


# 5 ########################################
print()
zahlen = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

def gerade(li: list):
    return list(filter(lambda x: x % 2 == 0, li))

print(gerade(zahlen))

# 6 ########################################
print()

def vokale(s: str):
    list_vokale = ["a","e","i","o","u"]
    return list(filter(lambda x: x in list_vokale, s))

string = "heute ist ein schoener tag"

print(vokale(string))