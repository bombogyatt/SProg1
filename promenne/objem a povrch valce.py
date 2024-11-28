import math
#objem válce
vyska = int(input("Zadej vysku valce: "))
polomer = int(input("Zadej polomer valce: "))

# vypocet objemu a povrchu
objem = round(math.pi * (polomer ** 2) * vyska, 2)
povrch = round(2 * math.pi * polomer * (polomer + vyska), 2)

# vypis hodnot
print(f"Povrch válce: {povrch} cm2")
print(f"Objem válce: {objem} cm2")
