import matplotlib.pyplot as plt
import numpy as np

# x = [1,2,3,4,5]
# y = [1,2,3,4,5]

# plt.plot(x,y)
# plt.show()
# # Can be r,g,b with o,^,--,-
# plt.plot(x,y,"ro")
# plt.show()

# plt.plot(x,y)
# plt.axis([0,10,0,200])
# plt.show()

# plt.plot(x,y, "r--", label="Y = X", linewidth=4)
# plt.axis([0,10,0,50])
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Graph")
# plt.legend()
# plt.show()


# x = np.arange(0,10,0.2)
# y1 = x ** 2
# y2 = x ** 3

# plt.plot(x, y1,"g--",x,y2,"b--")
# plt.show()

# # generate 100 points between -5 and 5
# x = np.linspace(-5,5,100)
# y = (2 * x) + 1

# plt.plot(x,y,"ro",label="Y = 2x + 1")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("Y = mx+b")
# plt.legend()

# plt.show()

# # x = position of bar
# # y = length of bar

# x=[1,3,5,7]
# y=[2,6,4,9]

# plt.bar(x,y,color="b")
# plt.show()

# x=[1,3,5,7]
# y=[2,6,4,9]
# x2 = [2,4,6,8]
# y2=[1,2,3,4]

# plt.bar(x,y,color="b")
# plt.bar(x2,y,color="g")
# plt.show()

# plt.bar(["Male Literacy","Female Literacy"],[90,95])
# plt.show()

# class1 = int(input("How many in the first class: "))
# class2 = int(input("How many in the second class: "))
# class3 = int(input("How many in the third class: "))

# plt.bar(["First Class", "Second Class", "Third Class"],[class1,class2,class3])
# plt.show()

# x = []
# y = []

# for i in range(5):
#     x.append(int(input("Please enter a number: ")))

# for xVal in x:
#     y.append((xVal * 4) + 10)
# print(x)
# print(y)

# plt.plot(x,y,"go",label="Y=4x+10")
# plt.xlabel("X from user")
# plt.ylabel("Y from Y=4x+10")
# plt.legend()
# plt.show()

x = np.arange(1,30)
y = (x ** 2) + (x*3) + 10

plt.plot(x,y,"r--",label="Y=x^2+3x+10")
plt.xlabel("X from 1 to 30")
plt.ylabel("Y")
plt.legend()
plt.show()