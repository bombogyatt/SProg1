def pocet_cislic(cislo):
    cislice = 0
    for i in str(abs(cislo)):
        cislice += 1
    
    return cislice

print(pocet_cislic(12345))  # 5
print(pocet_cislic(-27))  # 2
print(pocet_cislic(0))  # 1
