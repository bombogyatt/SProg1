seznam = [8, 8, 2, 7, 4, 5, 3, 2, 6, 1, 10, 8, 9, 2, 3]

def partition(left, right, list):
    
    # vybrání pivota
    pivot_pos = int(len(list)/2)
    pivot = list[pivot_pos]
    print(f'pivot je {pivot} na pozici {pivot_pos}')

    i = left
    j = right

    while i <= j:

        while True:
            if list[i] > pivot:
                break
            else:
                i += 1



        


partition(0, 14, seznam)

