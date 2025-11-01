print()

def func1():
    num = 3
    print(num, end=" | ")

def func2(x):
    x = x * 3
    print(x, end=" | ")

num = 1

print("BEFORE", num, end=" | ")
func1()
print("AFTER",num)

num = 4
print("BEFORE", num, end=" | ")
func2(num)
print("AFTER", num)

print()

###############

string = "abc"

print("BEFORE", string, end=" | ")
func2(string)
print("AFTER", string)

print()

###############

def do_something2(l: list):
    l.append(22)


l = [1,2,3]

print("BEFORE", l ,end=" | ")
do_something2(l)
print("AFTER",l)