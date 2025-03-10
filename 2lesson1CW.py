import numpy as np

list1 = [1,2,3,4,5]
print(type(list1))

arr1 = np.array(list1)
print(type(arr1))

arr2 = np.array([6,7,8,9,10])
print(type(arr2))

arr2 += 1
print(arr2)

# list1 += 1
# print(list1)
for i in range(len(list1)):
    list1[i] += 1
print(list1)

# Arr can only be 1 data type

# arr3 = np.array([1,3,5,7], "Hello")
# print(arr3)

arr4 = np.zeros(4)
print(arr4)
arr5 = np.ones(7)
print(arr5)

arr6 = np.array([0,10,20,30],dtype="f")
print(arr6)

# ERROR Uneven shape
# arr7 = np.array([[1,2],[3,4],[5,6,7]])

arr7 = np.array([[1,2],[3,4],[5,6]])
print(arr7)

print(arr7.ndim) 
print(arr7.shape)
print(arr7.size)
print(arr7.nbytes) # each element is 4 bytes

arr8 = np.arange(5,60)
print(arr8)

arr9 = np.arange(10,928,50) #start,stop,step
print(arr9)

arr10 = np.arange(2,101,2)
print(arr10)
arr11 = np.arange(1,100,2)
print(arr11)

num1 = np.random.randint(0,100)
print(num1)

arr12 = np.random.permutation(np.arange(10,21))
print(arr12)
arr13 = np.random.permutation(15)
print(arr13)

# 1 arr
arr14 = np.random.rand(1,20)
print(arr14)
# 2 arr
arr15 = np.random.rand(2,20)
print(arr15)

arr16 = np.arange(1,10)
print(arr16)
arr16 = arr16.reshape(3,3)
print(arr16)

arr17 = np.arange(1,37)

print(arr17.reshape(2,18))
print(arr17.reshape(3,12))
print(arr17.reshape(4,9))
print(arr17.reshape(6,6))
print(arr17.reshape(18,2))
print(arr17.reshape(12,3))
print(arr17.reshape(9,4))


arr18 = np.random.permutation(101)
print(arr18)
print(np.sort(arr18))