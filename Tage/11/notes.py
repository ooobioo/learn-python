class my_obj:
    def __init__(self):
        print("konstruiere")
        pass
    
    def f(self, text):
        print(text)

    def interne_methode(x):
        print(x)


# obj = my_obj()
# obj.f("huhu")
# obj.interne_methode("huhu")



class Hund:
    name: str

    def __init__(self, name: str):
        self.name = name

    def sprich(self) -> str:
        return f"{self.name} spricht: wuff!"
    
    def friss(self, nahrung) -> bool:
        return nahrung == "Fleisch"


my_hund = Hund("Bello")

print("Hallo, ich bin", my_hund.name)
print(my_hund.sprich())
print(my_hund.friss("Gurke"))
print(my_hund.friss("Fleisch"))


class Tier:
    def __init__(self, name):
        self.name = name

class Katze(Tier):
    def __init__(self, name, rasse):
        super().__init__(name)
        self.rasse = rasse

cat = Katze("mauzi", "shorthair")

print(cat.name)
print(cat.rasse)