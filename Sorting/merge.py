def merge(list):
    if len(list) > 1:
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]
        merge(left)
        merge(right)
        i = j = k = 0

        while len(left) > i and len(right) > j:
            if left[i] < right[j]:
                list[k] = left[i]
                i = i+1
                k = k+1
            else:
                list[k] = right[j]
                j = j+1
                k = k+1

        while len(left) > i:
            list[k] = left[i]
            i = i+1
            k = k+1
        while len(right) > j:
            list[k] = right[j]
            j = j+1
            k = k+1


num = int(input("Elements number:"))

list = [int(input()) for x in range(num)]
merge(list)

print("Sorted list:", list)
