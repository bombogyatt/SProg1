import copy
import random
import time
def measure_sorts():
    unsorted_list = [9, 8, 7, 6, 5, 4]

    #V1
    list_copy = copy.deepcopy(unsorted_list)
    time_start = time.perf_counter()
    comparisons = bubblesortV1(list_copy)
    time_end = time.perf_counter()

    execution_time = time_end - time_start
    print(f"BubbleV1 - pocet porovnani: {comparisons}, cas: {execution_time}")

    #V2
    list_copy = copy.deepcopy(unsorted_list)
    time_start = time.perf_counter()
    comparisons = bubblesortV2(list_copy)
    time_end = time.perf_counter()

    execution_time = time_end - time_start
    print(f"BubbleV2 - pocet porovnani: {comparisons}, cas: {execution_time}")

    #V3
    list_copy = copy.deepcopy(unsorted_list)
    time_start = time.perf_counter()
    comparisons = bubblesortV3(list_copy)
    time_end = time.perf_counter()

    execution_time = time_end - time_start
    print(f"BubbleV3- pocet porovnani: {comparisons}, cas: {execution_time}")




def prehod_poradi(index_1, index_2, seznam):
    mezi_cislo = seznam[index_1]
    seznam[index_1] = seznam[index_2]
    seznam[index_2] = mezi_cislo

#V1
def bubblesortV1(seznam):
    index = 0
    pocet_porovnani = 0
    while index < len(seznam):
        for i in range(len(seznam)-1):
            pocet_porovnani += 1 
            if(seznam[i] > seznam[i+1]):
                prehod_poradi(i, i+1, seznam)                  
        index += 1
    return pocet_porovnani

#V2
def bubblesortV2(seznam):
    pocet_porovnani = 0
    for j in range(len(seznam)-1):
        for i in range(len(seznam)-1-j):
            pocet_porovnani += 1
            if(seznam[i] > seznam[i+1]):
                prehod_poradi(i, i+1, seznam) 
                
        j += 1     
    return pocet_porovnani

#V3
def bubblesortV3(seznam):
    prohozeno = None
    pocet_porovnani = 0
    for j in range(len(seznam)-1):
        for i in range(len(seznam)-1-j):
            pocet_porovnani += 1
            if(seznam[i] > seznam[i+1]):
                prehod_poradi(i, i+1, seznam)
                prohozeno = True
                
        j += 1
        if not prohozeno:   
            return pocet_porovnani  
        prohozeno = False
    return pocet_porovnani

#V4
def bubblesortV4(seznam):
    pocet_porovnani = 0
    for j in range(len(seznam)-1):
        for i in range(len(seznam)-1-j):
            pocet_porovnani += 1
            if(seznam[i] > seznam[i+1]):
                prehod_poradi(i, i+1, seznam) 
                
        j += 1     
    return pocet_porovnani

seznam = [ 8, 7, 4, 5, 1]
seznam2 = [1, 4, 5, 7, 8]

measure_sorts()

