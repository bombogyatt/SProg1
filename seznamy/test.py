# první seznam
delka1 = int(input("Zadej délku prvního seznamu: "))
arr1 = []


for i in range(delka1):
    arr1.append(int(input(f"Zadej číslo {i + 1} pro první seznam: ")))

# druhý seznam
delka2 = int(input("Zadej délku druhého seznamu: "))
arr2 = []

for j in range(delka2):
    arr2.append(int(input(f"Zadej číslo {j + 1} pro druhý seznam: ")))

arr3 = []

# slučování
for t in range(max(delka1, delka2)):
    if t < delka1:
        arr3.append(arr1[t])
    if t < delka2:
        arr3.append(arr2[t])

print(f"Výsledný seznam {arr3}")