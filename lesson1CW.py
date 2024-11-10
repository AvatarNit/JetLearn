import numpy as np

# from random import randint
# array:
list = [1,2,3,4,5]
print(list)

numpy_arr = np.array(list)
print(numpy_arr)

words = ["nishtha", "nithik", "rynav"]
numpy_words = np.array(words)
print(numpy_words)

a = np.array([1,2,3])
b = np.array([[1,2], [3,4]])
print(b)

# ndim --> dimension of array
print(a.ndim)
print(b.ndim)

# The shape of an array
c = np.array([[1,2], [3,4], [4,5], [5,6]])
print(c.shape)

# Multidimensional Array
d = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
print(c)

# Accessing elements
e = np.array([[10,20,30], [40,50,60]])
print(e[0][1])
print(e[1][-1])

# arrange() --> 
f = np.arange(0, 10, 2)
print(f)

# reshaping of array
g = np.array([1,2,3,4,5,6])
new_g = g.reshape(2,3)
print(new_g)

# permutation --> random shuffled array
h = np.array([1,2,3,4,5])
print(np.random.permutation(h))

# sorting
i = np.array([6,5,7,3,2])
print(np.sort(i))