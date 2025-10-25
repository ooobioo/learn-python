import time, random


def generate_integer_values(number_of_values: int = 10000) -> list:
    list = []
    start = time.perf_counter()
    while len(list) < number_of_values:
        numbers = random.sample(range(int(9e6)), number_of_values)
        list.extend(numbers)
    end = time.perf_counter()
    print(f"Generating {number_of_values:,}".replace(",","."), end=" ")
    print(f"values took {round(end-start, 3)}s")
    return list


def write_file(content: list) -> None:
    start = time.perf_counter()
    content_string = ""
    for el in content:
        content_string = content_string + str(el)+"\n"
    content_string = content_string[:-1]
    with open("numbers.csv", "w") as file:
        file.write(content_string)
    end = time.perf_counter()
    print(f"Write file with {len(content):,}".replace(",","."), end=" ")
    print(f"lines took {round(end-start, 3)}s")
    return


print()
print("### LISTE ERZEUGEN")
list = generate_integer_values(100000)
print()
print("### DATEI SCHREIBEN")
write_file(list)
print()