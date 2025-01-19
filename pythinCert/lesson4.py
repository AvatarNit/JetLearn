# Task 1
num = int(input("Input a number: "))

if num != 0:
    print("The number is positive" if num > 0 else "The number is negative")
    print("That is an even number" if num % 2 ==0 else "That is an odd number")
else:
    print("The number is zero and is neither odd nor even \nThe number is zero and is neither positive nor negative")

# Task 2
dist = int(input("Input a distance: "))
age = int(input("Input an age: "))

if dist < 1000:
    if age < 12:
        print("$200")
    elif age <= 64:
        print("$300")
    else:
        print("$250")
else:
    if age < 12:
        print("$400")
    elif age <= 64:
        print("$500")
    else:
        print("$450")

# Task 3

age = int(input("Input an age: "))

if age < 12 or age >= 65:
    print("Highest priority")
elif age >= 12 and age <= 64:
    print("Medium priority")
else:
    print("Lowest priority")

# Task 4

income = int(input("Input your income: "))
healthIn = bool(input("Input if health insurance is paid: "))
charityMade = bool(input("Input if you have made charitable donations: "))
taxRate = 0

if income < 10000:
    taxRate += 0
elif income > 10000 and income < 50000:
    taxRate += 10
else:
    taxRate += 20

if healthIn:
    taxRate -= 5
elif charityMade:
    taxRate -= 10

print("Your tax rate is" , taxRate)