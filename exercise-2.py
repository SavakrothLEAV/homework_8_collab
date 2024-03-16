""" 
You are given an array with positive numbers and a number N.
You should find the N-th power of the element in the array with the index N. 
If N is outside of the array, then return -1. 
Don't forget that the first element has the index 0.
"""


def index_power(numbers, n):
    # If n is less than the length of the list, 
    # return the value of the element at index n raised to the power of n.
    if n < 0 or n >= len(numbers):
        return -1
    else:
        return numbers[n] ** n


print(index_power([2, 3, 4, 5], 4)) # 16
