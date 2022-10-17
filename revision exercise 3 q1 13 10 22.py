def factorial(n):
    if (n == 1 or n == 0):
        return 1
    else:
        return n * factorial(n-1)

num = int(input('Enter Number: '))
print(factorial(num))

# took code from github as i dont know factiorial at all and didnt understand how to do it myself ever
