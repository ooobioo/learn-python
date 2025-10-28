from random import randint


class Spieler():
    def __init__(self, name, id, spielstaerke):
        self.name = name
        self.id = id
        self.spielstaerke = spielstaerke

    def aufschlag(self, spiel: "Spiel", gegner):
        schlagstaerke = randint(0, self.spielstaerke)
        verloren = False
        if schlagstaerke == 0:
            with open("game.log", "a") as file:
                file.write(f"  Aufschlag {self.name}: {schlagstaerke}\n")
                file.write(f"  --> Punkt für {gegner.name}\n")
                verloren = True
        else:
            with open("game.log", "a") as file:
                file.write(f"  Aufschlag {self.name}: {schlagstaerke}\n")
        if verloren == True:
            spiel.set_punkt(gegner)
        else:
            gegner.schlag(self, spiel, schlagstaerke)

    
    def schlag(self, gegner: "Spieler", spiel: "Spiel", gegner_schlagstaerke):
        schlagstaerke = randint(0, self.spielstaerke)
        if schlagstaerke == 0:
            with open("game.log", "a") as file:
                file.write(f"  Schlag {self.name}: {schlagstaerke}\n")
                file.write(f"  --> Punkt für {gegner.name}\n")
            spiel.set_punkt(gegner)
        elif schlagstaerke < (gegner_schlagstaerke - 16):
            with open("game.log", "a") as file:
                file.write(f"  Schlag {self.name}: {schlagstaerke}\n")
                file.write(f"  --> Punkt für {gegner.name}\n")
            spiel.set_punkt(gegner)
        else:
            with open("game.log", "a") as file:
                file.write(f"  Schlag {self.name}: {schlagstaerke}\n")
            gegner.schlag(self, spiel, schlagstaerke)



class Spiel():

    def __init__(self, spieler1: Spieler, spieler2: Spieler, gewinnsaetze):
        self.spieler = [spieler1, spieler2]
        self.gewinnsaetze = gewinnsaetze
        self.spielstand_satz = [0, 0]
        self.ergebnis = [0, 0]
        self.hat_satz_aufschlag = self.ermittle_aufschlag()
        self.hat_aufschlag = self.hat_satz_aufschlag
        with open("game.log", "w") as file:
            file.write(80 * "#" + "\n")
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
            self.punkt()
            baelle += 1
            with open("game.log", "a") as file:
                file.write(f"Neuer Spielstand: {self.spielstand_satz}\n")
        with open("game.log", "a") as file:
            file.write(35 * "_" + "\n")
            file.write(35 * "_" + "\n")
            file.write(f"Satz endet: {self.spielstand_satz}")
            file.write(5 * "\n")
        self.wechsel_satz_aufschlag()
        return self.spielstand_satz.index(max(self.spielstand_satz))
    
    def punkt(self):
        with open("game.log", "a") as file:
            file.write(35 * "_" + "\n")
            file.write(f"Start Punkt\n")
        self.spieler[self.hat_aufschlag].aufschlag(self, self.spieler[1 if self.hat_aufschlag == 0 else 0])

    
    def set_punkt(self, gewinner):
        index = self.spieler.index(gewinner)
        self.spielstand_satz[index] += 1
        with open("game.log", "a") as file:
            file.write(f"Zwischenstand: {self.spielstand_satz}\n")

    def wechsel_aufschlag(self):
        self.hat_aufschlag = 1 if self.hat_aufschlag == 0 else 0
  
    def wechsel_satz_aufschlag(self):
        self.hat_satz_aufschlag = 1 if self.hat_satz_aufschlag == 0 else 0
        self.hat_aufschlag = self.hat_satz_aufschlag

    def ermittle_aufschlag(self):
        return randint(0,1)

s1 = Spieler("S1", 1234, 85)
s2 = Spieler("S2", 5678, 90)

sp = Spiel(s1, s2, 4)

print(sp.spielen())