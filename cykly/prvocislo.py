cislo = int(input("Nacti cislo, u ktereho chces overit prvociselnost: "))

x = 1
zbytek = 0
while cislo > x:
    if cislo % x and cislo != x:
        print("není prvočíslo")
        break
    x += 1

