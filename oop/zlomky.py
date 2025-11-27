import math

class Zlomek:

    def __init__(self, _citatel, _jmenovatel = 1):
        self.citatel = _citatel
        self.jmenovatel = _jmenovatel

    def __str__(self):
       return f"{self.citatel}/{self.jmenovatel}"
    
    def zkrat(self):
        nsd = math.gcd(abs(self.citatel), abs(self.jmenovatel))
        self.citatel = int(self.citatel / nsd)
        self.jmenovatel = int(self.jmenovatel / nsd)
        return self

    def __add__(self, jiny):
        n_citatel = self.citatel * jiny.jmenovatel + jiny.citatel * self.jmenovatel
        n_jmenovatel = self.jmenovatel * jiny.jmenovatel
        n_zlomek = Zlomek(n_citatel, n_jmenovatel)
        return n_zlomek.zkrat()
    
    def __sub__(self, jiny):
        n_citatel = self.citatel * jiny.jmenovatel - jiny.citatel * self.jmenovatel
        n_jmenovatel = self.jmenovatel * jiny.jmenovatel
        n_zlomek = Zlomek(n_citatel, n_jmenovatel)
        return n_zlomek.zkrat()
    
    def __mul__(self, jiny):
        n_citatel = self.citatel * jiny.citatel
        n_jmenovatel = self.jmenovatel * jiny.jmenovatel
        n_zlomek = Zlomek(n_citatel, n_jmenovatel)
        return n_zlomek.zkrat()
    
    def __truediv__(self, jiny):
        if jiny.citatel == 0:
            print("jmenovatel se rovná nule, nelze dělit")
            return None
        else:
            n_citatel = self.citatel * jiny.jmenovatel
            n_jmenovatel = self.jmenovatel * jiny.citatel
            n_zlomek = Zlomek(n_citatel, n_jmenovatel)
            return n_zlomek.zkrat()
        
    def __eq__ (self, jiny):
        self.zkrat()
        jiny.zkrat()
        if (self.citatel * jiny.jmenovatel) == (self.jmenovatel * jiny.citatel):
            return True
        else:
            return False


# Test 1: Vytvoření zlomků
z1 = Zlomek(1, 2)
z2 = Zlomek(3, 4)
z3 = Zlomek(5)
print(f"z1 = {z1}")  # 1/2
print(f"z2 = {z2}")  # 3/4
print(f"z3 = {z3}")  # 5/1

# Test 2: Sčítání
print(f"{z1} + {z2} = {z1 + z2}")  # 5/4

# Test 3: Odčítání
print(f"{z2} - {z1} = {z2 - z1}")  # 1/4

# Test 4: Násobení
print(f"{z1} * {z2} = {z1 * z2}")  # 3/8

# Test 5: Dělení
print(f"{z1} / {z2} = {z1 / z2}")  # 2/3

# Test 6: Složitější výpočet
print(f"({z1} + {z2}) * {z3} = {(z1 + z2) * z3}")  # 25/4

# Test 7: Zkracování
z4 = Zlomek(8, 12)
print(f"Před zkrácením: {z4}")  # 8/12
z4.zkrat()
print(f"Po zkrácení: {z4}")    # 2/3

z10 = Zlomek(11, 5)
z11 = Zlomek(2)
print(z10 == z11)



