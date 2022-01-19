def fact(n):
    factorial = 1
    if n == 0 or n == 1:
        print("Factorial of",n,"is 1")
    elif n<0:
        print("Negative numbers factorial does not exsist.")
    else:
        for i in range(1,n+1):
            factorial = factorial * i
        print("Factorial of",n,"is",factorial)
num = int(input("Enter number: "))
fact(num)