Prime number check
def checkPrime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num%2 == 0:
            return False
    return True

while True:
    userNum = int(input("Enter a number: "))
    if checkPrime(userNum):
        print(f"{userNum} is prime")
    else:
        print(f"{userNum} is not prime")

password = "12345"
avalibleAttempts = 3

while avalibleAttempts != 0:
    userPass = input(f"What is the password for the account({avalibleAttempts} Attempts left): ")
    if userPass == password:
        print("welcome")
        break
    elif avalibleAttempts > 1:
        print("Incorrect Please try again")
    avalibleAttempts -= 1
else:
    print("You have run out of attempts")

import time

num = int(input("Enter a number to countdown from: "))

while num > 0:
    mins , sec = divmod(num, 60)
    print(f"{mins} min(s) & {sec} sec(s)")
    time.sleep(1)
    num -= 1
else:
    print("Happy New Year")

def checkLeapYear(year):
    if year % 4 == 0 and year % 200 != 0:
        return True
    else:
        return False

while True:
    userYear = int(input("Give a year: "))
    if checkLeapYear(userYear):
        print(f"{userYear} is a leap year")
    else:
        print(f"{userYear} is not a leap year")

grade = float(input("Enter the grade percentage: "))
if grade > 90:
    print("A")
elif grade > 80:
    print("B")
elif grade > 70:
    print("C")
elif grade > 60:
    print("D")
else:
    print("F")

a = int(input("Enter one side: "))
b = int(input("Enter one side: "))
c = int(input("Enter one side: "))
if a == 0 or b == 0 or c == 0:
    print("It is not a triangle")
elif a == b and b == c:
    print("It is Equalateral")
elif a == b or b == c or a == c:
    print("It is isosoles")
else:
    print("It is scalene")

balance = 1000
amount = float(input("Enter how much you would like to withdraw: "))
if balance - amount >= 0:
    balance -= amount
    print(f"Withdrawl successful\nRemaining balance {balance}")
else:
    print("Withdrawl not successful")

sentence = input("Enter a sentence: ").split(" ")
words = {}

for word in sentence:
    if word.lower() in words:
        words[word.lower()] += 1
    else:
        words[word.lower()] = 1

print(words)
