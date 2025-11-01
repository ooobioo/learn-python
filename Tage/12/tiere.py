#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Tier:
    anzahl_tiere = 0

    def __init__(self, name):
        self.name = name
        Tier.anzahl_tiere += 1
        
    def spricht(self):
        pass
        
    def frisst(self, etwas):
        pass
        
    def name_aus(self):
        return self.name
    
    def fuettern(self):
        print(f"{self.name} bedankt sich fuer das leckere Futter!")

    def get_all_tiere(self):
        res = f"\nTiere: {Tier.anzahl_tiere} \n"
        return res

     
class Hund(Tier):
    anzahl_hunde = 0

    def __init__(self, name, hundemarke):
        super().__init__(name)
        self.marke = hundemarke
        Hund.anzahl_hunde += 1
        
    def spricht():
        return "wau"
        
    def frisst(self, etwas):
        if etwas  == "Fleisch":
            return True
        return False
    
    def get_all_hunde(self):
        res = f"\nKatzen: {Hund.anzahl_hunde} \n"
        return res


class Katze(Tier):
    anzahl_katzen = 0

    def __init__(self, name, farbe):
        super().__init__(name)
        self.farbe = farbe
        Katze.anzahl_katzen += 1

    def spricht(self):
        return f"{self.name} spricht: Miau!"
    
    def frisst(self, nahrung):
        return nahrung == ("Fleisch" or "Fisch")
    
    def get_farbe(self):
        return self.farbe

    def get_all_katzen(self):
        res = f"\nKatzen: {Katze.anzahl_katzen} \n"
        return res


class Mensch:
    def __init__(self, name: str, tiere: list[Tier]):
        self.name = name
        if 1 <= len(tiere) <= 5 and all(isinstance(tier, Tier) for tier in tiere):
            self.tiere = set(tiere)
        else:
            raise ValueError("Tiere must be list of class Tier and amount must be between 1 and 5")
    
    def get_tiere_class_and_names(self):
        names = []
        for tier in self.tiere:
            names.append(f"{type(tier).__name__}: {tier.name}")
        return sorted(names)
    
    def anbetteln(self, tier: Tier):
        if tier in self.tiere and isinstance(tier, Hund):
            tier.fuettern()
        elif tier in self.tiere :
            print(f"{tier.name} fuettere ich nicht! Du bist meine {type(tier).__name__}.")
        else:
            print(f"{tier.name} fuettere ich nicht! Du bist ein fremdes Tier!")



hund1 = Hund("Waldi", 123)
hund2 = Hund("Wuffi", 1234)
hund3 = Hund("Fiffi", 12345)
hund4 = Hund("Fuffu", 123456)
katze1 = Katze("Minka", "gelb")
katze2 = Katze("Munka", "gelb")

print("Hunde", hund1.anzahl_hunde)
print("Katzen", katze1.anzahl_katzen)
print("Tiere", katze1.anzahl_tiere)



fremder_hund = Hund("Bello", 1234567)

mensch1 = Mensch("Peter", [hund1])
mensch2 = Mensch("Paul", [hund2])
# mensch3 = Mensch("Mary", [mensch2])

print()
me = Mensch(name="Thomas", tiere=[hund1, hund2, hund3, hund4, katze1])
print(f"{me.name} Tiere sind: {me.get_tiere_class_and_names()}")

me.anbetteln(hund1)
me.anbetteln(fremder_hund)
me.anbetteln(katze1)
print()


print("Hunde", hund1.anzahl_hunde)
print("Katzen", katze1.anzahl_katzen)
print("Tiere", katze1.anzahl_tiere)
