import string

cislo = input("Vlož číslo: ")

soucet = 0
for i in range(len(cislo)):
   soucet += int(cislo[i])

print(soucet)

