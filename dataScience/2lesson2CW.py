import numpy as np

arr1 = np.array([1,2,3,4,5,6,7,8,9,10])

# Slicing operator :

print(arr1[0])
print(arr1[0:5])
print(arr1[4:])
print(arr1[:5])

print(arr1[0:10:2])
print(arr1[1:10:2])

# Reverse
print(arr1[::-1])

arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2)
print(arr2[0:2,0:2])

arr3 = np.arange(1,50)
print(arr3)

arr3 = arr3.reshape(7,7)
print(arr3)

print(arr3[2:5,2:5])

arr4 = np.arange(1,37)

print(arr4.reshape(2,18))
print(arr4.reshape(3,12))
print(arr4.reshape(4,9))
print(arr4.reshape(6,6))
print(arr4.reshape(18,2))
print(arr4.reshape(12,3))
print(arr4.reshape(9,4))

arr5 = np.arange(1,101)
print(arr5.reshape(2,50))
print(arr5.reshape(4,25))
print(arr5.reshape(5,20))
print(arr5.reshape(10,10))
print(arr5.reshape(50,2))
print(arr5.reshape(25,4))
print(arr5.reshape(20,5))

# Conditionals

arr6 = np.array([1,2,3,4,5,6,7,8,9,10])
evenArr6 = arr6[arr6%2 == 0]
oddArr6 = arr6[arr6%2 != 0]
print(evenArr6)
print(oddArr6)

print(arr6[arr6==5])
print(arr6[arr6==11])
print(arr6[[2,4,6]])
print(arr6[arr6<5])

arr6 += 10
print(arr6)

arr7 = np.array([1,2,3,4,5])
arr8 = np.array([6,7,8,9,10])

print(arr7 + arr8)
print(arr7 - arr8)

arr9 = np.random.permutation(np.arange(1,17)).reshape(4,4)
print(arr9)

arr10 = np.random.permutation(np.arange(1,17)).reshape(4,4)
print(arr10)

print(arr9+arr10)

def linearE(x):
    return 2 * x + 1

print(linearE(10))
print(linearE(np.arange(1,6)))

def quadE(x):
    return x**2 + 5 * x + 10
print(quadE(1))
print(quadE(np.arange(1,6)))