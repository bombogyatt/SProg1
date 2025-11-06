def partition(left, right, pivot, numbers):
    while(left <= right):

        while(numbers[left]<pivot):
            left += 1


        while(pivot<numbers[right]):
            right -= 1

        if(left<=right):           
            numbers[left], numbers[right] = numbers[right], numbers[left]
            left += 1
            right -= 1


    return left

def quicksort(left, right, numbers):
    if(left < right):
        pivot = numbers[(left + right) // 2]
        mid = partition(left, right, pivot, numbers)
        quicksort(left, mid - 1,numbers)
        quicksort(mid, right ,numbers)
    return numbers

