text = input("Zadej text: ")
slovnik_slov = {}

seznam_slov = text.split(" ")

for slovo in seznam_slov:
    if slovnik_slov.get(slovo) == None:
        slovnik_slov[slovo] = 1
    else:
        slovnik_slov[slovo] += 1

print(slovnik_slov)