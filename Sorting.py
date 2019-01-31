import pandas as pd
import numpy as np
import random


# Bubble Sort
# Bubble Sort is an algorithm which is used to sort N elements that are given in a memory
# an Array with N number of elements. Bubble Sort compares all the element one by one and sort them based on their values

def BubbleSort(ls):
    for i in range(0, len(ls)):
        # print(i)
        flag = 0
        for j in range(0, len(ls) - i - 1):
            # print(j)
            t = 0
            # print(ls)
            if ls[j + 1] < ls[j]:
                t = ls[j]
                ls[j] = ls[j + 1]
                ls[j + 1] = t
                flag = 1
            # print(ls)
        if (flag == 0):
            break
    return ls


###Time Complexity

# Best case O(n^2)
# Worst case O(n^2)
# Average Case O(n) (If already sorted array os passed)


# Insertion sorting
# It is a simple Sorting algorithm which sorts the array by shifting elements one by one.
# It has one of the simplest implementation
# It is efficient for smaller data sets, but very inefficient for larger lists.
# Insertion Sort is adaptive, that means it reduces its total number of steps if given a partially sorted list,
# hence it increases its efficiency.
# It is better than Selection Sort and Bubble Sort algorithms. number of comparisons is less
# Its space complexity is less. Like Bubble Sorting, insertion sort also requires a single additional memory space.
# It is a Stable sorting, as it does not change the relative order of elements with equal keys
# Pick second key and compare from left and insert to its suitable place


def InsertionSort(ls_insert):
    for i in range(1, len(ls_insert)):
        temp = 0
        for j in range(0, i):
            if ls_insert[i] < ls_insert[j]:
                temp = ls_insert[i]
                ls_insert.pop(i)
                ls_insert.insert(j, temp)
                continue
        # print(ls_insert)
    return ls_insert


###Time Complexity

# Best case O(n) input is sorted array
# Worst case O(n^2) when input is reversed sorted
# Average Case O(n^2)


# Selection sorting
# Selection sorting is conceptually the most simplest sorting algorithm.
# This algorithm first finds the smallest element in the array and exchanges
# it with the element in the first position, then find the second smallest element
# and exchange it with the element in the second position, and continues in this way
# until the entire array is sorted.

def SelectSort(ls_sel):
    for i in range(0, len(ls_sel) - 1):
        min_val = i
        for j in range(i + 1, len(ls_sel)):
            if (ls_sel[j] < ls_sel[min_val]):
                min_val = j
                # print(min_val)
        temp = ls_sel[i]
        ls_sel[i] = ls_sel[min_val]
        ls_sel[min_val] = temp
        # print(ls_sel)


###Time Complexity

# Best case O()
# Worst case O(n^2)
# Average Case O()

# Merge Sort
# Merge Sort follows the rule of Divide and Conquer. Stable sorting.
# In merge sort the unsorted list is divided into N sublists, each having one element, because a list consisting of one element is always sorted.
# Then, it repeatedly merges these sublists, to produce new sorted sublists, and in the end, only one sorted list is produced.
# Merge Sort is quite fast, and its not inplace sorting algo.

def MergeSort(alist):
    if len(alist) > 1:
        mid = int(len(alist) / 2)
        left_s = alist[:mid]
        right_s = alist[mid:]

        MergeSort(left_s)
        MergeSort(right_s)
        # print("break")
        # print(left_s)
        # print(right_s)
        i, j, k = 0, 0, 0
        while i < len(left_s) and j < len(right_s):

            if left_s[i] < right_s[j]:
                alist[k] = left_s[i]
                i = i + 1
            else:
                alist[k] = right_s[j]
                j = j + 1
            k = k + 1
            # print("after first loop")
            # print(alist)
        while i < len(left_s):
            alist[k] = left_s[i]
            i = i + 1
            k = k + 1
        while j < len(right_s):
            alist[k] = right_s[j]
            j = j + 1
            k = k + 1
        # print(alist)
    return alist


# Best case O()
# Worst case O(nlogn)
# Average Case O()
# Space Complexity O(nlogn)-Worst case
#                 O(n)- Best case


# Quick Sort Algorithm
# Quick Sort,sorts any list very quickly. It is insort algorithm
# Quick sort is not a stable search, but it is very fast and requires veryless additional space.
# It is based on the rule of Divide and Conquer(also called partition-exchange sort).
# Randomly choose pivot, divide list in 2 left less than pivot right greater than pivot,repeat the same steps

def quickSort(alist):
    quickSortinner(alist, 0, len(alist) - 1)
    return alist


def quickSortinner(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        quickSortinner(alist, first, splitpoint - 1)
        quickSortinner(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]

    left_in = first + 1
    right_in = last

    done = False
    while not done:

        while left_in <= right_in and alist[left_in] <= pivotvalue:
            left_in = left_in + 1

        while alist[right_in] >= pivotvalue and right_in >= leftmark:
            right_in = right_in - 1

        if right_in < left_in:
            done = True
        else:
            temp = alist[left_in]
            alist[left_in] = alist[right_in]
            alist[right_in] = temp

    temp = alist[first]
    alist[first] = alist[right_in]
    alist[right_in] = temp

    return right_in


# Time Complexity
# Best case O()
# Worst case O(n^2)
# Average Case O(nlogn) -
# Space Complexity O(logn) -Average case
#                 O(n)    -Worst case


if __name__ == '__main__':
    ls = [8, 1, 3, 1, 5, 2, 3, 4, 5, 2]

    ls_bub = BubbleSort(ls)
    print(ls_bub)

    ls_ins = InsertionSort(ls)
    print(ls_ins)

    ls_sel = SelectSort(ls)
    print(ls_sel)

    ls_mer = MergeSort(ls)
    print(ls_mer)

    ls_qui = quickSort(ls)
    print(ls_qui)


