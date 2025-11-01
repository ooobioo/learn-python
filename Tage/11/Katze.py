import Tier

class Katze(Tier.Tier):
    def __init__(self, name, farbe):
        super().__init__(name)
        self.farbe = farbe

    def spricht(self):
        return f"{self.name} spricht: Miau!"
    
    def frisst(self, nahrung):
        return nahrung == ("Fleisch" or "Fisch")
    
    def get_farbe(self):
        return self.farbe
    
my_cat = Katze("Lilo", "weiß")

print(my_cat.spricht())
print(my_cat.frisst("Banane"))
print(my_cat.frisst("Fleisch"))
print(my_cat.name_aus())