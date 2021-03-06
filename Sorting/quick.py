def pivot(list, first, last):
    pivot = list[first]
    left = first+1
    right = last
    while True:
        while left <= right and list[left] <= pivot:
            left = left+1
        while left <= right and list[right] >= pivot:
            right = right - 1
        if right < left:
            break
        else:
            list[left], list[right] = list[right], list[left]
    list[first], list[right] = list[right], list[first]
    return right


def quick(list, first, last):

    if first < last:
        p = pivot(list, first, last)
        quick(list, first, p-1)
        quick(list, p+1, last)


list = [23, 28, 65, 18, 22, 32, 23, 98, 66]
n = len(list)
quick(list, 0, n-1)
print(list)
