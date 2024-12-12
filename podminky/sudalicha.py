# vstup
cislo = int(input("Vlož číslo: "))

zbytek = cislo % 2

if zbytek == 0:
    print(f"Číslo {cislo} je sudé")
else:
    print(f"Číslo {cislo} je liché")