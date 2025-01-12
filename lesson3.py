# # Task 1: Find leap year
# year = int(input("Input a year: "))

# if year % 4 == 0 and year % 400 != 0:
#     print(year , "is a leap year")
# else:
#     print(year , "is not a leap year")

# Task 2

num1 = int(input("Input a num: "))
num2 = int(input("Input a num: "))

# ternary operator
print(f"The smallest number between {num1} and {num2} is {num1 if num1 < num2 else num2}")

# Bitwise AND
print(f"Bitwise AND of {num1} and {num2} is {num1 & num2}")

# Bitwise OR
print(f"Bitwise OR of {num1} and {num2} is {num1 | num2}")

# Bitwise not for first num
print(f"Bitwise not of {num1} is {~num1}")

# 1-bit left shift of second num
print(f"1-bit left shift of {num2} is {num2 << 1}")

# 2-bit right shift of second num
print(f"2-bit right shift of {num2} is {num2 >> 2}")