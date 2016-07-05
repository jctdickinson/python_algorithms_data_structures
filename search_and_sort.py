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

# Sequential search
# For loop iteration not working for some (probably obvious) reason..
# This version uses a flag
def sequential_search(a_list, item):
    # for i in range(len(a_list)):
    #     print(i)
    #     if a_list[i] is item:
    #         return True
    #     else:
    #         return False
    in_list = False
    index = 0

    while index < len(a_list) and not in_list:
        if a_list[index] is item:
            in_list = True
        else:
            index += 1

    return in_list


def binary_search(a_list, item):
    if len(a_list) is 0:
        return False
    else:
        # List must be sorted for binary_search to work
        # Temporarily using insertion sort
        insertion_sort(a_list)
        midpoint = len(a_list) // 2
        if a_list[midpoint] is item:
            return True
        else:
            if item < a_list[midpoint]:
                return binary_search(a_list[:midpoint], item)
            else:
                return binary_search(alist[midpoint + 1:], item)


# Generates list of user-defined number of elements
def generate_list(list_size):
    a_list = []
    for i in range(list_size):
        a_list.append(random.randint(0, 99))
    return a_list


# Semi-optimized bubble sort algorithm
# Time complexity: O(n**2)
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


# Selection sort, sorted by lowest value or highest value
# Time complexity: O(n**2)
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


# Insertion sort
# Time complexity O(n**2)
def insertion_sort(a_list):
    # Sorting starts from left, so first element is considered sorted
    for i in range(1, len(a_list)):
        # Save current value from element 1
        current_value = a_list[i]
        # Store position to compare with current_value as element one to the left
        position = i - 1

        # As long as position is greater, loop
        while (position >= 0) and (a_list[position] > current_value):
            # Shift value of greater number up one index
            a_list[position + 1] = a_list[position]
            # Decrement position value for next iteration
            position -= position
        # Change current_value to continue iteration and avoid infinite loop
        a_list[position] = current_value
    return a_list

my_list = generate_list(20)
print("Randomly-generated list to feed sequential search (testing against value of 10):\n", my_list)
print("Sequential search results:\n", sequential_search(my_list, 10), "\n")

my_list = generate_list(20)
print("Randomly-generated list to feed sequential search (testing against value of 10):\n", my_list)
print("Binary search results:\n", binary_search(my_list, 10), "\n")

my_list = generate_list(10)
print("Randomly-generated list to feed bubble sort:\n", my_list)
print("Bubble sort results:\n", bubble_sort(my_list), "\n")

my_list = generate_list(10)
print("Randomly-generated list to feed selection sort:\n", my_list)
print("Selection sort results:\n", selection_sort(my_list), "\n")

my_list = generate_list(10)
print("Randomly-generated list to feed insertion sort:\n", my_list)
print("Insertion sort results:\n", selection_sort(my_list))