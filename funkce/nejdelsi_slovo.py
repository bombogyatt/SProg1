def nejdelsi_slovo(text):
    seznam_slov = text.split(" ")
    nejdelsi_slovo = "a"
    for i in range(len(seznam_slov)):
        if len(seznam_slov[i]) > len(nejdelsi_slovo):
            nejdelsi_slovo = seznam_slov[i]

    return nejdelsi_slovo


print(nejdelsi_slovo("Včera jsme šli na výlet do hor"))  # "výlet"