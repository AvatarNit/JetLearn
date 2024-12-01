
# mx+b
def linear_equation(m,b):
    return [m*x + b for x in range(11)]

def quadratic_equation(a,b,c):
    return [a*x**2 + b*x + c for x in range(11)]

def main():
    print("Choose the equation type: ")
    print("1. Linear equation: (y = mx+b)")
    print("2. Quadratic equation: (y = ax^2 + bx + c)")
    choice = int(input("Enter 1 for Linear and 2 for Quadratic\n  :"))

    if choice == 1:
        print("You chose Linear Equation (y = mx + b)")
        m = float(input("Enter coefficient m: "))
        b = float(input("Enter constant b: "))
        results = linear_equation(m,b)
    elif choice == 2:
        print("You chose Quadratic Equation (y = ax^2 + bx + c)")
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter constant c: "))
        results = quadratic_equation(a,b,c)
    else:
        print("invalid choice")
    
    print("Results for x = 0 to x = 10")
    for x , y in enumerate(results):
        print(f"x = {x}, y = {y}")

main()
