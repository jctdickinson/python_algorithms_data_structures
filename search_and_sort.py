"""
Collection of sorting and searching algorithms in Python
By jctdickinson
https://github.com/jctdickinson

I would like to eventually add a suitable suite of unit tests to demonstrate
each algorithm with its respective time complexity but for now playing with
the provided generate_list function should suffice.

A comparison of sorting algorithms to built in list.sort() would be fun.

Thinking of adding swap function, but for now keeping each algorithm as modularly
contained as possible.

"""

import random


# Generates list of user-defined number of elements
def generate_list(list_size):
    a_list = []
    for i in range(list_size):
        a_list.append(random.randint(0, 99))
    return a_list


# Semi-optimized bubble sort algorithm
# Time complexity: O(n^2)
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


# Sort by lowest value or highest value
# Time complexity: O(n^2)
def selection_sort(a_list):
    for i in range(len(a_list)):
        # In this case we will sort by lowest value
        min_value = i
        for j in range(i + 1, len(a_list)):
            if a_list[j] < a_list[min_value]:
                min_value = j
        swap_value = a_list[min_value]
        a_list[min_value] = a_list[i]
        a_list[i] = swap_value
    return a_list


my_list = generate_list(10)
print("Randomly-generated list to throw at bubble sort:\n" + str(my_list))
print("Bubble sort results:\n" + str(bubble_sort(my_list)))

my_list2 = generate_list(10)
print("Randomly-generated list to throw at selection sort:\n" + str(my_list2))
print("Selection sort results:\n" + str(selection_sort(my_list2)))