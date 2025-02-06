import string

for cislo in range(1, 100):
    cislo_str = str(cislo)
    soucet_cislic = 0


    while(soucet_cislic != 1 and soucet_cislic != 4):

        # projede jednotlive číslice a udela jejich ciferný součet
        for i in range(len(cislo_str)):
            soucet_cislic += int(cislo_str[i])**2

        if soucet_cislic == 1 or soucet_cislic == 4:
            break

        cislo_str = str(soucet_cislic)
        soucet
        print(cislo_str)
        
    # cislo_str = str(soucet_cislic)
    
    if soucet_cislic == 1:
        print(f"čislo {cislo_str} je štastné")
