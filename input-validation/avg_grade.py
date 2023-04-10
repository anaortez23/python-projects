
def main():
    scoreQuantity = int(input("How many scores will you be adding: "))
    while scoreQuantity > 0:
        average(scoreQuantity)


def average(scoreQuantity):
    scoreSum = 0
    for i in range(scoreQuantity):
        scoreInput = int(input("Enter score: "))
        scoreInput + scoreSum
    print(scoreSum)


main()
