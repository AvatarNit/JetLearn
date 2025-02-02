# Task 1
def calculation(a,b):
    return f"{a+b}, {a-b}"
res = calculation(40,10)
print(res)

# Task 2
sum = 0
def sum1to(num):
    global sum
    if num == 0:
        return sum
    sum += num
    return sum1to(num-1)
print(sum1to(10))

# Task 3
def performOp(x,y,op):
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def multi(a,b):
        return a*b
    def divide(a,b):
        return a/b

    if op == "+":
        return add(x,y)
    elif op == "-":
        return sub(x,y)
    elif op == "*":
        return multi(x,y)
    elif op == "/":
        return divide(x,y)

print("5 + 4 =" , performOp(5,4,"+") , "\n5 - 4 =" , performOp(5,4,"-") , "\n5 x 4 =" , performOp(5,4,"*") , "\n5 / 4 =" , performOp(5,4,"/"))

# Task 4
def getEven(list1):
    tempList = []
    for i in list1:
        if i % 2 == 0:
            tempList.append(i)
    return tempList

print(getEven([1,2,3,4,5,6,7,8,9]))
