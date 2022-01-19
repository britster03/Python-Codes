str1= "SOFTWARE SPECIFICATIONS :   LANGUAGES TO BE USED : HTML , CSS , JAVASCRIPT ,  STYLES TO BE USED : BOOTSTRAP FRAMEWORK TO BE USED : DJANGO (PYTHON WEB FRAMEWORK    DATABASE TO BE USED : Django "
str2= "Python programming is powerful and joyful"
print("string1 : ",str1)
print("string2 : ",str2)
#adding two strings
str= str1+str2
print("addition of two strings : ",str )

#printing str2 10 times
print(10*(str2 +'\n' ))

#finding length of strings
print(len(str1))
print(len(str2))

#Converting String str to Upper, Lower, Title, Capitalization
str= str1+str2
print("addition of two strings : ",str )
print(str.upper())
print(str.lower())
print(str.title())
print(str.capitalize())
print("Normal string : " ,str1)

#replace easy from str1 to popular and print again
str=str1.replace('easy','popular')
print("Replaced string : ", str)


#Find Start and End of both the String and show to users
print(str1.startswith("Python"))
print(str1.endswith("easy"))
print(str2.startswith("Python"))
print(str2.endswith("joyful"))


def triangle():
    a = int(input("Enter Side1: "))
    b = int(input("Enter Side2: "))
    c = int(input("Enter Side3: "))
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or c == a:
        print("Isoceles")
    else:
        print("Scalene")

triangle()


def usingfor(a):
    for i in range(1, a + 1):
        print(i, end=",")
        if i % 10 == 0:
            print("\b")


def usingwhile(a):
    i = 1
    while i <= a:
        print(i, end=",")
        if i % 10 == 0:
            print("\b")
        i += 1

num = int(input("enter a number: "))
print("Using for loop:")
usingfor(num)
print("\n\nUsing while loop:")
usingwhile(num)

import math

def add(num1, num2):
    return (num1+num2)


def sub(num1, num2):
    return (num1 - num2)


def mul(num1, num2):
    return (num1 * num2)


def div(num1, num2):
    return (num1 / num2)


def mod(num1, num2):
    return (num1 % num2)


def exp(num1, num2):
    return (math.exp(num1))


def menu():
    num1 = int(input("1st number:"))
    num2 = int(input("2nd number:"))
    choice = int(input("1-ADDITION, 2-SUBTRACTION, 3-MULTIPLICATION, 4-DIVISION, 5-MODULUS, 6-EXPONENTIAL"))

    if (choice == 1):
        print("addition is:", add(num1, num2))
    if (choice == 2):
        print("subtraction is:", sub(num1, num2))
    if (choice == 3):
        print("multiplication is:", mul(num1, num2))
    if (choice == 4):
        print("division is:", div(num1, num2))
    if (choice == 5):
        print("{} modulus {} is:".format(num1, num2), mod(num1, num2))
    if (choice == 6):
        print("{} raised to {} is:".format(num1, num2), exp(num1, num2))


menu()