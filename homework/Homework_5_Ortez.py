import random


def main():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print("number one: ", num1)
    print("number two: ", num2)

    result = calculateSum(num1, num2)
    print("The sum of two squares: ", result)


def calculateSum(num1, num2):
    result = num1**2 + num2**2
    print("number one squared: ", num1**2)
    print("number two squared: ", num2**2)
    return (result)


main()
