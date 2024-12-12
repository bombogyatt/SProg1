import math

# vstup 3 cisel
a = int(input("Zadej koeficient a: "))
b = int(input("Zadej koeficient b: "))
c = int(input("Zadej koeficient c: "))

diskriminant = float((b ** 2) - (4*a*c))

if diskriminant >= 0:
    kořen1 = float((-b + math.sqrt(diskriminant)) / 2*a)
    kořen2 = float((-b - math.sqrt(diskriminant)) / 2*a)
    print(f"Kořeny rovnice jsou x1 = {kořen1}, x2 = {kořen2}")
else:
    print("rovnice nemá v R řešení!")
