def pocitani_slov(text, min_delka = 3):
    slova = text.split(" ")
    slovnik_slov = {}
    for i in range(len(slova)):
        if slovnik_slov.get(slova[i]) == None and len(slova[i]) >= min_delka:
            slovnik_slov[slova[i]] = 1
        elif len(slova[i]) >= min_delka:
            slovnik_slov[slova[i]] += 1

    return slovnik_slov


print(pocitani_slov("Python je skvělý, Python je mocný programovací jazyk."))
# {'python': 2, 'skvělý': 1, 'mocný': 1, 'programovací': 1, 'jazyk': 1}

print(pocitani_slov("Ahoj jak se máš", min_delka=4))
# {'ahoj': 1}
            

 



