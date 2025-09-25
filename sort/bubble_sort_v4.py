#V4
# nerfunguje prohzavání smerem zpatky
def bubblesortV4(seznam):
    pocet_porovnani = 0
    pocet_prvku = len(seznam)

    # prvni a posledni index podle ktereho radime
    start = 0
    end = len(seznam) - 1

    print(seznam)

    for j in range(pocet_prvku - 1):
        #kontrola serazenosti
        prohozeno = False

        for i in range(start, end, 1):
            pocet_porovnani += 1
            if seznam[i] > seznam [i + 1]:
                seznam[i], seznam[i + 1] = seznam[i+1], seznam[i]
                prohozeno = True
        end -= 1

        if not prohozeno:
            break

        prohozeno = False

        for i in range(end, start, 1):
            pocet_porovnani += 1
            if seznam[i] < seznam[i - 1]:
                seznam[i], seznam[i - 1] = seznam[i - 1], seznam[i]
                prohozeno = True
        start += 1

        if not prohozeno:
            break


    print(seznam)


    return pocet_porovnani