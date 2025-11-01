print("### 1 #############")

def params_2_test(f):
    try:
        f(1, 2)
        return True
    except Exception as e:
        return False

def func1(a,b):
    print(a,b)

def func2(a,b,c):
    print(a,b,c)

print(params_2_test(func1))
print(params_2_test(func2))


print("### 2 #############")

def siebenerwert(k):
    quersumme = 0
    for char in str(k):
        quersumme += int(char)
    print("Quersumme", quersumme)
    if quersumme > 10:
        return siebenerwert(quersumme)
    return quersumme == 7


print(siebenerwert(17))
print(siebenerwert(556))
print(siebenerwert(26))
print(siebenerwert(54556))


print("### 3 #############")

def is_happy(k):
    quadrate = 0
    # for char in str(k):
    #     quadrate += int(char)**2
    quadrate = sum(int(digit) for digit in k)
    print("Quadrate", quadrate)
    if quadrate > 10:
        return is_happy(quadrate)
    return quadrate == 1


def is_happy_number(n):
    seen = set()
    print("\nCheck", n)
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
        print("n", n)

    return n == 1

for i in range(1,10):
    print(i, is_happy_number(i))