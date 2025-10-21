import time

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
        counter += 1
    end = time.process_time()
    compute_time = round(end-start, 4)
    print(f"While loop: {compute_time}s")
    return compute_time

def run_for(liste):
    start = time.process_time()
    for i in range(len(liste)):
        some_value = do_something(liste[100])
    end = time.process_time()
    compute_time = round(end-start, 4)
    print(f"For loop: {compute_time}s")
    return compute_time


def read_file():
    str_list= []
    int_list = []
    list_list = []
    with open("numbers.csv", "r") as file:
        start = time.process_time()
        for row in file:
            str_list.append(row)
            int_list.append(int(row))
            list_list.append([row])
        end = time.process_time()
        print("### IMPORT")
        print(f"Importing file with {len(str_list)} rows took: {round(end-start, 3)}s")
    print()

    print("### STRINGS")
    run_for(str_list)
    run_while(str_list)
    print()

    print("### INTEGER")
    run_for(int_list)
    run_while(int_list)
    print()

    print("### LIST")
    run_for(list_list)
    run_while(list_list)
    print()

    return

print()
read_file()