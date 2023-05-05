#1 Module calling another
"""def main():
    num1 = int(input('Enter a number:'))
    num2 = int(input('Enter a number:'))
    showSum(num1, num2)


def showSum(n1, n2):
    total = n1+n2
    print(total)

main()"""

#1 Module calling a function
def main():
    num1 = int(input('Enter a number:'))
    num2 = int(input('Enter a number:'))
    output = showSum(num1, num2)
    print(output)

def showSum(n1, n2):
    total = n1+n2
    return total

main()