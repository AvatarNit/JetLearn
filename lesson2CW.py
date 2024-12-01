# array slicing
# conditioning sectioning
# mathematical operations
# logical operations
import numpy as np
# create 1d array
arr1d = np.array([10,20,30,40,50])

# slicing the array
slice1d = arr1d[1:4]
print("array slicied: ", slice1d)

# 2d array slicing
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
slice2d = arr2d[0:2 , 1:3]
slice2d2 = arr2d[1:3 , 0:2]
print(slice2d)

# condition section
condition = arr1d > 25
# filtering the elements greater than 25
filtered_arr = arr1d[condition]
print(filtered_arr)
# ans: 30,40,50

# mathematical operations
arr_squared = arr1d ** 2
print(arr_squared)
# ans: [ 100  400  900 1600 2500]

# 2d array
arr_squared2 = arr2d ** 2
print(arr_squared2)
# [[ 1  4  9]
#  [16 25 36]
#  [49 64 81]]

# 2d --> +,-
# create 2d array
# another 2d
# input as operator

arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])

# op = input("Input an operator(+,-): ")

# if op == "+":
#     print(arr1+arr2)
# elif op == "-":
#     print(arr1-arr2)
# else:
#     print("Incorrect Input")

# logical operations
arr1d1 = np.array([True,False,True,False])
arr1d2 = np.array([True,True,False,False])

print(arr1d1 & arr1d2)
# ans: [ True False False False]

print(arr1d1 | arr1d2)
# ans: [ True  True  True False]

# not operator (~)
print(~arr1d1)
# ans: [False  True False  True]

# xor --> Exclusive or (^)
# T , T : F
# F , F : F
# T , F : T
# F , T : T
print(arr1d1^arr1d2)
# ans: [False  True  True False]

# NUMPY FUNCTIONS
print(np.sum(arr2d)) # sum all of elements
print(np.mean(arr2d)) # mean of all elements
print(np.min(arr2d)) # minimum element
print(np.max(arr2d)) # maximum element

# functions for logical operations
print(np.logical_and(arr1d1,arr1d2)) # and operator
print(np.logical_or(arr1d1,arr1d2)) # or operator
print(np.logical_not(arr1d1)) # not operator
print(np.logical_xor(arr1d1,arr1d2)) # xor operator


# TODO: functions

def add_constant(arr,constant):
    return arr + constant

arr = np.array([1,2,3])
result = add_constant(arr,5)
print("result after adding constant: ", result)
