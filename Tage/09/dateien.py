inputfile = open("daten.csv", "r")

# print(type(inputfile))

print(inputfile.read(2))
inputfile.seek(0)
print("-")

print(inputfile.read())
inputfile.seek(0)
print("-")

print(inputfile.readlines())
inputfile.seek(0)
print("-")



for row in inputfile:
    row = row.strip()
    print(row.split(";")) # erstellt eine liste mit den elementen die durch semikolon getrennt sind

inputfile.close()

print("-")


with open("daten.csv", "r") as myfile:
    for row in myfile:
        row = row.strip()
        print(row.split(";"))

print("-")


with open("NewFile.txt", "r+") as outputFile:
    for i in range(0,2): 
        outputFile.write(f"Zeile    x {i} \n")


