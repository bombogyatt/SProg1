class Hrac:

    def __init__(self, name):
        self.jmeno = name
        self._zivoty = 100

    def utrzi_zraneni(self, dmg):
        self.zivoty -= dmg 


hrac1 = Hrac("David")
print(hrac1.zivoty)
hrac1.utrzi_zraneni(20)
print(hrac1.zivoty)
hrac2 = Hrac("dam")