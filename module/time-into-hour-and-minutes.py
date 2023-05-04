def main():
    userInput = int(input('Enter time in minutes: '))
    h, m = convertTime(userInput)
    print(h, "hr :", m, "min")


def convertTime(userInput):
    hours = int(userInput/60)
    minutes = userInput % 60
    return hours, minutes


main()
