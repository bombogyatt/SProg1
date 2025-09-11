# n...počet lidí
# k...velikost kroku
def daviduv_problem(n, k):
    # naplnění seznamu čísly 1,2,3.... n
    seznam = []
    for i in range(n):
        seznam.append(i + 1)
    print(seznam)
    print("Začátek fce...............")
    
    starting_index = 0
    index_cyklu = 1
    while True:
        if len(seznam) > 1:  
            print(f"Začalo se na pozici {starting_index}")     
            deleting_index = starting_index + (k-1)
            
            if deleting_index >= len(seznam):
                deleting_index -= len(seznam)

            starting_index = deleting_index

            
            vymazane_cislo = seznam.pop(deleting_index)
            print(f"cyklus číslo {index_cyklu}")
            
            print(f"Skončilo se na pozici {deleting_index}")
            print(f"seznam po cyklu {index_cyklu}: {seznam}")
            print(f"vymazané číslo {vymazane_cislo}")
            index_cyklu += 1
            print("----------------------------------")
        elif len(seznam) == 1:
            break
    
    return seznam
    
    

        


#print(daviduv_problem(5, 0))
print(daviduv_problem(5, 3))