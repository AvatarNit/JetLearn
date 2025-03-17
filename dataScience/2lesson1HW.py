import numpy as np

arr1 = np.array(input("Enter the first array seperated by commas: ").split(","),dtype="i")
arr2 = np.array(input("Enter the second array seperated by commas: ").split(","),dtype="i")

while True:
    op = input("Enter the operation (+,-,or Q to quit): ")
    if op == "+":
        print(arr1 + arr2)
    elif op == "-":
        print(arr1-arr2)
    elif op == "Q":
        print("Bye")
        break
    else:
        print("Please enter a valid choice!!!")