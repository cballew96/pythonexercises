# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the other
# numbers in the original array except the one at index i
# For example, [1,2,3,4,5] returns [120,60,40,30,24] and [3,2,1] returns [2,3,6]

import numpy as np

def product_array(arr):
    product_arr = [1] * len(arr)
    zindex = 1
    xindex = 0
    while xindex < len(arr):
        for x in arr:
            product_arr[xindex] = np.prod(arr[zindex:]) * np.prod(arr[:xindex])

            xindex += 1
            zindex += 1

    print(product_arr)

product_array([3,2,1])
