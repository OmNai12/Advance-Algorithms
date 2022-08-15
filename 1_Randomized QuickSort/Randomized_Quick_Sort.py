# By Om Nai

import random

# Declaring a global variable for counting the number of swaps done
global count_var
count_var = 0


# Partition Function
def Partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        global count_var
        count_var += 1
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


# This will do random partition of an array
def Randomized_Partition(a, p, r):
    i = random.randint(p, r)
    a[i], a[r] = a[r], a[i]
    return Partition(a, p, r)


# Randomized Quick sort
def Randomize_QuickSort(a, p, r):
    if p < r:
        q = Randomized_Partition(a, p, r)
        Randomize_QuickSort(a, p, q - 1)
        Randomize_QuickSort(a, q + 1, r)
    pass


if __name__ == "__main__":
    arr = [9, 7, 5, 6, 48, 12, 74, 3, 12, 14, 36, 56, 74, 96]
    Randomize_QuickSort(arr, 0, len(arr) - 1)
    print("Number of comparisons are : ", count_var)
    print("The sorted array is as under :-")
    print(arr)
