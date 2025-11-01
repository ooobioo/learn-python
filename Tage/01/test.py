print("hello")

print("hello", "du")

print("hello", "du", sep="---")

print("hello", "du", sep="---", end=".\n")

eingabe = input("Please enter something: ")
print(eingabe)

number = int(input("Please enter a number: "))
print(number)


# kommentar
if number == 1:
    print("if")
elif number == 2: 
    print("elif") # kommentar
else:
    print("else")


def my_function():
  print("Hello from a function")

my_function()

def my_printfunction():
    print("Hallo!")
    print("Willkommen zu Python")
    print("Hallo!\nWillkommen zu Python")
    print("Hallo!","Willkommen zu Python", sep="\n")

my_printfunction()