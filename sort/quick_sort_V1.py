def partition(left, right, pivot, numbers):
    count = 0
    while(left <= right):

        while(numbers[left]<pivot):
            count += 1
            left += 1


        while(pivot<numbers[right]):
            count += 1
            right -= 1

        count += 1
        if(left<=right):           
            numbers[left], numbers[right] = numbers[right], numbers[left]
            left += 1
            right -= 1


    return left, count

def quicksort(left, right, numbers):
    step = 0
    if(left < right):
        pivot = numbers[(left + right) // 2]
        mid, partstep = partition(left, right, pivot, numbers)
        step += partstep
        step += quicksort(left, mid - 1,numbers)
        step += quicksort(mid, right ,numbers)
    return step

def quick_sortV1(numbers):
    count = quicksort(0, len(numbers) - 1, numbers)
    return count
