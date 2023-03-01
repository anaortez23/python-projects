stop = False

while stop == False:
    num = int(input('Enter a number: '))
    userIn = input("Do you want to continue? type yes or no:   ")
    if userIn != "yes":
        stop = True
