import matplotlib.pyplot as plt

def linear_equation(m,b):
    xVals = []
    yVals = []
    for x in range(51):
        xVals.append(x)
        yVals.append(m*x + b)
    print(xVals)
    print(yVals)
    plt.plot(xVals,yVals)

def quadratic_equation(a,b,c):
    xVals = []
    yVals = []
    for x in range(51):
        xVals.append(x)
        yVals.append(a*x**2 + b*x + c)
    print(xVals)
    print(yVals)
    plt.plot(xVals,yVals)

def cubic_equation(a,b,c,d):
    xVals = []
    yVals = []
    for x in range(51):
        xVals.append(x)
        yVals.append(a*x**3 + b*x**2 + c*x + d)
    print(xVals)
    print(yVals)
    plt.plot(xVals,yVals)

print("1. Linear equation\n2. Quadratic equation\n3. Cubic equation")
choice = int(input(": "))

if choice == 1:
    print("y = mx + b")
    m = float(input("Enter m: "))
    b = float(input("Enter b: "))
    linear_equation(m,b)
    plt.show()
elif choice == 2:
    print("y = ax^2 + bx + c")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    quadratic_equation(a,b,c)
    plt.show()
elif choice == 3:
    print("y = ax^3 + bx^2 + cx + d")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    d = float(input("Enter d: "))
    cubic_equation(a,b,c,d)
    plt.show()
else:
    print("invalid choice")
