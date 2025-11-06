def merge_sortV1(numbers):
    left = None
    right = None

    # rozdeleni prvku
    if len(numbers) > 1:
        mid = len(numbers) // 2

        left = merge_sortV1(numbers[:mid])
        right = merge_sortV1(numbers[mid:])


    # merge(left, right)
    #i = len(left)
    #j = len(right)

def merge(left, right):
    new_arr = []
    l = 0
    r = 0

    while(True):
        if left[l] < right[r]:
            new_arr.append(left[l])
            if not l == (len(left) - 1):
                l += 1
        elif right[r] < left[l]:
            new_arr.append(right[r])
            if not r == (len(right) - 1):
                r += 1
        elif right[r] == left[l]:
            new_arr.append(left[l])
            new_arr.append(right[r])
            if
                r += 1
                l += 1

        if(l > len(left) - 1) and (r > len(right) - 1):
            break
    
    return new_arr

print(merge([1, 2, 3, 4, 4], [6, 7, 8, 98]))



arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16, 17, 18,19]

merge_sortV1(arr)