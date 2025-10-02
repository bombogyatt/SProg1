#dodelat i s optimalizacemi
def insert_sortV1(seznam):
    pocet_porovnani = 0
    delka_seznamu = len(seznam)
    start = 1

    prvek_index = 0
    prvek_hodnota = 0

    for i in range (start, delka_seznamu):

        # i == start
        for j in range(i, 0, -1):

            pocet_porovnani += 1
            if seznam[j] < seznam[j - 1]:
                seznam[j], seznam[j - 1] = seznam[j - 1], seznam[j]
            else:
                break

        start += 1


    return pocet_porovnani


