import math


def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s * s == x


def isFibonacci(n):
    # n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both

    # is a perferct square

    return isPerfectSquare(5 * n * n + 4) or isPerfectSquare(5 * n * n - 4)


# print(isFibonacci(35))
choice='y'
while choice == 'y':
    num = int(input("enter a number to check fibonacci or not"))
    if isFibonacci(num) == True:
        print(num, "is a fibonacci number")
    else:
        print(num, "is not a fibonacci number")
    choice= input("enter y for yes or n for No")

