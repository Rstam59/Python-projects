arr = [4, 6, 7, 1, 6, 8, 1, 8, 3]
matrix = [
    [1, 9, 0, 65, 75],
    [1, 11, 1, 56, 45],
    [35, 34, 31, 7, 9],
    [36, 7, 16, 50, 3],
    [9, 60, 31, 41, 50]
]
#####################################################
#################selection sort######################
#####################################################
# Python program for implementation of Selection
# Sort
import sys

A = [64, 25, 12, 22, 11]

# Traverse through all array elements
for i in range(len(A)):

    # Find the minimum element in remaining
    # unsorted array
    min_idx = i
    for j in range(i + 1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

        # Swap the found minimum element with
    # the first element
    A[i], A[min_idx] = A[min_idx], A[i]
    print("a")
# Driver code to test above
print("Sorted array")
for i in range(len(A)):
    print("%d" % A[i]),


################################################################################3
# bubble sort
################################################################################[64, 34, 25, 12, 22, 11, 90]
def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

            # Driver code to test above


arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i]),
