import random

  
class spieler:
    def __init__(self, name, lizenznummer, spielstaerke):
        self.name = name
        self.lizenz = lizenznummer
        self.staerke = spielstaerke
        pass
    
    def aufschlag(self, gegner, spielstand):
        # liefert True zurück, wenn Ballwechsel beendet 
        # und weiterer Ballwechsel nötig,
        # False wenn Spiel beendet
        schlagqualitaet = self.schlagqualitaet()
        if schlagqualitaet == 0:
            # Aufschlagfehler, direkt verloren
            return spielstand.resultat.punkt( self )
        else:
            return gegner.schlag(self, schlagqualitaet, spielstand)
        
    def __str__(self):
        return self.name + f"({self.lizenz}, Stärke {self.staerke})"
        
            
    def schlag(self, gegner, gegner_qualitaet, spielstand):
        schwellenwert_fuer_fehlschlag = 16
        meine_schlagqualitaet = self.schlagqualitaet() # Qualität des aktuellen Schlages
        if meine_schlagqualitaet == 0:
            # sehr schlechter Schlag, direkt verloren
            return spielstand.resultat.punkt( self )
             
        elif meine_schlagqualitaet + schwellenwert_fuer_fehlschlag < gegner_qualitaet:
            # Ball kommt wesentlich stärker als Spieler ihn abwehrt
            # -> Punkt für Gegner
            return spielstand.resultat.punkt( self )

        else:
            return gegner.schlag(self, meine_schlagqualitaet, spielstand)
            
    def schlagqualitaet(self):
        return random.randint(0, self.staerke)
     
    
class ergebnis:
    
    gewinnpunkte_fuer_satz = 11
    
    def __init__(self, gewinnsaetze, spieler_1, spieler_2 ):
        self.erg = [[0,0]]
        self.dauer = gewinnsaetze
        self.spieler_1 = spieler_1
        self.spieler_2 = spieler_2
          
    
    def punkt( self, spieler):
        # der Spieler, der einen Ballwechsel verliert, meldet das über diese Funktion
        if spieler is self.spieler_2:
            # Punkt für Spieler 1
            self.erg[0][0] += 1
        else:
            # Punkt für Spieler 2
            self.erg[0][1] += 1
        # ist Satz beendet?
        satz_beendet = False 
        if self.erg[0][0] > ergebnis.gewinnpunkte_fuer_satz:
            if self.erg[0][0] > self.erg[0][1] + 1:
                # zweites IF prüft ob in Verlängerung
                satz_beendet = True
        if self.erg[0][1] > ergebnis.gewinnpunkte_fuer_satz:
            if self.erg[0][1] > self.erg[0][0] + 1:
                satz_beendet = True
        if satz_beendet:
            if self.spiel_aus():
                self.erg.reverse()
                return False
            else: 
                # neuer Satz
                # wird vorne eingefügt, Reihenfolge also umgekehrt
                self.erg.insert( 0, [0,0] )        
        return True
    
    def spiel_aus( self ):
        spieler_1_saetze = 0
        spieler_2_saetze = 0
        for satz in self.erg:
            if satz[0] < satz[1]:
                spieler_2_saetze += 1
            else:
                spieler_1_saetze += 1
        if (spieler_2_saetze == self.dauer) or (spieler_1_saetze == self.dauer):
            # Ein Spieler hat die nötige Anzahl an Sätzen gewonnen
            return True
        else:
            return False
        
    def punkte_im_aktuellen_satz(self):
        # Gesamtzahl der gespielten Ballwechsel
        # wichtig für Entscheidung wer Aufschlag hat
        return self.erg[0][0] + self.erg[0][1]
    
    def __str__(self):
        rueckstring =  str(self.spieler_1) + " : "
        rueckstring += str(self.spieler_2) + "\n" 
        for satz in self.erg:
            rueckstring += str(satz[0]) + ":" + str(satz[1]) + " " 
        return rueckstring

    
class spiel():
    def __init__(self, erster_spieler, zweiter_spieler, gewinnsaetze):
        self.spieler_1 = erster_spieler
        self.spieler_2 = zweiter_spieler
        self.dauer = gewinnsaetze
        self.resultat = ergebnis( gewinnsaetze, self.spieler_1, self.spieler_2 )
        pass   
     
    def spielen(self):
        # zufällige Wahl wer beginnt
        wer_schlaegt_auf = random.randint(1,2)
        letzter_aufschlaeger = wer_schlaegt_auf
        spiel_nicht_fertig = True
        while spiel_nicht_fertig:
            if wer_schlaegt_auf == 1:
                spiel_nicht_fertig = self.spieler_1.aufschlag(self.spieler_2, self)
            else:
                spiel_nicht_fertig = self.spieler_2.aufschlag(self.spieler_1, self)
            if not spiel_nicht_fertig:
                punkte_im_satz = self.resultat.punkte_im_aktuellen_satz()
                if not (punkte_im_satz % 2) or punkte_im_satz > 20:
                    # aufschlagwechsel
                    # tauschen Werte 1 und 2
                    wer_schlaegt_auf = letzter_aufschlaeger//2 + 2*(letzter_aufschlaeger%2)
                    letzter_aufschlaeger = wer_schlaegt_auf 


    
s1 = spieler("Guido", 100, 99)
s2 = spieler("Gerhardt", 1000, 88)
sp = spiel(s1, s2, 4 )
sp.spielen()
print( sp.resultat )

# i = 0
# while sp.erg[0] < sp.erg[1]:
#     sp = spiel(s1, s2, 3)
#     x = sp.spielen()
#     i += 1 
#     print(sp.erg)
    
# print(i)