import random


# Partition function
def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # Moves left if current number is larger than pivot
        while low <= high and array[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1

        # Finds a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            # Exit the loop
            break

    array[start], array[high] = array[high], array[start]

    return high


# QuickSort function
def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)


# Define array for random numbers
randomList = []

# Loop to generate 1000 random numbers
for i in range(0, 1000):
    n = random.randint(1, 30)
    randomList.append(n)

# Prints the unsorted random number array
print("Unsorted array: ")
print(randomList)

# Calls QuickSort function
quick_sort(randomList, 0, len(randomList) - 1)
print("Sorted array: ")
print(randomList)