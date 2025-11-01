
# x = """ # Error

vect = ["alpha", "bravo", "charlie"]

# der filter nimmt jeden string aus vect und schaut ob es im uppercase des strings an pos -1 ein A oder O gibt
new_vec = filter(lambda s: s[-1].upper() in ["A", "O"], vect)

print()
for x in new_vec:
    print(x[1], end=" ")
print()

if(len(vect) > 1):
    xx = 0
    assert xx == 0
else:
    print("nix")

import platform
print("Platform:",platform.platform())
print("System:",platform.system())
print("Version:",platform.version())
print("Release:",platform.release())
# print("Machine",platform.machine())
# print(platform.python_version_tuple())


import random

x = random.choice([10,20,30])
print(x)
try:
    print(x)
finally:
    print("fin")


# i = 0
# while i < (i + 2):
#     print(i)
#     i += 1

x = 1
x = x == x
print(x)

print(float("1.3"))
x = "60"
x += 2 + 1

print(x )

x = "halo"

print(x[-2])

print(9 // 2)
print(4 / 2)
print(9 // 2 * 2 / 2)
print(12 % 2)
print(2 ** 3)
print(12 % 2 ** 3)
print(9 // 2 * 2 / 2 + 12 % 2 ** 3)