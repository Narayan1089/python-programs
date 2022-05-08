import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, ])


def pro(array):
    mx = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] * array[j] > mx:
                mx = array[i] * array[j]
                pairs = str(array[i]) + "," + str(array[j])
    print(pairs)
    print(mx)


pro(arr)
