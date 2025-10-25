class Einwert():
    def __init__(self):
        self._wert = None
    
    def lese_wert(self):
        print("ich lese wert")
        return self._wert

    def schreibe_wert(self, k):
        print("ich schreibe wert")
        if(isinstance(k, list)):
            self._wert = k
            return self._wert
        else:
            raise TypeError

    def loesche_wert(self):
        print("ich loesche wert")
        # del self._wert
        self._wert = None
        return self._wert
    
    wert = property(lese_wert, schreibe_wert, loesche_wert)

obj = Einwert()

print("\n############\n")
print(obj.wert)
obj.wert = [1,2,3]
print(obj.wert)
obj.loesche_wert()
print(obj.wert)
# obj.wert = 1
obj._wert = 1
print(obj.wert)
print("\n############\n")

