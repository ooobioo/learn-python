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
    

hu = Hund("Waldi","DFRGD 345345 !!")

print(hu.__doc__)




        




    

















