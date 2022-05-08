def bs(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break


arr = [64, 32, 5, 9, 10, 23, 4, 5, 21]

bs(arr)

print("Sorted array is:")

for i in range(len(arr)):
    print(arr[i])
