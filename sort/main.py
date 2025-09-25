import copy
import random
import matplotlib.pyplot as plt

from bubble_sort_v1 import bubblesortV1
from bubble_sort_v2 import bubblesortV2
from bubble_sort_v3 import bubblesortV3
from bubble_sort_v4 import bubblesortV4


def measure_sorts():
    lists_lens = [n for n in range(10, 50, 10)]

    bubbleV1_results = []
    bubbleV2_results = []
    bubbleV3_results = []
    bubbleV4_results = []

    for n in range(10, 50, 10):
        unsorted_list = [random.randint(0, n**2) for i in range(n)]

        bubbleV1_results.append(bubblesortV1(copy.deepcopy(unsorted_list)))
        bubbleV2_results.append(bubblesortV2(copy.deepcopy(unsorted_list)))
        bubbleV3_results.append(bubblesortV3(copy.deepcopy(unsorted_list)))
        #bubbleV4_results.append(bubblesortV4(copy.deepcopy(unsorted_list)))

    plt.plot(lists_lens, bubbleV1_results, label='bubble V1', color = 'blue')
    plt.plot(lists_lens, bubbleV2_results, label='bubble V2', color = 'red')
    plt.plot(lists_lens, bubbleV3_results, label='bubble V3', color = 'green')
    #plt.plot(lists_lens, bubbleV4_results, label='bubble V4', color = 'brown')


    plt.legend()
    plt.show()
    
bubblesortV4([1, 6, 2, 5, 4, 0])

measure_sorts()






