while True:
    userinput = input("Bitte geben sie ein Stadt ein (oder Ende zum beenden): ")

    if userinput == "Ende":
        break

    with open("daten.csv", "r") as myfile:
        response = ""
        for row in myfile:
            row = row.strip()
            data = (row.split(";"))
            try:
                data.index(userinput)
                response = f"{data[0]} | {data[1]}°C | {data[2]}ml Niederschlag"
                break
            except ValueError:
               response = "kein Datensatz gefunden - weiter..."

        print(response)

