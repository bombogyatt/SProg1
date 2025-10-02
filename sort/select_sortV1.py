def select_sortV1(seznam):
    pocet_porovnání = 0
    cislo_hodnota = 0
    cislo_index = 0
    start = 0
    delka_seznamu = len(seznam)

    #print(seznam)

    for j in range(delka_seznamu - 1):  

        cislo_hodnota = seznam[start]
        cislo_index = start 
        #print(f'cyklus cislo {j+1}')
        for i in range(start, delka_seznamu - 1, 1):
            
            #print(f'porovnávání číslo {i +1}')
            #zapise si hodnotu prvniho cisla a jeho index
            pocet_porovnání += 1   
            if cislo_hodnota > seznam[i]:
                cislo_hodnota = seznam[i]
                cislo_index = i 

        seznam[start], seznam[cislo_index] = seznam[cislo_index], seznam[start]
        #print(f'seznam po {j + 1}. serazení: {seznam}')
        start += 1

    #print(seznam)

    return pocet_porovnání


