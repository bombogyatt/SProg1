# vstup 3 cisel
cislo1 = int(input("Vlož první číslo: "))
cislo2 = int(input("Vlož druhé číslo: "))
cislo3 = int(input("Vlož třetí číslo: "))


nejmensi_cislo = 0
stredni_cislo = 0
nejvetsi_cislo = 0

# test nejvetsiho cisla
if cislo1 > cislo2 and cislo1 > cislo3:
    
    nejvetsi_cislo = cislo1
    if cislo2 > cislo3:
        stredni_cislo = cislo2
        nejmensi_cislo = cislo3       
    else:
        stredni_cislo = cislo3
        nejmensi_cislo = cislo2
elif cislo2 > cislo3 and cislo2 > cislo1:
   
    nejvetsi_cislo = cislo2
    if cislo1 > cislo3:
        stredni_cislo = cislo1
        nejmensi_cislo = cislo3       
    else:
        stredni_cislo = cislo3
        nejmensi_cislo = cislo1

elif cislo3 > cislo2 and cislo3 > cislo1:

    nejvetsi_cislo = cislo3
    if cislo2 > cislo1:
        stredni_cislo = cislo2
        nejmensi_cislo = cislo1      
    else:
        stredni_cislo = cislo1
        nejmensi_cislo = cislo2

print(f"Čísla v vzestupném pořadí: {nejvetsi_cislo}, {stredni_cislo}, {nejmensi_cislo}")

