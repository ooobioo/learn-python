from random import randint
import logging

RUECKSCHLAG_HANDICAP = 16
PUNKTE_ZUM_SATZGEWINN = 11

# logfile leeren bzw neu erzeugen
with open("game.log", "w") as file:
    file.write(f"START LOGGING\n\n")

logging.basicConfig(filename="game.log", level=logging.INFO)


class Spieler:
    def __init__(self, name, id, spielstaerke):
        self.name = name
        self.id = id
        self.spielstaerke = spielstaerke

    def aufschlag(self, set_punkt_callback, gegner: "Spieler"):
        schlagstaerke = randint(0, self.spielstaerke)
        logging.info(f"Aufschlag {self.name:<17}: {schlagstaerke:>3}")
        if schlagstaerke == 0:
            logging.info("----> Punkt für %s", {gegner.name})
            set_punkt_callback(gegner)
        else:
            gegner.schlag(self, set_punkt_callback, schlagstaerke)

    
    def schlag(self, gegner: "Spieler", set_punkt_callback, gegner_schlagstaerke):
        schlagstaerke = randint(0, self.spielstaerke)
        logging.info(f"Schlag {self.name:<20}: {schlagstaerke:>3}")
        if schlagstaerke == 0:
            logging.info("----> Punkt für %s", {gegner.name})
            set_punkt_callback(gegner)
        elif schlagstaerke < (gegner_schlagstaerke - RUECKSCHLAG_HANDICAP):
            logging.info("----> Punkt für %s", {gegner.name})
            set_punkt_callback(gegner)
        else:
            gegner.schlag(self, set_punkt_callback, schlagstaerke)



class Spiel:

    def __init__(self, spieler1: Spieler, spieler2: Spieler, gewinnsaetze):
        self.spieler = [spieler1, spieler2]
        self.gewinnsaetze = gewinnsaetze
        self.spielstand_satz = [0, 0]
        self.saetze = []
        self.ergebnis = [0, 0]
        self.hat_satz_aufschlag = self.ermittle_aufschlag()
        self.hat_aufschlag = self.hat_satz_aufschlag
        logging.info(50 * "#")
        logging.info(f"Spieler 2: {self.spieler[1].name} - Id: {self.spieler[1].id} - Spielstärke: {self.spieler[1].spielstaerke}")
        logging.info(f"Gewinnsätze: {self.gewinnsaetze}")
        logging.info(50 * "#")

    def spielen(self):
        while max(self.ergebnis) < self.gewinnsaetze:
            gewinner = self.satz()
            self.ergebnis[gewinner] += 1
            self.spielstand_satz[0] = 0
            self.spielstand_satz[1] = 0
        logging.info(40 * "#")
        logging.info(f"Endergebnis: {self.ergebnis}")
        logging.info(f"Der Gewinner ist {self.spieler[self.ergebnis.index(max(self.ergebnis))].name}")
        res = f"\n{self.spieler[0].name}({self.spieler[0].id}, Stärke {self.spieler[0].spielstaerke})"
        res = res + " : " + f"{self.spieler[1].name}({self.spieler[1].id}, Stärke {self.spieler[1].spielstaerke})\n"
        for satz in self.saetze:
            res = res + f"{satz} "
        res = res + f"\nDer Gewinner ist {self.spieler[self.ergebnis.index(max(self.ergebnis))].name} mit "+  ":".join(str(x) for x in self.ergebnis) + "\n"
        return res
    
    def satz(self):
        baelle = 0
        logging.info(f"Satz beginnt")
        while (max(self.spielstand_satz) < PUNKTE_ZUM_SATZGEWINN) or ((max(self.spielstand_satz) >= PUNKTE_ZUM_SATZGEWINN) and (max(self.spielstand_satz) - min(self.spielstand_satz)) <= 1):
            if baelle > 0 and baelle % 2 == 0:
                logging.info(f"Aufschlag wechselt zu: {self.spieler[self.hat_aufschlag].name}")
                self.wechsel_aufschlag()
            self.punkt()
            baelle += 1
            logging.info(f"Neuer Spielstand: {self.spielstand_satz}" + 10 * "." + "\n")
        logging.info(f"Satz endet: {self.spielstand_satz}" + 3 * "\n")
        self.saetze.append(":".join(str(x) for x in self.spielstand_satz))
        self.wechsel_satz_aufschlag()
        return self.spielstand_satz.index(max(self.spielstand_satz))
    
    def punkt(self):
        logging.info(f"Punkt beginnt " + 20 * ".")
        self.spieler[self.hat_aufschlag].aufschlag(self.set_punkt, self.spieler[self.wechsel(self.hat_aufschlag)])

    def set_punkt(self, gewinner):
        index = self.spieler.index(gewinner)
        self.spielstand_satz[index] += 1

    def wechsel_aufschlag(self):
        self.hat_aufschlag = self.wechsel(self.hat_aufschlag)
  
    def wechsel_satz_aufschlag(self):
        self.hat_satz_aufschlag = self.wechsel(self.hat_satz_aufschlag)
        self.hat_aufschlag = self.hat_satz_aufschlag

    def wechsel(self, i):
        return 1 if i== 0 else 0

    def ermittle_aufschlag(self):
        return randint(0,1)

s1 = Spieler("Hans Müller", 1234, 85)
s2 = Spieler("Jürgen Fischer", 5678, 90)

sp = Spiel(s1, s2, 4)

print(sp.spielen())
