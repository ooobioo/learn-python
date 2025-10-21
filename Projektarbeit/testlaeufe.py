import time
import datetime

MIN_MULTIPLIER, MAX_MULTIPLIER = 1, 100
MIN_ROUNDS, MAX_ROUNDS = 1, 100
multiplier = 1
rounds = 1

TYPES = ["String", "Integer", "List"]
timing_data = {t: {"Name": t, "Timings": {"For": [], "While": []}} for t in TYPES}


def do_something(k):
    return hash(k) % 10


def run_while(liste):
    counter = 0
    start = time.perf_counter()
    while counter < len(liste):
        some_value = do_something(counter)
        if str(some_value) == "testword":
            print("something")
        counter += 1
    end = time.perf_counter()
    compute_time = round(end-start, 4)
    return compute_time


def run_for(liste):
    start = time.perf_counter()
    for i in range(len(liste)):
        some_value = do_something(i)
        if str(some_value) == "testword":
            print("something")
    end = time.perf_counter()
    compute_time = round(end-start, 4)
    return compute_time


def read_file():
    with open("numbers.csv", "r") as file:
        start = time.perf_counter()
        # loop over all rows in the file and create the string list without the \n character at the end
        rows = [line.strip() for line in file]
        str_list = [f"{i}{row}" for row in rows for i in range(1, multiplier + 1)]
        # take the string list and create int and list lists
        int_list = [int(x) for x in str_list]
        list_list = [[x] for x in str_list]
        end = time.perf_counter()
        print("\n### IMPORT")
        print(f"Importing file and creating three lists with {len(str_list):,}".replace(",","."), end=" ")
        print(f"elements took: {round(end-start, 3)}s\n")
    return str_list, int_list, list_list


def calculate_mean(numbers: list):
    return round(sum(numbers)/len(numbers),4)


def calculate_deviation(a,b):
    return f"{round(abs(a - b) / a * 100, 1)}%"


def print_with_four_digits(number):
    return f"{number:.4f}"


def create_separator():
    return 120 * "-"


def create_header():
    separator = create_separator()
    header = create_row_template(["Anzahl", "Typ", "Durchlauefe", "Mittelwert FOR", "Mittelwert WHILE", "Abweichung"])
    return separator + "\n" + header + "\n" + separator 


def create_row(data: list):
    length = f"{data[0]:,}".replace(",",".")
    mean_for = calculate_mean(data[2]['Timings']['For'])
    mean_while = calculate_mean(data[2]['Timings']['While'])
    row = create_row_template([length, data[2]['Name'], data[1], print_with_four_digits(mean_for), print_with_four_digits(mean_while), calculate_deviation(mean_for, mean_while)])
    return row


def create_row_template(fields):
    return ''.join(f"{f:<20}" for f in fields)


def create_table(liste: list):
    header = create_header() 
    table_data = "\n"
    for el in liste:
        table_data = table_data + create_row(el) + "\n"
    return header + table_data


def write_file(content):
    start = time.perf_counter()
    with open("ausgabe.txt", "a") as file:
        file.write("\n" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "\n")
        file.write(content)
    end = time.perf_counter()
    print(f"Write to file with {len(content):,}".replace(",","."), end=" ")
    print(f"characters took {round(end-start,4)}s")


while True:
    print()
    multiplier = input(f"Wie oft soll die Liste vervielfacht werden ({MIN_MULTIPLIER} bis {MAX_MULTIPLIER} - oder Ende zum Beenden): ")
    if multiplier.lower() == "ende":
        break

    try:
        if int(multiplier) not in range(MIN_MULTIPLIER, MAX_MULTIPLIER+1):
            print(f"Invalid input – the value must be between {MIN_MULTIPLIER} and {MAX_MULTIPLIER}.")
            continue
        multiplier = int(multiplier)
    except Exception as e:
        print(f"Something's wrong with your input: {multiplier} - {e} ")
        continue

    rounds = input(f"Wieviele Wiederholungen sollen durchlaufen werden ({MIN_ROUNDS} bis {MAX_ROUNDS}):  ")
    try:
        if int(rounds) not in range(MIN_ROUNDS, MAX_ROUNDS+1):
            print(f"Invalid input – the value must be between {MIN_ROUNDS} and {MAX_ROUNDS}.")
            continue
        rounds = int(rounds)
    except Exception as e:
        print(f"Something's wrong with your input: {rounds} - {e} ")
        continue

    str_list, int_list, list_list = read_file()

    for i in range(rounds):
        timing_data["String"]["Timings"]["For"].append(run_for(str_list))
        timing_data["String"]["Timings"]["While"].append(run_while(str_list))
        timing_data["Integer"]["Timings"]["For"].append(run_for(int_list))
        timing_data["Integer"]["Timings"]["While"].append(run_while(int_list))
        timing_data["List"]["Timings"]["For"].append(run_for(list_list))
        timing_data["List"]["Timings"]["While"].append(run_while(list_list))

    table = create_table([[len(str_list), rounds, timing_data["String"]], [len(int_list), rounds, timing_data["Integer"]], [len(list_list), rounds, timing_data["List"]]])
    print(table)
    write_file(table)
