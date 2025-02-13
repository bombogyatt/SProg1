cisla = [2, 3, 1, 0, 5, 6, 4, 2]

index_nuly = None
index_trojky = None
indexy_dvojky = []

for i in range(len(cisla)):
    if cisla[i] == 0:
        index_nuly = i
    if cisla[i] == 3:
        index_trojky = i
    if cisla[i] == 2:
        indexy_dvojky.append(i)

print(f"dvojka je na indexech {indexy_dvojky[0]} a {indexy_dvojky[1]}, trojka na {index_trojky}, a nula je na indexu {index_nuly}")
    
