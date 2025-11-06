import time
import copy
from souboj_quick import quicksort

arr = [11, 1, 0, 3, 14, 19, 6, 1, 13, 2, 5, 14, 14, 1, 4, 9, 6, 16, 7, 6]

# python sorting
cas1 = time.time()
vystup_python = sorted(copy.deepcopy(arr))
cas2 = time.time()
delta1 = cas2 - cas1

# muj sorting
cas3 = time.time()
vystup_moje = quicksort(0, len(arr) - 1, copy.deepcopy(arr))
cas4 = time.time()
delta2 = cas4 - cas3

print(vystup_python)
print(f'Pole seřazeno za {delta1}')

print(vystup_moje)
print(f'Pole seřazeno za {delta2}')

