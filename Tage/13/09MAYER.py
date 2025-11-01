import datetime
import random

print("# 1 ######################")
class Person():
    def __init__(self, geburtsjahr=0, groesse=0, gewicht=0):
        self.geburtsjahr = geburtsjahr
        self.groesse = groesse
        self.gewicht = gewicht

    def alter(self):
        year = datetime.date.today().year
        return year - self.geburtsjahr

    def bmi(self):
        return round(self.gewicht / (self.groesse / 100) ** 2, 2)


person1 = Person(1974, 189, 90)

print("Alter:", person1.alter())
print("BMI:", person1.bmi())


print("# 2 ######################")
class Stack():
    def __init__(self):
        self.stack = []
    def ablegen(self, el):
        self.stack.append(el)
    def holen(self):
        el = self.stack[-1]
        self.stack.pop(-1)
        return el
    def hinten_schauen(self):
        return self.stack[-1]
    def vorne_schauen(self):
        return self.stack[0]
    def ist_leer(self):
        return len(self.stack) == 0
    def get_len(self):
        return len(self.stack)

mystack = Stack()
print("Leer:", mystack.ist_leer())
print("Laenge:",mystack.get_len())
mystack.ablegen(1)
print("Laenge:",mystack.get_len())
mystack.ablegen(2)
print("Laenge:",mystack.get_len())
print("Vorne schauen:",mystack.vorne_schauen())
print("Hinten schauen:",mystack.hinten_schauen())
print("Leer:", mystack.ist_leer())
print("Holen:", mystack.holen())
print("Hinten schauen:",mystack.hinten_schauen())


print("# 3 ######################")

class Warteschlange(Stack):
    def __init__(self):
        super().__init__()

    def einreihen(self, el):
        super().ablegen(el)

    def schauen(self):
        return super().vorne_schauen()

    def holen(self):
        el = self.schauen()
        self.stack.remove(el)
        return el


obj = Warteschlange()

print("Leer:", obj.ist_leer())

obj.einreihen(1)
obj.einreihen(2)
obj.einreihen(3)

print("Leer:", obj.ist_leer())
print("Schauen:", obj.schauen())
print("Holen:", obj.holen())
print("Schauen:", obj.schauen())


print("# 4 ######################")

class Spieler():
    def __init__(self, name):
        self.name = name
    def wuerfeln(self):
        wurf = random.randint(1,6)
        # return f"{self.name} würfelt {wurf}"
        return wurf



class Spielleiter():
    def __init__(self):
        self.names = ["Spieler1", "Spieler2", "Spieler3", "Spieler4"]
        self.spieler = {Spieler(spieler): 0 for spieler in self.names}
        self.ergebnisse = {spieler.name: 0 for spieler in self.spieler}

    def get_spielliste(self):
        return self.ergebnisse
    
    def spielen(self):
        wins = []
        for runde in range(1, 6):
            print(f"Runde {runde}")
            ergebnisse_runde = []
            for spieler in self.spieler:
                ergebnisse_runde.append(spieler.wuerfeln())
            print(ergebnisse_runde)
            winner = max(ergebnisse_runde)
            print("winner", winner)
            # index_winner = ergebnisse_runde.index(winner)
            # name_winner = self.ergebnisse[index_winner]
            # print("index_winner", index_winner)
            # wins.append(name_winner)
        # sieger = max(count(wins))
        # self.ergebnisse[winner] += 1
        return self.ergebnisse

gamemaster = Spielleiter()

print(gamemaster.get_spielliste())
# print(gamemaster.spielliste[0].wuerfeln())
print(gamemaster.spielen())