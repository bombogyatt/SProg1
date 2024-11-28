# vstupy
objemDat_MB = int(input("Zadej objem dat ke stažení v megabajtech: "))
rychlostStahovani = int(input("Zadej rychlost stahování v megabitech za sekundu (Mbit/s): "))

# výpočet
dobaStahovani = round((objemDat_MB * 8) / rychlostStahovani, 2)

# vypis do konzole
print(f"Doba stahování je {dobaStahovani} sekund :)")