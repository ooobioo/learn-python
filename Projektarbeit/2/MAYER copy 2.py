# import random
from random import randint

class Spieler():
    def __init__(self, name, id, spielstaerke):
        self.name = name
        self.id = id
        self.spielstaerke = spielstaerke

    def aufschlag(self):
        schlagstaerke = randint(0, self.spielstaerke)
        with open("game.log", "a") as file:
            file.write(f"  Aufschlag {self.name}: {schlagstaerke}\n")
        return schlagstaerke
    
    def schlag(self):
        schlagstaerke = randint(0, self.spielstaerke)
        with open("game.log", "a") as file:
            file.write(f"  Schlag {self.name}: {schlagstaerke}\n")
        return schlagstaerke



class Spiel():
    gewinnpunkte = 11

    def __init__(self, spieler1: Spieler, spieler2: Spieler, gewinnsaetze):
        self.spieler = [spieler1, spieler2]
        self.gewinnsaetze = gewinnsaetze
        self.spielstand_satz = [0, 0]
        self.ergebnis = [0, 0]
        self.hat_aufschlag = self.ermittle_aufschlag()
        self.hat_ball = self.hat_aufschlag
        print(f"{self.spieler[0].name}({self.spieler[0].id}, {self.spieler[0].spielstaerke}) : {self.spieler[1].name}({self.spieler[1].id}, {self.spieler[1].spielstaerke})")
        with open("game.log", "w") as file:
            file.write(80 * "#" + "\n")
            file.write(f"Spieler 1: {self.spieler[0].name} - Id: {self.spieler[0].id} - Spielstärke: {self.spieler[0].spielstaerke}\n")
            file.write(f"Spieler 2: {self.spieler[1].name} - Id: {self.spieler[1].id} - Spielstärke: {self.spieler[1].spielstaerke}\n")
            file.write(f"Gewinnsätze: {self.gewinnsaetze}\n")
            file.write(80 * "#" + "\n")

    def spielen(self):
        while max(self.ergebnis) < self.gewinnsaetze:
            gewinner = self.satz()
            self.ergebnis[gewinner] += 1
            self.spielstand_satz[0] = 0
            self.spielstand_satz[1] = 0
        with open("game.log", "a") as file:
            file.write("\n" + 40 * "#" + "\n")
            file.write(f"Endergebnis: {self.ergebnis}\n")
            file.write(f"Der Gewinner ist {self.spieler[self.ergebnis.index(max(self.ergebnis))].name}\n")
        print("\nEndergebnis:", self.ergebnis)
        return(f"Der Gewinner ist {self.spieler[self.ergebnis.index(max(self.ergebnis))].name}")
    
    def satz(self):
        baelle = 0
        with open("game.log", "a") as file:
            file.write(35 * "_" + "\n")
            file.write(35 * "_" + "\n")
            file.write(f"Satz beginnt\n")
        while (max(self.spielstand_satz) < 11) or ((max(self.spielstand_satz) >= 11) and (max(self.spielstand_satz) - min(self.spielstand_satz)) <= 1):
            if baelle > 0 and baelle % 2 == 0:
                with open("game.log", "a") as file:
                    file.write("\n" + 16 * "- " + "\n")
                    file.write(f"Aufschlag wechselt zu: {self.spieler[self.hat_aufschlag].name}\n")
                    file.write(16 * "- " + "\n")
                self.wechsel_aufschlag()
            punkt_fuer = self.punkt()
            self.spielstand_satz[punkt_fuer] += 1
            baelle += 1
            with open("game.log", "a") as file:
                file.write(f"Neuer Spielstand: {self.spielstand_satz}\n")
        with open("game.log", "a") as file:
            file.write(35 * "_" + "\n")
            file.write(35 * "_" + "\n")
            file.write(f"Satz endet: {self.spielstand_satz}\n\n")
        print(f"{self.spielstand_satz}", end=" ")
        return self.spielstand_satz.index(max(self.spielstand_satz))
    
    def punkt(self):
        with open("game.log", "a") as file:
            file.write(35 * "_" + "\n")
            file.write(f"Start Punkt\n")
        aufschlag = self.spieler[self.hat_ball].schlag()
        letzter_schlag = aufschlag
        while True:
            self.wechsel_ball()
            schlag = self.spieler[self.hat_ball].schlag()
            if schlag == 0:
                with open("game.log", "a") as file:
                    file.write(f"  Punkt für {self.spieler[1 if self.hat_ball == 0 else 0].name}\n")
                break
            if (schlag - 16) < letzter_schlag:
                with open("game.log", "a") as file:
                    file.write(f"  Punkt für {self.spieler[1 if self.hat_ball == 0 else 0].name}\n")
                break
            letzter_schlag = schlag
        self.wechsel_ball()
        return self.hat_ball

    def wechsel_ball(self):
        self.hat_ball = 1 if self.hat_ball == 0 else 0

    def wechsel_aufschlag(self):
        self.hat_aufschlag = 1 if self.hat_aufschlag == 0 else 0

    def ermittle_aufschlag(self):
        return randint(0,1)

s1 = Spieler("Hans", 1234, 85)
s2 = Spieler("Karl", 5678, 90)

sp = Spiel(s1, s2, 2)

print(sp.spielen())