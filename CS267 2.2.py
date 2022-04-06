import random


# Binary Search Function
def binarySearch(arr, l, r, x):
    # Check base case
    if r >= l:

        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

            # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

            # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1


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
print("Randomly generated list:")
print(randomList)

# Generates random number to be searched
searchedValue = random.randint(0, 50)

# Sorts randomList in order to be searched
quick_sort(randomList, 0, len(randomList) - 1)
print("Sorted List:")
print(randomList)

# Calls Binary Search function
res = binarySearch(randomList, 0, len(randomList)-1, searchedValue)
print("Result:")
if res == -1:
    print(searchedValue, "not found")
else:
    print(searchedValue, "found at", res)