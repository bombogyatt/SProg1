soucet_druhych_mocnin = 0
druha_mocnina_souctu = 0

for i in range(101):
    soucet_druhych_mocnin += i**2

for j in range(101):
    druha_mocnina_souctu += j

druha_mocnina_souctu = druha_mocnina_souctu**2

print(f"rozdíl je {druha_mocnina_souctu - soucet_druhych_mocnin}")