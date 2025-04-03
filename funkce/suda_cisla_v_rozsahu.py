def vypis_suda_od_do(zacatek, konec):
    if zacatek > konec:
        return None
    
    for i in range(zacatek, konec + 1):
        if i % 2 == 0:
            print(f"{i} ")

vypis_suda_od_do(4, 12)
vypis_suda_od_do(4, 4)
vypis_suda_od_do(6, 4)