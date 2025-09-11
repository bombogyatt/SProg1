def nsd(cislo1, cislo2):
    zbytek = cislo1%cislo2
    if zbytek == 0:
        return cislo2
    else:
        return nsd(cislo2, zbytek)
    

print(nsd(252, 105))
