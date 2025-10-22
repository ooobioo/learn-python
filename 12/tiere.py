#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Tier:
    def __init__(self, name):
        self.name= name
        
    def spricht(self):
        pass
        
    def frisst(self, etwas):
        pass
        
    def name_aus(self):
        return self.name
    
    def fuettern(self):
        print(f"{self.name} bedankt sich fuer das leckere Futter!")

     
class Hund(Tier):

    def __init__(self, name, hundemarke):
        super().__init__(name)
        self.marke = hundemarke
        
    def spricht():
        return "wau"
        
    def frisst(self, etwas):
        if etwas  == "Fleisch":
            return True
        return False


class Katze(Tier):
    def __init__(self, name, farbe):
        super().__init__(name)
        self.farbe = farbe

    def spricht(self):
        return f"{self.name} spricht: Miau!"
    
    def frisst(self, nahrung):
        return nahrung == ("Fleisch" or "Fisch")
    
    def get_farbe(self):
        return self.farbe


class Mensch:
    def __init__(self, name: str, tiere: list[Tier]):
        self.name = name
        if 1 <= len(tiere) <= 5:
            self.tiere = set(tiere)
        else:
            raise ValueError("Number of animals must be between 1 and 5")
    
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

fremder_hund = Hund("Bello", 1234567)


print()
me = Mensch(name="Thomas", tiere=[hund1, hund2, hund3, hund4, katze1])
print(f"{me.name} Tiere sind: {me.get_tiere_class_and_names()}")

me.anbetteln(hund1)
me.anbetteln(fremder_hund)
me.anbetteln(katze1)
print()

