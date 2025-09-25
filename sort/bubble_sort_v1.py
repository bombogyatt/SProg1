#V1
def bubblesortV1(seznam):
    pocet_porovnani = 0
    pocet_prvku = len(seznam)

    for i in range(pocet_prvku - 1):
        for j in range(pocet_prvku - 1):
            pocet_porovnani += 1
            if seznam[j] > seznam[j + 1]:
                seznam[j], seznam[j + 1] = seznam[j+1], seznam[j]
     
    return pocet_porovnani