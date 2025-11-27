import time
import copy
import random
from souboj_quick import quicksort

unsorted_list = [random.randint(0, 10000) for i in range(1000000)]

# python sorting
cas1 = time.time()
vystup_python = sorted(copy.deepcopy(unsorted_list))
cas2 = time.time()
delta1 = cas2 - cas1

# muj sorting
cas3 = time.time()
vystup_moje = quicksort(0, len(unsorted_list) - 1, copy.deepcopy(unsorted_list))
cas4 = time.time()
delta2 = cas4 - cas3


print(f'Pole seřazeno za {delta1}')

print(f'Pole seřazeno za {delta2}')

