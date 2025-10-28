import random

class Spieler():
    def __init__(self, name, id, spielstaerke):
        self.name = name
        self.id = id
        self.spielstaerke = spielstaerke

    def schlag(self):
        schlagstaerke = random.randint(0, self.spielstaerke)
        return schlagstaerke



class Spiel():
    gewinnpunkte = 11

    def __init__(self, spieler1: Spieler, spieler2: Spieler, gewinnsaetze):
        self.spieler = [spieler1, spieler2]
        self.gewinnsaetze = gewinnsaetze
        self.saetze = [0, 0]
        self.spielstand = [0, 0]
        self.hat_ball = self.aufschlag()

    def spielen(self):
        while max(self.saetze) < self.gewinnsaetze:
            gewinner = self.satz()
            self.saetze[gewinner] += 1
            self.spielstand[0] = 0
            self.spielstand[1] = 0
        print("Endergebnis:", self.saetze)
        return(f"Der Gewinner ist {self.spieler[self.saetze.index(max(self.saetze))].name}")
    
    def satz(self):
        aufschlag = self.spieler[self.hat_ball].schlag()
        letzter_schlag = aufschlag
        while (max(self.spielstand) < 11) or ((max(self.spielstand) >= 11) and (max(self.spielstand) - min(self.spielstand)) <= 1):
            self.hat_ball = 1 if self.hat_ball == 0 else 0
            rueckschlag = self.spieler[self.hat_ball].schlag()
            # print("L:", letzter_schlag, " R:", rueckschlag)
            if (rueckschlag - 16) < letzter_schlag:
                # print(f"Punkt: {self.spieler[ 1 if self.hat_ball == 0 else 0].name}")
                self.spielstand[1 if self.hat_ball == 0 else 0] += 1
                # print(f"Neuer Spielstand: {self.spielstand}")
                letzter_schlag = self.spieler[self.hat_ball].schlag()
                continue
            else:
                letzter_schlag = rueckschlag
                continue
        print(f"Satz: {self.spielstand}")
        return self.spielstand.index(max(self.spielstand))

    def aufschlag(self):
        return random.randint(0,1)

s1 = Spieler("S1", 1234, 85)
s2 = Spieler("S2", 5678, 90)

sp = Spiel(s1, s2, 4)

print(sp.spielen())