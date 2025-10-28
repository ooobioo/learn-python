import time
import datetime
from pathlib import Path
# from multiprocessing import Pool
import concurrent.futures


MIN_MULTIPLIER, MAX_MULTIPLIER = 1, 100
MIN_ROUNDS, MAX_ROUNDS = 1, 100
TYPES = ["String", "Integer", "List"]

multiplier = 1
rounds = 1
timing_data = {t: {"Name": t, "Timings": {"For": [], "While": []}} for t in TYPES}

str_timings = None
int_timings = None
list_timings = None


def do_something(s: str) -> str:
    return s*2


def run_for(items: list) -> float:
    # counter = 0
    start = time.perf_counter()
    for el in items:
        if(isinstance(el, list)):
            some_value = do_something(el[0])
        else:
            some_value = do_something(el)
        if some_value == "0":
            print("something")
        # counter += 1
    end = time.perf_counter()
    compute_time = round(end-start, 4)
    return compute_time


def run_while(items: list) -> float:
    counter = 0
    list_length = len(items)
    start = time.perf_counter()
    while counter < list_length:
        if(isinstance(items[counter], list)):
            some_value = do_something(items[counter][0])
        else:
            some_value = do_something(items[counter])
        if some_value == "0":
            print("something")
        counter += 1
    end = time.perf_counter()
    compute_time = round(end-start, 4)
    return compute_time


def read_file(filename: str = "input.csv", multiplier: int = 1) -> tuple[list[str], list[int], list[list[str]]]:
    if filename == "":
        filename = "numbers.csv"

    path = Path(filename)
    start = time.perf_counter()

    # Read lines stripping trailing whitespace
    try:
        with path.open("r", encoding="utf-8") as file: rows = [line.strip() for line in file]
    except Exception:
        print(f"File {filename} not found")
        raise

    # Generate repeated strings
    str_list = [f"{i}{row}" for row in rows for i in range(1, multiplier + 1)]

    # Convert strings to integers
    int_list = [int(x) for x in str_list]

    # Create list of single-item lists of strings
    list_list = [[x] for x in str_list]

    end = time.perf_counter()
    print("\n### IMPORT")
    print(f"Importing file and creating three lists with {len(str_list):,}".replace(",", "."), f"elements took: {end - start:.2f}s\n")

    return str_list, int_list, list_list


def calculate_mean(numbers: list) -> float:
    return round(sum(numbers)/len(numbers),4)


def calculate_deviation(a,b) -> str:
    return f"{round(abs(a - b) / a * 100, 1)}%"


def number_with_four_digits(number) -> str:
    return f"{number:.4f}"


def create_separator() -> str:
    return 120 * "-"


def create_header() -> str:
    columns = [
        "Anzahl",
        "Typ",
        "Durchläufe",
        "Mittelwert FOR",
        "Mittelwert WHILE",
        "Abweichung",
    ]
    header_row = format_row(columns)
    separator = create_separator()
    return f"{separator}\n{header_row}\n{separator}"


def create_row(items: list) -> str:
    list_length, rounds, metrics = items

    list_length_str = f"{list_length:,}".replace(",", ".")
    timings = metrics.get("Timings", {})
    datatype = metrics.get("Name", "N/A")

    mean_for = calculate_mean(timings.get("For", []))
    mean_while = calculate_mean(timings.get("While", []))
    deviation = calculate_deviation(mean_for, mean_while)

    values = [
        list_length_str,
        datatype,
        rounds,
        number_with_four_digits(mean_for),
        number_with_four_digits(mean_while),
        deviation,
    ]
    return format_row(values)


def format_row(fields: list) -> str:
    return "".join(f"{f:<20}" for f in fields)


def create_table(items: list) -> str:
    header = create_header()
    rows = (create_row(item) for item in items)
    footer = create_separator()
    table_data = "\n".join(rows)
    return f"{header}\n{table_data}\n{footer}\n"


def write_file(content: str, runtime: str, filename: str = "output.txt") -> None:
    start = time.perf_counter()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as file:
        file.write("#"*70 + "\n")
        file.write(timestamp + "  |  parallel execution: " + parallel_excecution +  "  |  Laufzeit: " + runtime + "\n")
        file.write(content +"\n"*2)
    duration = time.perf_counter() - start
    print(f"\nWrote {len(content):,} characters to {filename} in {duration:.4f}s".replace(",", "."))



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
    
    filename = input(f"Welche Datei moechten sie einlesen:  ")
    try:
        str_list, int_list, list_list = read_file(filename=filename, multiplier=multiplier)
    except Exception as e:
        print(e)
        break

    parallel_excecution = input(f"Soll der Code parallel ausgeführt werden (yes/no):  ")
    if parallel_excecution.lower() not in ["yes", "no"]:
        print(f"Invalid input – the value must be between yes or no.")
        continue

    start = time.perf_counter()

    if parallel_excecution.lower() == "yes":
        def time_strings():
                results = {"For": [], "While": []}
                for _ in range(rounds):
                    results["For"].append(run_for(str_list))
                    results["While"].append(run_while(str_list))
                return results

        def time_integers():
            results = {"For": [], "While": []}
            for _ in range(rounds):
                results["For"].append(run_for(int_list))
                results["While"].append(run_while(int_list))
            return results

        def time_lists():
            results = {"For": [], "While": []}
            for _ in range(rounds):
                results["For"].append(run_for(list_list))
                results["While"].append(run_while(list_list))
            return results

        with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
            future_str = executor.submit(time_strings)
            future_int = executor.submit(time_integers)
            future_lst = executor.submit(time_lists)

            str_timings = future_str.result()
            int_timings = future_int.result()
            list_timings = future_lst.result()

        timing_data = {
            "String": {"Name": "String", "Timings": str_timings},
            "Integer": {"Name": "Integer", "Timings": int_timings},
            "List": {"Name": "List", "Timings": list_timings},
        }

    else:   
        for i in range(rounds):
            # strings
            timing_data["String"]["Timings"]["For"].append(run_for(str_list))
            timing_data["String"]["Timings"]["While"].append(run_while(str_list))
            # integer
            timing_data["Integer"]["Timings"]["For"].append(run_for(int_list))
            timing_data["Integer"]["Timings"]["While"].append(run_while(int_list))
            # lists
            timing_data["List"]["Timings"]["For"].append(run_for(list_list))
            timing_data["List"]["Timings"]["While"].append(run_while(list_list))


    table = create_table([[len(str_list), rounds, timing_data["String"]], [len(int_list), rounds, timing_data["Integer"]], [len(list_list), rounds, timing_data["List"]]])
    print(table)
    end = time.perf_counter()
    runtime = f"{end-start:.2f}s".replace(",", ".")
    write_file(table, runtime)
    print("\n### PROCESSING DATA")
    print(f"Processing took: {runtime}")

