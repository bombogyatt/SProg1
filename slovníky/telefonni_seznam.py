seznam = {}

kontakty = int(input("Zadej počet kontaktů: "))

for i in range(kontakty):
    jmeno = input("Zadej jméno: ")
    číslo = int(input("Zadej tel. číslo: "))
    seznam[jmeno] = číslo

print(seznam)

klic = input("Koho chceš vyhledat?: ")
print(seznam.get(klic))