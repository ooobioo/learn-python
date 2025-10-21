import time

multiplikator = 1
rounds = 1

di = {
    "String": {
        "Name": "String",
        "Timings": {
            "For": [],
            "While": []
        }
    },
    "Integer": {
        "Name": "Integer",
        "Timings": {
            "For": [],
            "While": []
        }
    },
    "List": {
        "Name": "List",
        "Timings": {
            "For": [],
            "While": []
        }
    },
}


def do_something(k):
    x = str(10*k)
    if x == True:
        return x
    else:
        return None


def run_while(liste):
    counter = 0
    start = time.process_time()
    while counter < len(liste):
        some_value = do_something(liste[100])
        if some_value == i:
            print("something")
        counter += 1
    end = time.process_time()
    compute_time = round(end-start, 4)
    return compute_time


def run_for(liste):
    start = time.process_time()
    for i in range(len(liste)):
        some_value = do_something(liste[100])
        if some_value == i:
            print("something")
    end = time.process_time()
    compute_time = round(end-start, 4)
    return compute_time


def read_file():
    str_list= []
    int_list = []
    list_list = []
    big_list = []
    with open("numbers.csv", "r") as file:
        start = time.process_time()
        # loop over all rows in the file
        for row in file:
            # multiply rows
            # take each row, add the number of i to the beginning and write to big_list
            for i in range(1, multiplikator+1):
                big_list.append(str(i) + row)
        # create the lists for different data types from big_list        
        for el in big_list:
            str_list.append(el)
            int_list.append(int(el))
            list_list.append([el])
        end = time.process_time()
        print("\n### IMPORT")
        print(f"Importing file and creating a list with {len(big_list):,}".replace(",","."), end=" ")
        print(f"elements took: {round(end-start, 3)}s")
    print()
    return str_list, int_list, list_list


def compare_loops(list):
    compute_time_for = run_for(list)
    compute_time_while = run_while(list)
    return compute_time_for, compute_time_while


def calculate_mean(numbers: list):
    return round(sum(numbers)/len(numbers),4)


def print_with_four_digits(number):
    return f"{number:.4f}"


def create_field(text: str):
    field = f"{text:<20}"
    return field


def create_separator():
    return 120 * "-"


def create_header():
    separator = create_separator()
    header = create_row_template(["Anzahl", "Typ", "Durchlauefe", "Mittelwert FOR", "Mittelwert WHILE", "Abweichung"])
    return separator + "\n" + header + "\n" + separator 


def calculate_abweichung(a,b):
    return f"{round(abs(a - b) / a * 100, 1)}%"


def create_row(data: list):
    length = f"{data[0]:,}".replace(",",".")
    row = create_row_template([length, data[2]['Name'], data[1], print_with_four_digits(calculate_mean(data[2]['Timings']['For'])), print_with_four_digits(calculate_mean(data[2]['Timings']['While'])), calculate_abweichung(calculate_mean(data[2]['Timings']['For']), calculate_mean(data[2]['Timings']['While']))])
    return row


def create_row_template(liste: list):
    string = ""
    for el in liste:
        string += create_field(el)
    return string


def create_table(liste: list):
    header = create_header() 
    table_data = "\n"
    for el in liste:
        table_data = table_data + create_row(el) + "\n"
    return header + table_data

def write_file(content):
    start = time.process_time()
    with open("ausgabe.txt", "a") as file:
        file.write(content)
    end = time.process_time()
    print(f"Write file with {len(content):,}".replace(",","."), end=" ")
    print(f"lines took {round(end-start, 3)}s")

while True:
    multiplikator = input("Wie oft soll die Liste vermehrfacht werden (1 bis 100) (oder Ende zum Beenden): ")
    if multiplikator.lower() == "ende":
        break

    try:
        if int(multiplikator) not in range(1,100):
            print("Invalid input – the value must be between 1 and 100.")
            continue
        multiplikator = int(multiplikator)
    except Exception as e:
        print(f"Something's wrong with your input: {multiplikator} - {e} ")
        continue

    rounds = input("Wieviele Wiederholungen sollen durchlaufen werden - (1 bis 100):  ")
    try:
        if int(rounds) not in range(1,100):
            print("Invalid input – the value must be between 1 and 100.")
            continue
        rounds = int(rounds)
    except Exception as e:
        print(f"Something's wrong with your input: {rounds} - {e} ")
        continue

    str_list, int_list, list_list = read_file()

    for i in range(rounds):
        di["String"]["Timings"]["For"].append(run_for(str_list))
        di["String"]["Timings"]["While"].append(run_while(str_list))
        di["Integer"]["Timings"]["For"].append(run_for(int_list))
        di["Integer"]["Timings"]["While"].append(run_while(int_list))
        di["List"]["Timings"]["For"].append(run_for(list_list))
        di["List"]["Timings"]["While"].append(run_while(list_list))

    table = create_table([[len(str_list), rounds, di["String"]], [len(int_list), rounds, di["Integer"]], [len(list_list), rounds, di["List"]]])
    print(table)
    write_file(table)
