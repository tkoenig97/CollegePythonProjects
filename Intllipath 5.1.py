def swapElement(list, pos1, pos2):
    get = list[pos1], list[pos2]

    list[pos2], list[pos1] = get

    return list


def bubbleSort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


array = [3, 44, 45, 10, 15, 16, 9, 11]

bubbleSort(array)

for i in range(len(array)):
    print("%d" % array[i]),