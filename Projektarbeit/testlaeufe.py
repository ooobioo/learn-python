import time
import datetime
from pathlib import Path
import concurrent.futures

MIN_MULTIPLIER, MAX_MULTIPLIER = 1, 100
MIN_ROUNDS, MAX_ROUNDS = 1, 100
TYPES = ["String", "Integer", "List"]


def do_something(s: str) -> str:
    return s * 2


def run_for(items: list) -> float:
    start = time.perf_counter()
    for el in items:
        some_value = do_something(el[0] if isinstance(el, list) else el)
        if some_value == 0:
            print("something")
    end = time.perf_counter()
    return round(end - start, 4)


def run_while(items: list) -> float:
    counter = 0
    list_length = len(items)
    start = time.perf_counter()
    while counter < list_length:
        some_value = do_something(items[counter][0] if isinstance(items[counter], list) else items[counter])
        if some_value == 0:
            print("something")
        counter += 1
    end = time.perf_counter()
    return round(end - start, 4)


def read_file(filename: str = "input.csv", multiplier: int = 1) -> tuple[list[str], list[int], list[list[str]]]:
    if not filename:
        filename = "numbers.csv"
    path = Path(filename)
    start = time.perf_counter()
    try:
        with path.open("r", encoding="utf-8") as file:
            rows = [line.strip() for line in file]
    except Exception:
        print(f"File {filename} not found")
        raise

    str_list = [f"{i}{row}" for row in rows for i in range(1, multiplier + 1)]
    int_list = [int(x) for x in str_list]
    list_list = [[x] for x in str_list]

    end = time.perf_counter()
    print("\n### IMPORT")
    print(f"Importing file and creating three lists with {len(str_list):,}".replace(",", "."), f"elements took: {end - start:.2f}s\n")
    return str_list, int_list, list_list


def calculate_mean(numbers: list) -> float:
    return round(sum(numbers) / len(numbers), 4)


def calculate_deviation(a, b) -> str:
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


def write_file(content: str, runtime: str, parallel_excecution: str, filename: str = "output.txt") -> None:
    start = time.perf_counter()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as file:
        file.write("#" * 70 + "\n")
        file.write(timestamp + "  |  parallel execution: " + parallel_excecution + "  |  Laufzeit: " + runtime + "\n")
        file.write(content + "\n" * 2)
    duration = time.perf_counter() - start
    print(f"\nWrote {len(content):,} characters to {filename} in {duration:.4f}s".replace(",", "."))


# Define top-level timing functions for ProcessPoolExecutor

def time_strings(str_list, rounds):
    results = {"For": [], "While": []}
    for _ in range(rounds):
        results["For"].append(run_for(str_list))
        results["While"].append(run_while(str_list))
    return results


def time_integers(int_list, rounds):
    results = {"For": [], "While": []}
    for _ in range(rounds):
        results["For"].append(run_for(int_list))
        results["While"].append(run_while(int_list))
    return results


def time_lists(list_list, rounds):
    results = {"For": [], "While": []}
    for _ in range(rounds):
        results["For"].append(run_for(list_list))
        results["While"].append(run_while(list_list))
    return results


def wrapper(func_args):
    func, *args = func_args
    return func(*args)


def main():
    print()
    timing_data = {t: {"Name": t, "Timings": {"For": [], "While": []}} for t in TYPES}

    def clear_timings():
        timing_data["String"]["Timings"]["For"].clear()
        timing_data["String"]["Timings"]["While"].clear()
        timing_data["Integer"]["Timings"]["For"].clear()
        timing_data["Integer"]["Timings"]["While"].clear()
        timing_data["List"]["Timings"]["For"].clear()
        timing_data["List"]["Timings"]["While"].clear()

    clear_timings()

    while True:
        multiplier = input(f"Wie oft soll die Liste vervielfacht werden ({MIN_MULTIPLIER} bis {MAX_MULTIPLIER} - oder Ende zum Beenden): ")
        if multiplier.lower() == "ende":
            break

        try:
            if int(multiplier) not in range(MIN_MULTIPLIER, MAX_MULTIPLIER + 1):
                print(f"Invalid input – the value must be between {MIN_MULTIPLIER} and {MAX_MULTIPLIER}.")
                continue
            multiplier_int = int(multiplier)
        except Exception as e:
            print(f"Something's wrong with your input: {multiplier} - {e}")
            continue

        rounds = input(f"Wieviele Wiederholungen sollen durchlaufen werden ({MIN_ROUNDS} bis {MAX_ROUNDS}):  ")
        try:
            if int(rounds) not in range(MIN_ROUNDS, MAX_ROUNDS + 1):
                print(f"Invalid input – the value must be between {MIN_ROUNDS} and {MAX_ROUNDS}.")
                continue
            rounds_int = int(rounds)
        except Exception as e:
            print(f"Something's wrong with your input: {rounds} - {e}")
            continue

        filename = input(f"Welche Datei moechten sie einlesen:  ")
        try:
            str_list, int_list, list_list = read_file(filename=filename, multiplier=multiplier_int)
        except Exception as e:
            print(e)
            break

        parallel_excecution = input(f"Soll der Code parallel ausgeführt werden (yes/no):  ")

        if parallel_excecution.lower() not in ["yes", "no"]:
            print(f"Invalid input – the value must be yes or no.")
            continue

        start = time.perf_counter()

        if parallel_excecution.lower() == "yes":
            with concurrent.futures.ProcessPoolExecutor() as executor:
                results = executor.map(
                    wrapper,
                    [
                        (time_strings, str_list, rounds_int),
                        (time_integers, int_list, rounds_int),
                        (time_lists, list_list, rounds_int),
                    ],
                )
                str_timings, int_timings, list_timings = results

            timing_data = {
                "String": {"Name": "String", "Timings": str_timings},
                "Integer": {"Name": "Integer", "Timings": int_timings},
                "List": {"Name": "List", "Timings": list_timings},
            }

        else:
            for _ in range(rounds_int):
                timing_data["String"]["Timings"]["For"].append(run_for(str_list))
                timing_data["String"]["Timings"]["While"].append(run_while(str_list))
                timing_data["Integer"]["Timings"]["For"].append(run_for(int_list))
                timing_data["Integer"]["Timings"]["While"].append(run_while(int_list))
                timing_data["List"]["Timings"]["For"].append(run_for(list_list))
                timing_data["List"]["Timings"]["While"].append(run_while(list_list))

        table = create_table(
            [
                [len(str_list), rounds_int, timing_data["String"]],
                [len(int_list), rounds_int, timing_data["Integer"]],
                [len(list_list), rounds_int, timing_data["List"]],
            ]
        )
        print(table)
        end = time.perf_counter()
        runtime = f"{end - start:.2f}s".replace(",", ".")
        write_file(table, runtime, parallel_excecution)
        print("\n### PROCESSING DATA")
        print(f"Processing took: {runtime}")
        clear_timings()


if __name__ == "__main__":
    main()
