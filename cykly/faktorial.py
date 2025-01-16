x = int(input("Vlož číslo ze ktereého chceš vypočítat faktoriál: "))

vysledek = 1
for y in range(x):
    vysledek *= x               
    x -= 1

print(f"faktorial je: {vysledek}")