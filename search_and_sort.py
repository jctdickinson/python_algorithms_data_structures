"""
Collection of sorting algorithms in Python

"""

import random


# Generates list of user-defined number of elements
def generate_list(list_size):
    a_list = []
    for i in range(list_size):
        a_list.append(random.randint(0, 99))
    return a_list


# Semi-optimized bubble sort algorithm
# Time efficiency: O(n^2)
def bubble_sort(a_list):
    for i in range(len(a_list) - 1, 0, -1):
        # To keep track of number of swaps
        count = 0
        for j in range(i):
            if a_list[j] > a_list[j + 1]:
                swap_value = a_list[j]
                a_list[j] = a_list[j + 1]
                a_list[j + 1] = swap_value
                # Optimization: Increment count for every swap
                count += 1
        # Optimization:
        # After iteration of every member of list, if there have been no swaps,
        # list is sorted and it is safe to break our outer loop
        if count is 0:
            break
    return a_list



my_list = generate_list(10)
print(my_list)
print(bubble_sort(my_list))