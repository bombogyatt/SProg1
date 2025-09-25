#V3
def bubblesortV3(seznam):
    pocet_porovnani = 0
    pocet_prvku = len(seznam)


    for i in range(pocet_prvku - 1):

        prohodil_se = False

        for j in range(pocet_prvku - 1 - i):
            pocet_porovnani += 1
            if seznam[j] > seznam[j + 1]:
                seznam[j], seznam[j + 1] = seznam[j+1], seznam[j]
                prohodil_se = True

        if not prohodil_se:
            break

    return pocet_porovnani

