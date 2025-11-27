#dodelat nassobeni

import math

class Vektor:

    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def __str__(self):
        return f"[{self.x}, {self.y}]"
    
    def __add__(self, jiny):
        return Vektor(self.x + jiny.x, self.y + jiny.y)
    
    def __sub__(self, jiny):
        return Vektor(self.x - jiny.x, self.y - jiny.y)
    
    def delka(self):
        delka = math.sqrt(self.x**2 + self.y**2)
        return delka
    
    def __mul__(self, jiny):
        if isinstance(jiny, Vektor):


        if isinstance(jiny, (int, float)):


v1 = Vektor(3, 4)
v2 = Vektor(-1, 2)
print(v1)  # [3, 4]
print(v2)  # [-1, 2]

v1 = Vektor(3, 4)
v2 = Vektor(1, 2)
v3 = v1 + v2
print(f"{v1} + {v2} = {v3}")  # [3, 4] + [1, 2] = [4, 6]

v = Vektor(3, 4)
print(f"Délka {v} = {v.delka()}")  # Délka [3, 4] = 5.0