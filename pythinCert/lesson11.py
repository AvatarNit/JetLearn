# Task 1
try:
    value = int(input("Enter a value: "))
    print(value/value)
except ValueError:
    print("Bad Input...")
except ZeroDivisionError:
    print("Very bad input...")
except:
    print("Booo!")

# Task 2
try:
    num = int(input("Enter a value: "))
except ValueError:
    print("Not an Integer")

# Task 3
try:
    num1 = int(input("Enter a value: "))
    num2 = int(input("Enter a value: "))
except ValueError:
    print("Not an Integer")

# Task 4
try:
    list1 = [0,1,2,4]
    list1.apend(5)
except AttributeError:
    print("AttributeError")

# Task 5
try:
    print(10/0)
except ZeroDivisionError:
    print("You cannnot divide by 0")

# Task 6
try:
    userIn = input("Input: ")
except KeyboardInterrupt:
    print("No Input Given")

# Task 7
try:
    list1 = [0,1,2]
    list1.pop(3)
except IndexError:
    print("Index does not exist")

# Task 8
try:
    print(0%0)
except ArithmeticError:
    print("Math error")

# Task 9
try:
    list1 = [0,1,2]
    list1.insrt(1)
except AttributeError:
    print("Insrt does not exist")


# Task 10
try:
    num1 = int(input("Input a number: "))
    num2 = int(input("Input a number: "))
    print(num1/num2)
except:
    print("Bad Input")
else:
    print("You didn't divide by zero!!")
finally:
    print("Numbers are great")
