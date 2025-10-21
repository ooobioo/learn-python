# Aufgabe
# Schreiben Sie ein Programm, das
# ● von der Tastatur einen Dateinamen dn als String einliest
# ● den Inhalt der Datei dn.txt einliest
# ● eine neue Datei dn10.txt erzeugt, die
# ● von jeder Originalzeile die maximal 10 ersten Zeichen 
# enthält.


def write_file(content: list):
    with open("dn10.txt", "w") as file:
        for el in content:
            file.writelines(f"{el[0]:.<24}: {el[1]}...\n")
        print("new file created!")


while True:
    user_input = input("Please enter a file name (or exit): ")

    if user_input == "exit":
        break

    file_name = user_input + ".csv"


    try:
        with open(file_name, "r") as file:
            content = []
            for row in file:
                row = row.strip()
                list = row.split(";")
                # print(f"{list[0]}: {list[1][0:20]}...")
                content.append([list[0], list[1][0:50]])
            # print(content)
            write_file(content)
    except Exception as e:
        print(f"{e}")



