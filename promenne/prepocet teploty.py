# vstupy
celsius = int(input("Zadej teplotu v stupních Celsia: "))

# výpočty
kelviny = round(celsius + 273.15, 2)
fahrenheity = round(celsius * (9/5) + 32, 2)

print(f"Hodnota v Kelvinech je: {kelviny} a hodnota ve Fahrenheitech je: {fahrenheity} :)")
