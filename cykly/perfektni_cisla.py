
# kontroluje soucet delitelu
delitel = 0

for cislo in range(1, 10000):
    delitel = 0
    for i in range(1, cislo):
        # scita delitele
        if cislo%i == 0:
            delitel += i

    if delitel == cislo:
        print(f"číslo {cislo} je perfektní")
            