mez = int(input("Napis mi mez pro kterou chces vygenerovat cisla: "))

x = 0
zbytek = 0
while x < mez :
    zbytek = x%2
    if x % 2 == 0:
        print(f"Číslo {x} je sudé")
    else:
        print(f"Číslo {x} je liché")
    x += 1