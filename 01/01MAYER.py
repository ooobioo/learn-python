# 1 ################################################################################
def my_printfunction1():
    print("Hallo!")
    print("Willkommen zu Python.")

def my_printfunction2():
    print("Hallo!\nWillkommen zu Python.")

def my_printfunction3():
    print("Hallo!","Willkommen zu Python.", sep="\n")

my_printfunction1()
my_printfunction2()
my_printfunction3()



# 2 ################################################################################
eingabe = input("Ihre Eingabe bitte: ")
print("Das war die Eingabe: ", eingabe)
print()



# 3 ################################################################################
PROMPT_1 = "Erste Zahl: "
PROMPT_2 = "Zweite Zahl: "
TEXT_SUMME = "Die Summe:"
TEXT_PRODUKT = "Das Produkt:"

# 3A #####################################
# Simple solution without type check
zahl1 = float(input(PROMPT_1))
zahl2 = float(input(PROMPT_2))

# Print results
print(TEXT_SUMME, zahl1 + zahl2, TEXT_PRODUKT, zahl1 * zahl2)
print()

# 3B #####################################
# Complex solution with type check and docstring
def sum_two_numbers(a: float, b: float) -> float:
    """
    Sums two numbers and returns the result rounded to 2 decimals.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of a and b rounded to 2 decimals.
    """
    return round(a + b, 2)

def multiply_two_numbers(a: float, b: float) -> float:
    """
    Multiplies two numbers and returns the result rounded to 2 decimals.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The product of a and b rounded to 2 decimals.
    """
    return round(a * b, 2)

def get_float_input(prompt: str) -> float:
    """
    Prompts the user to enter a floating-point number with input validation.

    Repeatedly asks the user for input until a valid float is entered. 
    If the input is invalid, prints an error message and asks again.

    Args:
        prompt (str): The message displayed to the user when asking for input.

    Returns:
        float: The user-entered value converted to a float.
    """
    while True:
        eingabe = input(prompt)
        try:
            return float(eingabe)
        except ValueError:
            print("Das war keine gültige Zahl!")

# Input with type check
zahl1 = get_float_input(PROMPT_1)
zahl2 = get_float_input(PROMPT_2)

# Print results rounded to 2 decimals
print(TEXT_SUMME, sum_two_numbers(zahl1, zahl2), TEXT_PRODUKT, multiply_two_numbers(zahl1, zahl2))
print()