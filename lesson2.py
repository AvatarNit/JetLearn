num1 = int(input("Input the first number: "))
num2 = int(input("Input the second number: "))

if num1 > num2:
    print(num1 , " - " , num2 , " = " , (num1-num2))
elif num1 < num2:
    print(num1 , " + " , num2 , " = " , (num1+num2))
else:
    print(num1 , " == " , num2 , "=" , (num1==num2))

