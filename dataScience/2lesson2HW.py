def linear_equation(m,b):
    return [m*x + b for x in range(11)]

def quadratic_equation(a,b,c):
    return [a*x**2 + b*x + c for x in range(11)]

print("1. Linear equation\n2. Quadratic equation")
choice = int(input(": "))

if choice == 1:
    print("y = mx + b")
    m = float(input("Enter m: "))
    b = float(input("Enter b: "))
    results = linear_equation(m,b)
elif choice == 2:
    print("y = ax^2 + bx + c")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    results = quadratic_equation(a,b,c)
else:
    print("invalid choice")

print(results)