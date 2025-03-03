def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num-1)

print(factorial(4))

def checkPrime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num%2 == 0:
            return False
    return True
print(checkPrime(7))

def largest(num1,num2,num3):
    if num1 > num2:
        if num1 > num3:
            return num1
        else:
            return num3
    elif num2 > num3:
        return num2
    else:
        return num3

print(largest(5,3,4))

def reverse(str):
    tempStr = ""
    for i in range(len(str)-1,-1,-1):
        tempStr += str[i]
    return tempStr

print(reverse("Hello"))

def checkEmail(email):
    atFound = False
    for i in range(len(email)):
        if atFound:
            if email[i] == ".":
                return True
        elif email[i] == "@":
            atFound = True
            continue
    return False

print(checkEmail("test@testcom"))

def cTof(c):
    return (c * (9/5) + 32)

print(cTof(12))

def checkPalin(str):
    if len(str) % 2 != 0:
        return False
    else:
        lStr = ""
        rStr = ""
        for i in range(int(len(str)/2)):
            lStr += str[i]
        for i in range(int(len(str)-1), int(len(str)/2)-1,-1):
            rStr += str[i]
        return (lStr == rStr)

print(checkPalin("appal"))

def mostFrequent(text):
    words = text.split(" ")
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    maxWord = ""
    maxFrequency = 0
    for word,num in frequency.items():
        if num > maxFrequency:
            maxFrequency = num
            maxWord = word
    return maxWord

print(mostFrequent("The dog went running and running and jumped over a fence and over water"))

import random

def makePassword():
    symbols = ["$","!","@","#","%","^","&","*"]
    letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")
    nums = "1 2 3 4 5 6 7 8 9 0".split(" ")
    all = symbols + letters + nums
    random.shuffle(all)
    passwordChars = []
    passwordChars.append(symbols[random.randrange(len(symbols))])
    passwordChars.append(letters[random.randrange(len(letters))])
    passwordChars.append(nums[random.randrange(len(nums))])
    for i in range(5):
        passwordChars.append(all[random.randrange(len(all))])
        random.shuffle(passwordChars)
    random.shuffle(passwordChars)
    password = ""
    for i in passwordChars:
        password += i
    return password

print(makePassword())

def mostFrequentVowl(text):
    word = []
    for i in text:
        word.append(i)
    frequency = {}
    for letter in word:
        if letter in ["a","e","i","o","u"]:
            if letter in frequency:
                frequency[letter] += 1
            else:
                frequency[letter] = 1
    maxLetter = ""
    maxFrequency = 0
    for letter,num in frequency.items():
        if num > maxFrequency:
            maxFrequency = num
            maxLetter = letter
    return maxLetter

print(mostFrequentVowl("hello its october"))