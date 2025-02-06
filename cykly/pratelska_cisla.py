import time
cas = time.time()

for cislo in range(1, 10000):
    delitel1 = 0
    for i in range(1, cislo):
        if cislo%i == 0:
            delitel1 += i

    delitel2 = 0
    for j in range(1, delitel1):
        if delitel1%j == 0:
            delitel2 += j

    if delitel2 == cislo and cislo != delitel1:
        print(f"cisla {cislo} a {delitel1} jsou přátelská")

print("--- %s seconds ---" % (time.time() - cas))