def analyzuj_text(text):

    vysledek = {
        "pocet_znaku": 0,
        "pocet_pismen": 0,
        "pocet_slov": 0,
        "pocet_vet": 0,
        "prumerna_delka_slova": 0,
        "nejdelsi_slovo": 0,
        "nejkratsi_slovo": 0
    }

    if not text:
        return vysledek
    
    vysledek["pocet_znaku"] = len(text)

    slova = text.split()

    vysledek["pocet_slov"] = len(slova)

    text.replace("?", ".").replace("!", ".")
    vety = text.split(".")

    vysledek["pocet_vet"] = len(vety)

    vysledek["nejdelsi_slovo"] = max(slova, key=len)
    vysledek["nejkratsi_slovo"] = min(slova, key=len)


