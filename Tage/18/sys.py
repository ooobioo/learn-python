import sys

def mw(a, b):
    return (int(a) + int(b)) / 2

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 script.py <number1> <number2>")
        sys.exit(1)

    if len(sys.argv) != 3:
        print("Usage: python3 script.py <number1> <number2>")
        sys.exit(1)

    _, a, b = sys.argv

    try:
        print(mw(a, b))
    except:
        print("hier stimmt was nicht")


if __name__ == "__main__":
    main()